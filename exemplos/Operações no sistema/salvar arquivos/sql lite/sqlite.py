import sqlite3


def create_connection():

    conectar = sqlite3.connect("./dados.db")

    cursor = conectar.cursor()

    # Exemplo de criação de tabela
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS usuarios
                    (id INTEGER PRIMARY KEY, nome TEXT, idade INTEGER)"""
    )

    # Exemplo de inserção de dados
    cursor.execute("INSERT INTO usuarios (nome, idade) VALUES (?, ?)", ("João", 30))

    # Exemplo de consulta de dados
    cursor.execute("SELECT * FROM usuarios")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Exemplo de atualização de dados
    cursor.execute("UPDATE usuarios SET idade = 25 WHERE nome = 'João'")

    # Exemplo de exclusão de dados
    cursor.execute("DELETE FROM usuarios WHERE idade < 20")

    conectar.commit()
    conectar.close()


if __name__ == "__main__":
    create_connection()
