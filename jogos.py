import adivinhacao
import forca

print("********************")
print("***Escolha o jogo***")
print("********************")

print("(1) Adivinhação (2) Forca")

jogo = int(input("Qual jogo gostaria de jogar? "))

if(jogo == 1):
    print("Jogando Adivinhação")
    adivinhacao.jogar_adivinhacao()
elif(jogo == 2):
    print("Jogando Forca")
    forca.jogar_forca()