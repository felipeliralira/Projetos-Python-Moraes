import random as rd

def jogar_adivinhacao():
    print("-------------------------------------")
    print("\nBem vindo ao jogo de adivinhação!\n")
    print("-------------------------------------")

    # Definição das variaveis
    n_secreto = rd.randrange(1, 101)
    n_tentativas = 0
    rodada = 1
    pontos = 1000

    print("Níveis de dificuldade")
    print("\n(1)Easy (2) Medium (3) Dificil (4)Aleatório\n")

    nivel = int(input("Escolha um nível: "))

    if(nivel == 1):
        n_tentativas = 12

    elif(nivel == 2):
        n_tentativas = 8

    elif(nivel == 3):
        n_tentativas = 5
    else:
        n_tentativas = rd.randrange(1,12)



    for rodada in range(1, n_tentativas + 1):
        print(f"rodada {rodada}/{n_tentativas}")
        entrada = int(input("digite um valor aleatório entre 1 e 100: "))
        acerto = entrada == n_secreto
        chutemaior = entrada > n_secreto
        chutemenor = entrada < n_secreto

        if(entrada > 100 or entrada < 1):
            print("O valor digitado não é permitido")
            continue

        print(f"Você digitou o número: {entrada}")

        if(acerto):
            print("Parabéns, você acertou")
            print(f"Você terminou o jogo com {pontos} pontos!")
            break
        else:
            if(chutemaior):
                print("o número secreto é menor que seu chute")
            if(chutemenor):
                print("o número secreto é maior que seu chute")
        pontos_perdidos = abs(n_secreto - entrada)
        pontos = pontos - pontos_perdidos
        rodada = rodada + 1
    print("Fim de Jogo!")