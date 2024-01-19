from enum import Enum

class Perfil(Enum):
    ADMIN = ("Admin", 1)
    USUARIO_COMUM = ("Usuario Comum", 2)

    def __new__(cls, nome, valor_inteiro):
        obj = object.__new__(cls)
        obj._value_ = nome
        obj.valor_inteiro = valor_inteiro
        return obj

    def __int__(self):
        return self.valor_inteiro
