# Classificador de Cliente
idade = int(input("Digite a idade do cliente: "))
renda = float(input("Digite a renda mensal do cliente: R$ "))

if idade >= 35 and renda >= 12000:
    categoria = "Diamante"
elif idade >= 28 and renda >= 7000:
    categoria = "Ouro"
elif idade >= 20 and renda >= 3000:
    categoria = "Prata"
else:
    categoria = "Bronze"

print(f"Categoria do cliente: {categoria}")
