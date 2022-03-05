from view import ViewPrincipal
from controller import ControladorLocacao

if __name__ == '__main__':
    controlador = ControladorLocacao()
    ViewPrincipal(controlador)