def jogar_forca():
    print("------------------------------")
    print("\nBem vindo ao Jogo da Forca\n")
    print("------------------------------")

    arquivo = open("Jogos/palavras.txt", "r")
    palavra = []

    for linha in palavra:
        linha = linha.strip()
        palavra.append(linha)

    arquivo.close()

    palavra_secreta = "banana".upper()
    letras_acertadas = ["_" for letra in palavra_secreta]
    #for letra in palavra:
        #letras_acertadas.append("_")
    perdeu = False
    acertou = False
    erros = 0
    #enquanto nao acerta a palavra secreta 
    #o jogador não pode jogar

    print("Você terá 6 tentativas. Boa sorte!")

    while (not perdeu and not acertou):
        chute = remover_acentos(input("Digite uma letra: "))
        chute = chute.strip().upper()
        #index define a posição da letra na palavra
        index = 0
        if(chute in palavra_secreta):
            for letra in palavra_secreta:
                if (chute.lower() == letra.lower()):
                    letras_acertadas[index] = letra
                index = index + 1
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
