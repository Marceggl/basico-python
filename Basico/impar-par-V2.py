'''
 # @ Author: Marcel Barreto
 # @ Create Time: 2023-12-14 23:36:24
 # @ Modified by: Marcel Barreto
 # @ Modified time: 2023-12-15 00:39:18
 # @ Description: Válidar se um número é impar ou par de modo estruturado, mexido pelo chatGPT, resolvi tirar a biblioteca "logging" para não ser necessário importar nada
 '''

def validador_par_impar(x):
    if x % 2:
        print("Seu número é impar")
    else:
        print("Seu número é par")

def processar_numero(x):
    try:
        valor = int(x)
        validador_par_impar(valor)

    except ValueError:
        print("Valor inválido, por favor coloque um valor inteiro !!!\n\n#########################################\n")
        return False
    return True

def main():

    print("### Válidar se é um número par ou impar ###\n")

    ### Mantém o programa aberto até o usuário digitar um número ou dar [CTRL + C] ###
    while True:
        ### obtem um valor do usuário ###
        valor_informado = input("Digite um valor: ")

        ### Se o usuário digitar um número pare o loop ###
        if(processar_numero(valor_informado)):
            break

if __name__ == "__main__":
    main()


    