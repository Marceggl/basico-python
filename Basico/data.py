from datetime import datetime, timedelta

def main():

    hoje = datetime.now()                   ### Pega a data de hoje
    futuro = hoje + timedelta(days=2)       ### Calcula a variancia entre a data de hoje mais dois dias 
    
    print(f"Hoje é: {hoje.date()}, daqui dois dias será: {futuro.date()}")          ### Mostra na tela apenas as datas solicitadas e esquecendo a hora


if __name__ == "__main__":
    main()