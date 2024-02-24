'''
 # @ Author: Marcel Barreto
 # @ Create Time: 2023-12-14 23:12:00
 # @ Modified by: Marcel Barreto
 # @ Modified time: 2023-12-15 00:38:24
 # @ Description: Manipular data e hora com a biblioteca datetime
 '''

from datetime import datetime, timedelta

def main():

    hoje = datetime.now()                   ### Pega a data de hoje
    futuro = hoje + timedelta(days=2)       ### Calcula a variancia entre a data de hoje mais dois dias 
    
    print(f"Hoje é: {hoje.date()}, daqui dois dias será: {futuro.date()}")          ### Mostra na tela apenas as datas solicitadas e esquecendo a hora


if __name__ == "__main__":
    main()