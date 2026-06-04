import sqlite3
import hashlib

while True:

    print("\n=== SISTEMA ===")
    print("1 - Login")
    print("2 - Cadastrar usuário")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    # LOGIN
    if opcao == "1":

        usuario = input("Usuário: ")
        senha = input("Senha: ")

        senha_hash = hashlib.sha256(
            senha.encode()
        ).hexdigest()

        conexao = sqlite3.connect("usuarios.db")
        cursor = conexao.cursor()

        cursor.execute(
            """
            SELECT * FROM usuarios
            WHERE usuario = ?
            AND senha = ?
            """,
            (usuario, senha_hash)
        )

        resultado = cursor.fetchone()

        if resultado:
            print("\nLogin realizado com sucesso!")
        else:
            print("\nUsuário ou senha incorretos.")

        conexao.close()

    # CADASTRO
    elif opcao == "2":

        usuario = input("Novo usuário: ")
        senha = input("Nova senha: ")

        senha_hash = hashlib.sha256(
            senha.encode()
        ).hexdigest()

        conexao = sqlite3.connect("usuarios.db")
        cursor = conexao.cursor()

        try:
            cursor.execute(
                "INSERT INTO usuarios(usuario, senha) VALUES (?, ?)",
                (usuario, senha_hash)
            )

            conexao.commit()

            print("Usuário cadastrado com sucesso!")

        except sqlite3.IntegrityError:
            print("Usuário já existe!")

        conexao.close()

    # SAIR
    elif opcao == "3":

        print("Encerrando sistema...")
        break

    else:
        print("Opção inválida!")