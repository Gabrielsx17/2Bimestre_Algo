#Tuplas são imutáveis, para manipular deve se usar a indexação e slicing, podem ser unidas por concatenação

numero = (5, 8, 12, 8, 7, 8, 3)
print(f"Tupla original: {numero}")

print(len(numero)) #Len é a cardinalidade da tupla
print((numero[2]))
print(f"Slicing do 2 ao 5 {numero[2:6]}")
print(f"Quantas vezes o número 8 repete: {numero.count(8)}")

min_tupla=min(numero)
max_tupla=max(numero)
soma_tupla=sum(numero)
tupla_org=sorted(numero)
print(min_tupla, max_tupla, soma_tupla)
print(tupla_org[2])
print("O número 4 está na tupla?", 3 in numero)

numero2 = (15, 20)
tupla_dobro_numero= numero*2
tupla_concatenada=numero+numero2
print(f"Ambas as tuplas concatenadas: {tupla_concatenada}")
print(tupla_dobro_numero)