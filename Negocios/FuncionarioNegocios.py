import sys
sys.path.append(r'C:\Users\thayr\OneDrive\Documentos\repositorios\Python\Testes\API_Python')

from Entidades.Funcionario import Funcionario
from Enums.Perfil import Perfil

class FuncionarioNegocios:
    def __init__(self, dados_funcionario):
        self.dados_funcionario = dados_funcionario

    def criar_funcionario(self, login, senha, nome_funcionario, cpf, perfil):
        try:
            novo_funcionario = Funcionario(login, senha, nome_funcionario, cpf, perfil)
            resultado = self.dados_funcionario.buscar_funcionario_por_cpf(cpf)

            if resultado is None or ('FuncionarioExiste' in resultado and resultado['FuncionarioExiste'] == 0):
                self.dados_funcionario.inserir_funcionario(novo_funcionario)
                return {"mensagem": "Funcionário criado com sucesso!"}
            else:
                return {"mensagem": "Funcionário já existe no sistema, verifique e tente novamente."}

        except ValueError as ex:
            return {"erro": f"Erro ao criar funcionário: {str(ex)}"}

        
    def login(self, login, senha):
        try:
            funcionario_recuperado = self.dados_funcionario.login(login, senha)

            if funcionario_recuperado:
                return {"funcionario": funcionario_recuperado}
            else:
                return {"mensagem": "Login ou senha incorretos."}

        except ValueError as ex:
            return {"erro": f"Erro durante o processo de login: {str(ex)}"}
