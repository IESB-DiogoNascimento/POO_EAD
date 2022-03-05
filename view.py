from controller import InterfaceControladora

class ViewPrincipal:
    def __init__(self, controlador: InterfaceControladora):
        self.mensagem_boasvindas()
        opcao = True
        while opcao != 9:
            opcao = self.imprimir_menu()
            if opcao == 1:
                self.cadastrar_novo_veiculo(controlador)
            if opcao == 2:
                self.cadastrar_novo_cliente(controlador)
            if opcao == 3:
                self.realizar_locacao_veiculo(controlador)
            if opcao == 4:
                self.relatorio_de_locacao(controlador)
                
    def mensagem_boasvindas(self):
        print('Bem-vindo a Locadora Boa Viagem, escolha uma das opções abaixo:')
    
    def imprimir_menu(self):
        print('''
1)  Cadastrar um Novo Veiculo 
2)  Cadastrar um Novo Cliente 
3)  Realizar a locação de um Veículo 
4)  Relatório de locação 
9)  Exit program
''')
        return int(input('Escolha uma das opções: '))
        

    def cadastrar_novo_veiculo(self, controlador):
        print('\nLista de categorias previamente cadastradas:')
        
        self.mostrar_veiculos(controlador)
        
        opcao = input('\nO carro que será cadastrado está em uma das categorias listadas acima [S/N]: ')
        
        if opcao.lower() == 'n':
            categoria = input('Entre com o nome da categoria: ')
            transmissao = input('Informe a Transmissão: ') 
            combustivel = input('Informe o tipo de Combustível: ')
            marca = input('Informe a Marca: ')
            modelo = input('Informe o Modelo: ')
            
            print('Atributos do carro:')
            ano = input('Ano: ')
            placa = input('Placa: ')
            controlador.cadastrar_novo_veiculo(categoria, 
                                                transmissao, 
                                                combustivel, 
                                                marca, 
                                                modelo,
                                                ano=ano,
                                                placa=placa)
        elif opcao.lower() == 's':
            idx_carro = int(input('Qual o número da categoria do carro a ser cadastrado: '))
            
            print('Atributos do carro:')
            ano = input('Ano: ')
            placa = input('Placa: ')
            
            controlador.cadastrar_novo_veiculo_a_partir_de_veiculo_previamente_cadastrado(idx_carro, ano=ano, placa=placa)

    def mostrar_veiculos(self, controlador: InterfaceControladora):
        lista_veiculos = controlador.get_lista_veiculos()
        if len(lista_veiculos) == 0:
            print('\nNenhum veículo cadastrado.')
        else:
            for idx, carro in enumerate(lista_veiculos):
                print(f'\nnumero: {idx+1}')
                print(carro)

    def cadastrar_novo_cliente(self, controlador):
        nome = input('Nome: ')
        cpf = input('cpf: ')
        rg = input('rg: ')
        controlador.cadastrar_novo_cliente(nome, cpf, rg)

    def realizar_locacao_veiculo(self, controlador):
        self.mostrar_veiculos(controlador)
        idx_carro = int(input('Qual Carro o cliente irá alugar: '))
        cpf_cliente = input('Qual o CPF do cliente: ')
        data_inicio = input('Qual o início da locação (dd/mm/yyyy): ')
        data_fim = input('Qual o fim da locação (dd/mm/yyyy): ')
        error = controlador.realizar_locacao_veiculo(idx_carro, cpf_cliente, data_inicio, data_fim)
        if error is None:
            return
        elif error == 1:
            print('\nCarro não identificado, entre com um número de categoria válido.')
        elif error == 2:
            print('\nCliente não cadastrado.')
        elif error == 3:
            print('\nData em formato inválido, por favor utilize o formato dd/mm/yyyy.')
        input('Pressione enter para continuar.')
        
    def relatorio_de_locacao(self, controlador):
        lista_locacoes = controlador.get_lista_locacoes()
        if len(lista_locacoes) == 0:
            print('\nNenhuma locação cadastrado.')
        else:
            for idx, locacao in enumerate(lista_locacoes):
                print(f'Locacao: {idx+1}')
                print(locacao)