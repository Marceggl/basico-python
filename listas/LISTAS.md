<h1 align="center">Listas em Python</h1>

## 📝 Conteúdo

- [Utilização de operadores básicos](#operadores_basicos)
- [Obter informações de hora](#info_horas)
- [Utilização e manipulação de listas](#listas)
- [Requisitos](#requisitos)

## 📖 Utilização e manipulação de listas <a name="listas"></a>

# Listas em Python

As listas em Python são estruturas de dados versáteis e poderosas que permitem armazenar e manipular coleções de elementos de forma eficiente. Aqui estão alguns conceitos fundamentais sobre listas:

## Criando uma Lista

Para criar uma lista, basta colocar os elementos entre colchetes, separados por vírgulas:

```python
minha_lista = [1, 2, 3, 4, 5]
```

## Acessando Elementos

Você pode acessar os elementos de uma lista usando índices. Lembre-se de que os índices em Python começam do zero:

```python
primeiro_elemento = minha_lista[0]
segundo_elemento = minha_lista[1]
```

## Modificando Elementos

As listas são mutáveis, o que significa que você pode modificar seus elementos:

```python
minha_lista[0] = 10
```

## Adicionando Elementos

Para adicionar elementos ao final de uma lista, você pode usar o método `append`:

```python
minha_lista.append(6)
```

## Removendo Elementos

Para remover um elemento com um valor específico, utilize o método `remove`:

```python
minha_lista.remove(4)
```

Se preferir remover o elemento com base no índice, use `pop`:

```python
elemento_removido = minha_lista.pop(2)
```

## Funções Úteis

Existem funções úteis para trabalhar com listas, como `len` para obter o comprimento da lista e `sorted` para ordenar os elementos:

```python
comprimento = len(minha_lista)
lista_ordenada = sorted(minha_lista)
```

Lembre-se, esses são apenas conceitos básicos. À medida que você avança, descobrirá mais recursos poderosos para manipulação de listas em Python. Experimente e divirta-se programando!

## ⚙️ Requisitos <a name = "requisitos"></a>

Não há requisitos no momento

