#Análise de 5 Números
soma = 0
maior = None
menor = None

for contador in range(1, 6):
    numero = float(input(f"Digite o {contador}º número: "))

    soma += numero

    if maior is None or numero > maior:
        maior = numero

    if menor is None or numero < menor:
        menor = numero

media = soma / 5

print(f"Soma: {soma}")
print(f"Média: {media:.2f}")
print(f"Maior número: {maior}")
print(f"Menor número: {menor}")