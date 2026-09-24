#Sistema de Autenticação
senha = "1234"
tentativas = 0
acesso = False

while tentativas < 3:
    senha = input("Digite a senha: ")

    if senha == senha:
        acesso = True
        print("Acesso liberado!")
        break
    else:
        tentativas += 1
        print(f"Senha incorreta. Tentativa {tentativas} de 3.")

if not acesso:
    print("Acesso bloqueado. Número máximo de tentativas atingido.")