import logging

def validador_par_impar(x):
    if x % 2:
        logging.warning(msg="Seu número é impar")
    else:
        logging.warning(msg="Seu número é par")

def validador_de_numero(x):
    try:
        valor = int(x)
        validador_par_impar(valor)
    except ValueError:
        logging.error(msg=" Valor inválido, por favor coloque um valor inteiro !!!\n\n#########################################\n")
        main()

def main():
    
    print("### Válidar se é um número par ou impar ###\n")

    ### obtem um valor do usuário ###
    valor_informado = input("Digite um valor: ")

    ### Validar se é um numero par ou impar ###
    validador_de_numero(valor_informado)

if __name__ == "__main__":
    logging.basicConfig(encoding='utf-8', format='%(levelname)s:%(message)s', level=logging.DEBUG)
    main()