x = float(input("Digite um valor: "))
operacao = input("Qual operação será realizada ? [+,-,*,/] ")
y = float(input("Digite outro valor: "))

if operacao == "+":
    resultado = x + y
elif operacao == "-":
    resultado = x - y
elif operacao == "/":
    # Evitar a divisão por zero
    if y != 0:
        resultado = x / y
    else:
        print("Erro: divisão por zero.")
        resultado = None
elif operacao == "*":
    resultado = x * y
else:
    print("Operação não reconhecida.")
    resultado = None

if resultado is not None:
    print(f"Resultado: {resultado}")
