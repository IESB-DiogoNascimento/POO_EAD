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