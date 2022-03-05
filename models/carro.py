from dataclasses import dataclass


@dataclass
class Carro:

    categoria: str
    transmissao: str
    combustivel: str
    marca: str
    modelo: str

    def set_atributo(self, nome: str, valor: str):
        setattr(self, nome, valor)

    @classmethod
    def criar_carro(cls, categoria, transmissao, combustivel, marca, modelo, **kwargs):
        novo_carro = Carro(categoria, transmissao, combustivel, marca, modelo)
        for atributo, valor in kwargs.items():
            setattr(novo_carro, atributo, valor)
        return novo_carro
    
    def copy(self):
        return self.criar_carro(self.categoria, self.transmissao, self.combustivel, self.marca, self.modelo)

    def __str__(self):
        return '\n'.join([f'{attr}: {value}' for attr, value in self.__dict__.items()])