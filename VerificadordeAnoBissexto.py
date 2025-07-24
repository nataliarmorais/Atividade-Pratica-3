# Solicita o ano ao usuário

ano = int(input("Digite um ano: "))

# Verificar se o ano é divisível por 4

if ano % 4 == 0 :
    
# Verificar se o ano é divisível por 100
    
    if ano % 100 != 0:
        print(f" O ano {ano} é bissexto.")
    
# Verificar se o ano é divisível por 400

    elif ano % 400 == 0:
        print(f"O ano {ano} é bissexto.")
    else:
        print(f"O ano {ano} não é bissexto.")
else:
        print(f"O ano {ano} não é bissexto.")

