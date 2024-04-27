from datetime import date, datetime


def lerDados(arquivo: str) -> None:
    with open(arquivo, "r") as dados:
        for linha in dados:
            # Se a linha começa com um número, assume-se que seja um timestamp
            if linha[0].isdigit():
                timestamp = float(linha.strip())
                data_hora = datetime.fromtimestamp(timestamp)
                print(data_hora.strftime("%Y-%m-%d %H:%M"))
            else:
                print(linha, end="")


def main(arquivo: str) -> None:
    token = "123abc"

    with open(arquivo, "w") as file:
        now = datetime.now()
        timestamp = now.timestamp()
        file.write(str(timestamp) + "\n")
        file.write(f"Token = {token}\n")


if __name__ == "__main__":
    arquivo = "Save-file.txt"
    escolha = int(input("1 - ver dados / 2 - atualizar"))

    if escolha == 1:
        lerDados(arquivo=arquivo)
    elif escolha == 2:
        main(arquivo=arquivo)
    else:
        print("Operação invalida")
