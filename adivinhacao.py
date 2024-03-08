import random
def jogar_adivinhacao():

    print("**********************************")
    print("Bem vindo no jogo de Adivinhação!")
    print("**********************************")

    tentativas = 0
    nivel = 0
    pontos = 1000
    numero_secreto = random.randrange(1, 101)

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    while nivel not in(1, 2, 3):
        nivel = int(input("Defina o nível:"))
        if nivel == 1:
            tentativas = 20
        elif nivel == 2:
            tentativas = 10
        elif nivel == 3:
            tentativas = 5
        else:
            print("Digite a dificuldade entre 1 e 3!")

    for rodada in range(1, tentativas + 1):
        print("Tentativa {} de {}".format(rodada, tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou", chute_str)
        chute = int(chute_str)

        if chute < 1 or chute > 100:
            print("Você deve digitar um número entre 1 e 100")
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if acertou:
            print("Você acertou e fez {}!".format(pontos))
            break
        else:
            if maior:
                print("Você errou! O seu chute foi maior do que o número secreto")
            elif menor:
                print("Você errou! O seu chute foi menor do que o número secreto")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos -= pontos_perdidos


    print("Fim do jogo")