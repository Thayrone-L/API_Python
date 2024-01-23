import re

class Cpf:
    def __init__(self, cpf):
        self._cpf = self._limpar_cpf(cpf)
        self.validar_cpf()

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, novo_cpf):
        novo_cpf = self._limpar_cpf(novo_cpf)
        self._cpf = novo_cpf
        self.validar_cpf()

    def _limpar_cpf(self, cpf):
        return ''.join(digito for digito in cpf if digito.isdigit())

    def validar_cpf(self):
        # Verifica a estrutura do CPF (111.222.333-44)
        if len(self._cpf) != 11:
            raise ValueError(f"O CPF {self._cpf} não possui 11 dígitos. Tente outro CPF.")

        soma_produtos = sum(int(a) * b for a, b in zip(self._cpf[:9], range(10, 1, -1)))
        digito_esperado = (soma_produtos * 10) % 11 % 10
        if int(self._cpf[9]) != digito_esperado:
            raise ValueError(f"O CPF {self._cpf} não é válido. Tente outro CPF.")

        soma_produtos1 = sum(int(a) * b for a, b in zip(self._cpf[:10], range(11, 1, -1)))
        digito_esperado1 = (soma_produtos1 * 10) % 11 % 10
        if int(self._cpf[10]) != digito_esperado1:
            raise ValueError(f"O CPF {self._cpf} não é válido. Tente outro CPF.")

    def to_json(self):
        return {'cpf': str(self._cpf)}