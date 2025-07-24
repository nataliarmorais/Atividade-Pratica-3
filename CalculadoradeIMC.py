# Solicitar peso e altura do usuário

peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em metros: "))

# Calcular o IMC

imc= peso/(altura**2)

# Classificar o IMC

if imc<18.5:
    classificacao = "Abaixo do peso"
elif imc <25:
    classificacao = "Peso normal"
elif imc <30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obesidade"
    
print(f"Seu IMC é {imc:.2f} e você está classificado como: {classificacao}")

    