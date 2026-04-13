from datetime import date

ano_atual = date.today().year

nome = input("Qual é o seu nome?")
idade = input("Qual ano você nasceu?" )
valor_idade = ano_atual + idade
print(f"Olá {nome} sua idade é {valor_idade}")
