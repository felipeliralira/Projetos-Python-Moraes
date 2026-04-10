import random as rd

def mensagem_boas_vindas():
    print("------------------------------")
    print("\nBem vindo ao Jogo da Forca\n")
    print("------------------------------")

def seleciona_palavra_aleatoria():
    arquivo = open("Jogos/palavras.txt", "r")
    palavra = []

    for linha in arquivo:
        linha = linha.strip()
        palavra.append(linha)

    arquivo.close()
    posicao = rd.randrange(0,len(palavra))

    palavra_secreta = palavra[posicao].upper()
    return palavra_secreta

def letras_corretas(palavra_secreta):
    return ["_" for letra in palavra_secreta]

def entrada_dados():
    chute = remover_acentos(input("Digite uma letra: "))
    chute = chute.strip().upper()
    return chute

def chute_correto(chute, palavra_secreta, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if (chute.lower() == letra.lower()):
            letras_acertadas[index] = letra
        index = index + 1
    return letras_acertadas

def jogar_forca():

    mensagem_boas_vindas()

    palavra_secreta = seleciona_palavra_aleatoria()
    letras_acertadas = letras_corretas(palavra_secreta)

    perdeu = False
    acertou = False
    erros = 0
    #enquanto nao acerta a palavra secreta 
    #o jogador não pode jogar


    print("Você terá 6 tentativas. Boa sorte!")
    print(" A palavra tem " + str(len(palavra_secreta)) + " letras.")
    while (not perdeu and not acertou):
        chute = entrada_dados()
        #index define a posição da letra na palavra
        
        if(chute in palavra_secreta):
            chute = chute_correto(chute, palavra_secreta, letras_acertadas)
        else:
            erros = erros + 1
            
        perdeu = erros == 6
        acertou = "_" not in letras_acertadas


        print(letras_acertadas)

#como resolver ocento nas palavras

def remover_acentos(palavra):
    palavra = palavra.replace("á", "a")
    palavra = palavra.replace("é", "e")
    palavra = palavra.replace("í", "i")
    palavra = palavra.replace("ó", "o")
    palavra = palavra.replace("ú", "u")
    return palavra


if __name__ == "__main__":
    jogar_forca()
