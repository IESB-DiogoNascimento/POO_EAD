from datetime import datetime
from abc import ABC, abstractmethod
from models import Cliente, Carro, Aluguel


class InterfaceControladora(ABC):
    
    @abstractmethod
    def cadastrar_novo_veiculo(self):
        pass
    @abstractmethod
    def cadastrar_novo_cliente(self):
        pass
    @abstractmethod
    def realizar_locacao_veiculo(self):
        pass
    @abstractmethod
    def get_lista_locacoes(self):
        pass
    @abstractmethod
    def get_lista_veiculos(self):
        pass


class ControladorLocacao(InterfaceControladora):
    def __init__(self):
        self.__lista_veiculos = []
        self.__lista_clientes = {}
        self.__lista_locacoes = []
        self.__lista_veiculos_indisponiveis = []

    def cadastrar_novo_veiculo(self,
                                categoria, 
                                transmissao, 
                                combustivel, 
                                marca, 
                                modelo,
                                **kwargs):
        idx_veiculo = len(self.__lista_veiculos)
        novo_veiculo = Carro.criar_carro(idx_veiculo, categoria, transmissao, combustivel, marca, modelo, **kwargs)
        self.__lista_veiculos.append(novo_veiculo)

    def cadastrar_novo_veiculo_a_partir_de_veiculo_previamente_cadastrado(self, idx_carro, **kwargs):
        veiculo_previamente_cadastrado = self.get_carro(idx_carro)
        idx_veiculo = len(self.__lista_veiculos)
        novo_veiculo = veiculo_previamente_cadastrado.copy(idx_veiculo)
        self.__lista_veiculos.append(novo_veiculo)

    def atualizar_atributos_carro(self, idx_carro, dict_atributos):
        carro = self.get_carro(idx_carro)
        for atributo, valor in dict_atributos.items():
            carro.set_atributo(atributo, valor)
        
        self.set_carro(idx_carro, carro)

    def get_lista_veiculos(self):
        return list(self.__lista_veiculos)

    def cadastrar_novo_cliente(self, nome, cpf, rg):
        self.__lista_clientes[cpf] = Cliente.criar_cliente(nome, cpf, rg)
        
    def realizar_locacao_veiculo(self, idx_carro, cpf_cliente, data_inicio, data_fim):
        try:
            carro = self.get_carro(idx_carro)
            cliente = self.get_cliente(cpf_cliente)
            inicio = datetime.strptime(data_inicio, '%d/%m/%Y')
            fim = datetime.strptime(data_fim, '%d/%m/%Y')
        except IndexError:
            return 1
        except KeyError:
            return 2
        except ValueError:
            return 3
        
        for locacao in self.__lista_locacoes:
            carro_locado = locacao.get_carro()

            if carro_locado.get_id() == (idx_carro-1):
                if locacao.get_fim() > inicio:
                    return 4
        
        novo_aluguel = Aluguel(carro, cliente, inicio, fim)

        self.__lista_locacoes.append(novo_aluguel)
    
    def get_lista_locacoes(self):
        return list(self.__lista_locacoes)

    def get_carro(self, idx_carro):
        return self.__lista_veiculos[idx_carro-1]

    def set_carro(self, idx_carro, carro):
        self.__lista_veiculos[idx_carro-1] = carro
    
    def get_cliente(self, cpf_cliente):
        return self.__lista_clientes[cpf_cliente]
    
