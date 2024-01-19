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

    def obter_usuario_por_id(self, user_id):
        try:
            usuario_recuperado = self.dados_usuario.selecionar_usuario_por_id(user_id)
            if usuario_recuperado:
                return {"usuario": usuario_recuperado.__dict__}
            else:
                return {"mensagem": "Usuário não encontrado."}
        except ValueError as ex:
            return {"erro": f"Erro ao obter usuário por ID: {str(ex)}"}
        
    def login(self, login, senha):
        try:
            usuario_recuperado = self.dados_usuario.login(login, senha)

            if usuario_recuperado:
                return {"usuario": usuario_recuperado.__dict__}
            else:
                return {"mensagem": "Login ou senha incorretos."}

        except ValueError as ex:
            return {"erro": f"Erro durante o processo de login: {str(ex)}"}

    def atualizar_usuario(self, user_id, login, senha, nome_usuario, perfil):
        try:
            usuario_atualizado = Usuario(login, senha, nome_usuario, Perfil(perfil))
            usuario_atualizado.id = user_id
            self.dados_usuario.atualizar_usuario(usuario_atualizado)
            return {"mensagem": "Usuário atualizado com sucesso!"}
        except ValueError as ex:
            return {"erro": f"Erro ao atualizar usuário: {str(ex)}"}

    def excluir_usuario(self, user_id):
        try:
            self.dados_usuario.excluir_usuario(user_id)
            return {"mensagem": "Usuário excluído com sucesso!"}
        except ValueError as ex:
            return {"erro": f"Erro ao excluir usuário: {str(ex)}"}
