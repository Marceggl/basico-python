<h1 align="center">dicionarios em Python</h1>

**O que são?**

Dicionários em Python são estruturas de dados que armazenam dados em pares chave-valor.

**Como funcionam?**

- As chaves são strings que identificam os valores.
- Os valores podem ser qualquer tipo de dado Python, como strings, números, listas, dicionários ou outros tipos de objetos.

**Analogia:**

Imagine um dicionário de palavras. As palavras são as chaves e as definições são os valores.

**Criação:**

```python
meu_dicionario = {"nome": "João Silva", "idade": 30}
```

Neste exemplo, "nome" e "idade" são as chaves e "João Silva" e 30 são os valores.

**Acessando valores:**

```python
nome = meu_dicionario["nome"]
idade = meu_dicionario["idade"]
```

**Benefícios:**

- Armazenam dados de forma organizada e eficiente.
- Permitem acesso rápido aos dados usando as chaves.
- São muito utilizados em diversos programas Python.

**Exemplo de uso:**

```python
agenda = {
  "João Silva": {"telefone": "1234-5678", "email": "joaosilva@email.com"},
  "Maria Oliveira": {"telefone": "9876-5432", "email": "mariaoliveira@email.com"}
}

# Acessando o telefone de Maria Oliveira
telefone_maria = agenda["Maria Oliveira"]["telefone"]

print(f"Telefone de Maria Oliveira: {telefone_maria}")
```

**Recursos adicionais:**

- Tutoriais sobre dicionários em Python: [https://www.w3schools.com/python/python_dictionaries.asp](https://www.w3schools.com/python/python_dictionaries.asp)

[Voltar pra cima](#📝-conteúdo)
