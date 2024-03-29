import pyodbc

class ConexaoBanco:
    # String de conexão fixa
    CONNECTION_STRING = 'DRIVER={SQL Server};SERVER=MONSTRO\SQLEXPRESS;DATABASE=BancoBase;Trusted_Connection=yes'

    def __init__(self):
        self.connection = None
        self.cursor = None

    def conectar(self):
        try:
            self.connection = pyodbc.connect(self.CONNECTION_STRING)
            self.cursor = self.connection.cursor()
            print("Conexão bem-sucedida!")
        except pyodbc.Error as ex:
            raise ValueError(f"Erro ao conectar ao banco de dados: {ex}")

    def executar_procedure(self, nome_procedure, parametros):
        try:
            placeholders = ', '.join(['?' for _ in parametros])
            sql = f"EXEC {nome_procedure} {placeholders}"

            self.cursor.execute(sql, parametros)

            # Verifica se a consulta atual é uma SELECT antes de tentar recuperar resultados
            if self.cursor.description is not None:
                results = self.cursor.fetchall()
                # Se necessário, você pode retornar os resultados aqui
                return results
            else:
                # Se a stored procedure não retornar resultados
                return {"mensagem": "Operação realizada com sucesso!"}
        except pyodbc.Error as ex:
            self.connection.rollback()
            error_message = str(ex)
            start_index = error_message.find("Erro:")
            end_index = error_message.find("!")
    
            if start_index != -1 and end_index != -1:
                # Extrair a mensagem específica
                error_message = error_message[start_index + 5:end_index + 1].strip()
            raise ValueError(f"Erro: {error_message}")



    def fechar_conexao(self):
        try:
            if self.cursor:
                self.cursor.close()
        except Exception as ex:
            raise ValueError(f"Erro ao fechar o cursor: {ex}")
        finally:
            try:
                if self.connection:
                    self.connection.close()
                    print("Conexão fechada.")
            except Exception as ex:
                raise ValueError(f"Erro ao fechar a conexão: {ex}")
