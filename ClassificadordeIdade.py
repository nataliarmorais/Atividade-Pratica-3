#Solicita a idade do usuário

idade = int(input("Digite a sua idade: "))

#Classifica a idade

if idade <=12:
    categoria= "Criança"
elif idade <=17:
    categoria = "Adolescente"
elif idade <=59:
    categoria = "Adulto"
else: 
    categoria = "Idoso"

print(f"Você é um(a) {categoria}")


