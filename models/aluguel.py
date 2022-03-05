from datetime import datetime
from dataclasses import dataclass
from .cliente import Cliente
from .carro import Carro


class Aluguel:
    def __init__(self, 
                carro: Carro, 
                cliente: Cliente, 
                inicio: datetime, 
                fim: datetime):
        self.__carro = carro
        self.__cliente = cliente
        self.__inicio = inicio
        self.__fim = fim

    def get_carro(self):
        return self.__carro
    
    def get_cliente(self):
        return self.__cliente
    
    def get_inicio(self):
        return self.__inicio
    
    def get_fim(self):
        return self.__fim

    def __str__(self):
        return \
f'''
Data Inicio: {self.get_inicio().strftime('%d/%m/%Y')}
Data Fim: {self.get_fim().strftime('%d/%m/%Y')}

Carro Alugado:
{self.get_carro()}

Cliente:
{self.get_cliente()}
'''