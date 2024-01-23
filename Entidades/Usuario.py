import sys
sys.path.append(r'C:\Users\thayr\OneDrive\Documentos\repositorios\Python\Testes\API_Python')
import re
from Enums.Perfil import Perfil
from .Cpf import Cpf

class Usuario:
    def __init__(self, login, senha, nome_usuario, cpf_param, perfil):
        self.login = login
        self.senha = senha
        self.nome_usuario = nome_usuario
        self._cpf = Cpf(cpf_param)
        self._perfil = perfil
        
    def to_json(self):
        return {
            'login': self.login,
            'senha': self.senha,
            'nome_usuario': self.nome_usuario,
            'perfil': self.perfil,
            'cpf_param': str(self.cpf_param)
        }

    @property
    def perfil(self):
        return self._perfil

    @perfil.setter
    def perfil(self, novo_perfil):
        if not isinstance(novo_perfil, Perfil):
            raise ValueError("O perfil deve ser uma instância do enum Perfil.")
        self._perfil = novo_perfil

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, novo_login):
        if not isinstance(novo_login, str) or len(novo_login) < 6 or not novo_login.islower() or not novo_login.isalpha():
            raise ValueError("Login deve conter pelo menos 6 letras minúsculas e não pode conter caracteres especiais ou espaços.")
        self._login = novo_login

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, nova_senha):
        if not isinstance(nova_senha, str) or len(nova_senha) < 8 or not any(c.isupper() for c in nova_senha) \
                or not any(c.islower() for c in nova_senha) or not any(c.isdigit() for c in nova_senha) \
                or not any(c in "!@#$%^&*()-_+=" for c in nova_senha):
            raise ValueError("Senha deve conter pelo menos 8 caracteres, com pelo menos 1 letra maiúscula, 1 letra minúscula, 1 número e 1 caractere especial.")
        self._senha = nova_senha

    @property
    def nome_usuario(self):
        return self._nome_usuario
    
    @property
    def cpf(self):
        return self._cpf.cpf
    
    @cpf.setter
    def cpf(self, novo_cpf):
        try:
            self._cpf.cpf = novo_cpf
        except ValueError as e:
            raise ValueError(f"CPF inválido: {e}")
    

    @nome_usuario.setter
    def nome_usuario(self, novo_nome_usuario):
        if not isinstance(novo_nome_usuario, str) or len(novo_nome_usuario) < 3 or not re.match("^[a-zA-ZáéíóúâêîôûãõàèìòùäëïöüçÁÉÍÓÚÂÊÎÔÛÃÕÀÈÌÒÙÄËÏÖÜÇ ]+$", novo_nome_usuario):
            raise ValueError("Nome de usuário deve conter pelo menos 3 letras, sem caracteres especiais")
        self._nome_usuario = novo_nome_usuario
