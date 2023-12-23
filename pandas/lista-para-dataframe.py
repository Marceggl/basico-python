"""
 # @ Author: Marcel Barreto
 # @ Create Time: 2023-12-21 19:59:47
 # @ Modified by: Marcel Barreto
 # @ Modified time: 2023-12-21 20:02:38
 # @ Description: Transformar uma lista em um data Frame Pandas
 """
### Importa a biblioteca pandas para manipulação de dados
import pandas as pd

### Importa o tipo List do módulo typing para uso na assinatura da função
from typing import List

"""
1 - Esta função recebe uma lista de listas de inteiros como argumento e Retornará um objeto DataFrame do pandas.
2 - Os rótulos das colunas do DataFrame são definidos como "Coluna 1" e "Coluna 2".
"""


def criar_um_dataFrame(dados: List[List[int]]) -> pd.DataFrame:
    df = pd.DataFrame(dados, columns=["Coluna 1", "Coluna 2"])

    return df


"""
Inicia a execução do código a partir deste ponto.
"""
if __name__ == "__main__":
    data = [[1, 15], [2, 11], [3, 11], [4, 20]]

    data_frame = criar_um_dataFrame(data)

    print(data_frame)
