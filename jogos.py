import adivinhacao
import forca

def escolha_jogo():
    print("********************")
    print("***Escolha o jogo***")
    print("********************")

    print("(1) Adivinhação (2) Forca")

    jogo = int(input("Qual jogo gostaria de jogar? "))

    if(jogo == 1):
        print("Jogando Adivinhação")
        adivinhacao.jogar()
    elif(jogo == 2):
        print("Jogando Forca")
        forca.jogar()

if(__name__ == "__main__"):
    escolha_jogo()