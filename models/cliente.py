from dataclasses import dataclass


@dataclass
class Cliente:

    nome: str
    cpf: str
    rg: str
    

    @classmethod
    def criar_cliente(cls, nome, cpf, rg, **kwargs):
        novo_cliente = Cliente(nome, cpf, rg)
        for atributo, valor in kwargs.items():
            setattr(novo_cliente, atributo, valor)
        return novo_cliente
    
    def __str__(self):
        return '\n'.join([f'{attr}: {value}' for attr, value in self.__dict__.items()])