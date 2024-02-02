import sys
sys.path.append(r'C:\Users\thayr\OneDrive\Documentos\repositorios\Python\Testes\API_Python')

from Dao.ConexaoSQL import ConexaoBanco
from Entidades.Funcionario import Funcionario

class _FuncionarioDados:
    def __init__(self):
        self.conexao = ConexaoBanco()
    
    def buscar_funcionario_por_cpf(self, cpf):
        print("buscar_funcionario_por_cpf")
        try:
            self.conexao.conectar()
                # Se não existe, então inserir o funcionário
            parametros = (cpf,)
            self.conexao.executar_procedure('BuscarFuncionarioPorCPF', parametros)
            self.conexao.cursor.commit()

                
        except ValueError as ex:
            raise ValueError(f"Erro ao consultar funciona funcionário: {ex}")
        finally:
            self.conexao.fechar_conexao()

    def inserir_funcionario(self, funcionario):
        try:
            self.conexao.conectar()
                # Se não existe, então inserir o funcionário
            parametros = (funcionario.login, funcionario.senha, funcionario.nome_funcionario, funcionario.cpf, int(funcionario.perfil))
            self.conexao.executar_procedure('InserirFuncionario', parametros)
            self.conexao.cursor.commit()

                
        except ValueError as ex:
            raise ValueError(f"{ex}")
        finally:
            self.conexao.fechar_conexao()

            
    def login(self, login, senha):
        try:
            self.conexao.conectar()
            parametros = (login, senha)
            resultado = self.conexao.executar_procedure('Login', parametros)
            
            if resultado and len(resultado) > 0:
                funcionario_data = resultado[0]

                if len(funcionario_data) >= 3:
                    funcionario = Funcionario(
                    login=login,
                    senha=senha,
                    nome_funcionario=funcionario_data[0],
                    perfil=funcionario_data[1],
                    cpf_param=funcionario_data[2]
                )
                    return funcionario.to_json()
                else:
                    return None
            else:
                return None
        except ValueError as ex:
            raise ValueError(f"Erro ao selecionar funcionário por login e senha: {ex}")
        finally:
            self.conexao.fechar_conexao()

# Exportar a instância da classe interna
FuncionarioDados = _FuncionarioDados()
