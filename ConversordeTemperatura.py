#Solicita a temperatura, a unidade de origem e a unidade de destino
temperatura = float(input("Digite a temperatura: "))
unidade_origem = input("Digite a unidade de origem (C para Celsius, F para Fahrenheit, K para Kelvin): ").lower()
unidade_destino = input("Digite a unidade de destino (C para Celsius, F para Fahrenheit, K para Kelvin): ").lower()

resultado = None

#Conversão de Temperatura

if unidade_origem == "c" :
    if unidade_destino == "f":
        resultado = (temperatura * 9/5) + 32
    elif unidade_destino == "k":
        resultado= temperatura + 273.15
    else:
        resultado = temperatura
elif unidade_origem == "fahrenheit":
    if unidade_destino == "celsius":
        resultado = (temperatura - 32) * 5/9
    elif unidade_destino == "kelvin":
        resultado = (temperatura - 32) * 5/9 + 273.15
    else: 
        resultado = temperatura
else:
    print("Unidade de origem inválida!")
    resultad0 = None         
   
if resultado is not None:
    print(f"A temperatura convertida é: {resultado:.2f} {unidade_destino.capitalize()}")