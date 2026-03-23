lista = [1,2,3,4,5,6]
frutas = ['laranja', 'maçã', 'pera', 'banana', 'kiwi', 'banana']

#s[i] 
#ith item of s, origin 0 
#(3)(8)

print(frutas[1])
#Retorna Maçã
print(lista[3])
#Retorna 4
#Retorna O item da lista que está nessa posição
#-----------------------------------------------

#s + t
#the concatenation of s and t
#(6)(7)
print(frutas + lista)
# Junta as 2 lista
#-----------------------------

#s * n or n * s
#equivalent to adding s to itself n times
#(2)(7)
s = [2, 7]
n = 3

resultado = s * n
# Ou n * s (a ordem não importa)
print(resultado) 
# Saída: [2, 7, 2, 7, 2, 7]
#--------------------------------

#s[i:j]
#slice of s from i to j
#(3)(4)

numeros = [10,20,30,40,50]

fatia = numeros[1:4]

print(fatia)

#Basicamente vai contar do primeiro numero pra frente e o segunndo numero que é o J irá ser cortado, não vai contar ele.





