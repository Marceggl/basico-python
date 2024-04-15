"""
 # @ Author: Marcel Barreto
 # @ Create Time: 2023-12-15 16:35:05
 # @ Modified by: Marcel Barreto
 # @ Modified time: 2023-12-15 16:49:32
 # @ Description: Programa para realizar o calculo da média de um aluno
 """


def status_aluno(MEDIA):
    status = ""

    if MEDIA >= 7:
        status = "Aprovado"
    else:
        status = "Reprovado"

    return status


def main():
    print("### Criador de média de notas ###")
    notas = []
    i = 1

    while len(notas) < 4:
        try:
            notas.append(float(input(f"Insira a nota {i} do Aluno: ")))
            i += 1
        except:
            print("Por favor, insira um valor válido !!!")

    nota_max = max(notas)
    nota_min = min(notas)
    media = sum(notas) / len(notas)

    print(
        f"Este aluno foi {status_aluno(media)} com média: {media:.2f}.\nSendo que:\n  - A menor nota é: {nota_min}\n  - A maior nota é: {nota_max}\n"
    )


if __name__ == "__main__":
    main()
