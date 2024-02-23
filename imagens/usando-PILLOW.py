from PIL import Image

def abrir_imagem(imagem):

    img = Image.open(imagem)

    ### Mostrara as informacoes basicas da imagem ###
    """
    #   format - identifica o tipo da  imagem
    #   mode - Escala de cinza, RGB, CMYK
    #   size - dimensão da imagem
    """ 

    print(f"Formato da imagem: {img.format}\nDimensões da imagem: {img.size}\nModo: {img.mode}")

    img.show()


if __name__ == "__main__":

    caminho_imagem = "imgs/foto-lua.jpg"
    abrir_imagem(caminho_imagem)