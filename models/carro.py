from dataclasses import dataclass


@dataclass
class Carro:

    categoria: str
    transmissao: str
    combustivel: str
    marca: str
    modelo: str

    @classmethod
    def criar_carro(cls, categoria, transmissao, combustivel, marca, modelo, **kwargs):
        novo_carro = Carro(categoria, transmissao, combustivel, marca, modelo)
        for atributo, valor in kwargs.items():
            setattr(novo_carro, atributo, valor)
        return novo_carro