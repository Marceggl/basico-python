'''
 # @ Author: Marcel Barreto
 # @ Create Time: 2024-02-05 17:23:51
 # @ Modified by: Marcel Barreto
 # @ Modified time: 2024-02-23 21:20:29
 # @ Description: Realiza a extração de várias pastas zipadas de uma vez
 '''



import os
import zipfile

def extrair_pastas_zip(diretorio_origem, diretorio_destino):
    # Verifica se o diretório de destino existe, se não, cria
    if not os.path.exists(diretorio_destino):
        os.makedirs(diretorio_destino)

    # Lista todos os arquivos no diretório de origem
    arquivos_zip = [f for f in os.listdir(diretorio_origem) if f.endswith('.zip')]

    # Loop para extrair cada arquivo zip
    for arquivo_zip in arquivos_zip:
        caminho_completo = os.path.join(diretorio_origem, arquivo_zip)

        # Cria um objeto ZipFile e extrai o conteúdo
        with zipfile.ZipFile(caminho_completo, 'r') as zip_ref:
            zip_ref.extractall(diretorio_destino)

        print(f'Pasta extraída: {arquivo_zip}')

if __name__ == "__main__":
    # Substitua 'caminho/do/diretorio' pelo caminho completo do seu diretório de download
    diretorio_origem = r"caminho/do/diretorio"
    
    # Substitua 'caminho/do/diretorio/extraido' pelo caminho completo do diretório onde deseja extrair os arquivos
    diretorio_destino = r"caminho/de/destino"

    extrair_pastas_zip(diretorio_origem, diretorio_destino)
