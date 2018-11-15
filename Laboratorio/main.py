from Interfaz.Login import Login
from Código.BD import *


def main(bd):
    login = Login(bd)
    return 0


if __name__ == '__main__':
    bd = BD()
    main(bd)
