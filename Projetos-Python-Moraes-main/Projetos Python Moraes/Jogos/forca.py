def jogar_forca():
    print("------------------------------")
    print("\nBem vindo ao Jogo da Forca\n")
    print("------------------------------")

    palavra = "banana"
    perdeu = False
    acertou = False
    #enquanto nao acerta a palavra secreta o jogador não pode jogar

    while (not perdeu and not acertou):
        chute = remover_acentos(input("Digite uma letra: ")).strip()
        #index define a posição da letra na palavra
        index = 0
        for letra in palavra:
            if (chute.lower() == letra.lower()):
                print(f"A letra {chute} está na posição {index}!")
            index = index + 1


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
