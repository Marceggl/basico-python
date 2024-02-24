import random

def main():

    notas = []
    
    i = 0

    while i < 10:
        notas.append(random.randint(0, 10))
        i += 1

    print(f"Todas as notas: {notas}")
    print(f"A nota no indice 2 é: {notas[2]}")


if __name__ == "__main__":
    main()