import json

cadastro = {
  "nome": "João Silva",
  "idade": 30,
  "enderecos": [
    {
      "rua": "Rua Principal",
      "numero": 123
    },
    {
      "rua": "Rua Secundária",
      "numero": 456
    }
  ]
}

def ler_o_json():

    dados = cadastro

    #### Acessar um valor utilizando uma chave ###
    print("Usando chaves normal\n")
    print(dados["nome"])

    print("=========================")

    """
    O método get() é uma maneira mais segura de acessar um valor em um dicionário.

    Se a chave não existir no dicionário, o método get("chave", "Valor padrão") retornará None em vez de gerar um erro.
    """
    print("Método .get()\n")
    print(dados.get("Sobrenome", "Não informado"))

    print("=========================")


    ### Mostrar valores dentro de uma chave
    print("Iterando sobre os valores dentro de uma chave\n")
    for endereco in cadastro["enderecos"]:
        print(f"Rua {endereco['rua']}")
        print(f"numero {endereco['numero']}")

if __name__ == "__main__":
    ler_o_json()