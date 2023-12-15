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


    