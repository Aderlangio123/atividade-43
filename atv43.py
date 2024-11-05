# Utilizando listas faça um programa que faça 5 perguntas para uma
# pessoa sobre um crime. As perguntas são:
#  "Telefonou para a vítima?"
#  "Esteve no local do crime?"
#  "Mora perto da vítima?"
#  “Tinha dívidas com a vítima?"
#  "Já trabalhou com a vítima?“
# O programa deve no final emitir uma classificação sobre a
# participação da pessoa no crime. Se a pessoa responder
# positivamente a 2 questões ela deve ser classificada como
#"Suspeita“; entre 3 e 4 como "Cúmplice" e; 5 como "Assassino".
#caso contrario sera classificada como inocente

respostas = []
palavra = "sim"

print("responda as perguntas a seguir com Sim ou Não!   ")
print(" ")
pergunta_1 = str(input("Telefonou para a vítima?:  ")).strip().lower()
respostas.append(pergunta_1)
pergunta_2 = str(input("Esteve no local do crime?:  ")).strip().lower()
respostas.append(pergunta_2)
pergunta_3 = str(input("Mora perto da vítima?:  ")).strip().lower()
respostas.append(pergunta_3)
pergunta_4 = str(input("Tinha dívidas com a vítima:  ")).strip().lower()
respostas.append(pergunta_4)
pergunta_5 = str(input("Já trabalhou com a vítima?: ")).strip().lower()
respostas.append(pergunta_5)

quantidade = respostas.count(palavra)
if quantidade == 2:
    print("a classificação dessa pessoa é:  Suspeita!")
elif quantidade > 2 and quantidade < 5:
    print("a classificação dessa pessoa é:  Cúmplice")
elif quantidade == 5:
     print("a classificação dessa pessoa é:  Assasino!")
elif quantidade < 2:
    print("a classificação dessa pessoa é:  Inocente")