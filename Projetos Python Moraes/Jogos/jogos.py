import adivinhacao
import forca

print("--------------------")
print("\nEscolha seu Jogo\n")
print("--------------------")

print("(1) Adivinhação (2) Forca")

opcao_jogo = int(input("Escolhe seu jogo:"))

if(opcao_jogo == 1):
    print("Escolhendo Adivinhação")
    adivinhacao.jogar_adivinhacao()
elif(opcao_jogo == 2):
    print("Escolhendo Forca")
    forca.jogar_forca()

