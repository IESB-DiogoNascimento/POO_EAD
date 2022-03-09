from dataclasses import dataclass


@dataclass
class Carro:

    __idx: str
    categoria: str
    transmissao: str
    combustivel: str
    marca: str
    modelo: str

    def get_id(self):
        return self.__idx

    def set_atributo(self, nome: str, valor: str):
        setattr(self, nome, valor)

    @classmethod
    def criar_carro(cls, idx, categoria, transmissao, combustivel, marca, modelo, **kwargs):
        novo_carro = Carro(idx, categoria, transmissao, combustivel, marca, modelo)
        for atributo, valor in kwargs.items():
            setattr(novo_carro, atributo, valor)
        return novo_carro
    
    def copy(self, novo_idx: int):
        return self.criar_carro(novo_idx, self.categoria, self.transmissao, self.combustivel, self.marca, self.modelo)

    def __str__(self):
        return '\n'.join([f'{attr}: {value}' for attr, value in self.__dict__.items() if '__idx' not in attr])