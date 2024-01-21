import sys
sys.path.append(r'C:\Users\thayr\OneDrive\Documentos\repositorios\Python\Testes\API_Python')

from Entidades.Usuario import Usuario
from Enums.Perfil import Perfil

class UsuarioNegocios:
    def __init__(self, dados_usuario):
        self.dados_usuario = dados_usuario

    def criar_usuario(self, login, senha, nome_usuario, perfil):
        try:
            novo_usuario = Usuario(login, senha, nome_usuario, perfil)
            self.dados_usuario.inserir_usuario(novo_usuario)
            return {"mensagem": "Usuário criado com sucesso!"}
        except ValueError as ex:
            return {"erro": f"Erro ao criar usuário: {str(ex)}"}

        
    def login(self, login, senha):
        try:
            usuario_recuperado = self.dados_usuario.login(login, senha)

            if usuario_recuperado:
                return {"usuario": usuario_recuperado.__dict__}
            else:
                return {"mensagem": "Login ou senha incorretos."}

        except ValueError as ex:
            return {"erro": f"Erro durante o processo de login: {str(ex)}"}
