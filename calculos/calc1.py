"""
 # @ Author: Marcel Barreto
 # @ Create Time: 2023-12-16 20:23:11
 # @ Modified by: Marcel Barreto
 # @ Modified time: 2023-12-16 20:23:34
 # @ Description: Calculadora simples baseada no input de dois numeros do usuário
 """


def main():
    valores = []
    operacoes = {"+", "-", "/", "*"}
    cont = 1

    while cont < 3:
        try:
            valores.append(float(input(f"\nDigite o {cont}º da operação: ")))
            cont += 1
        except ValueError:
            print("Insira valores válidos")

    ope = input(
        "\nInforme uma das operações abaixo:\n    + soma\n    - subtração\n   / divisão\n   * multiplicação\n"
    )

    ### Válida se a operação que o usuário utilizou está na lista das operações suportadas"

    if ope in operacoes:
        if ope == "+":
            resultado = valores[0] + valores[1]
        elif ope == "-":
            resultado = valores[0] - valores[1]
        elif ope == "/":
            # Evitar a divisão por zero
            if valores[1] != 0:
                resultado = valores[0] / valores[1]
            else:
                print("Erro: divisão por zero.")
                resultado = None
        elif ope == "*":
            resultado = valores[0] * valores[1]
        else:
            print("Operação não reconhecida.")
            resultado = None

        if resultado is not None:
            print(f"Resultado: {resultado}")
    else:
        print("Operação não reconhecida.")


if __name__ == "__main__":
    main()
