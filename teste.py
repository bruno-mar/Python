# ESSE É MEU PRIMEIRO PROJETO PYTHON, SISTEMA DE PERGUNTAS E RESPOSTAS, MOSTRANDO SE ESTÁ CORRETA OU INCORRETA, E AO FINAL MOSTRANDO SUA NOTA.
print("Seja muito bem vindo ao quiz!")
answer_user = input("Quer começar? (S/N) ")

if answer_user != "S":
    quit()

score = 0


print("Começando...")
print("Quem desenvolveu o jogo Grand Theft Auto (GTA)? \n (A) Rockstar Games \n (B) Ubisoft \n (C) Activision \n (D) EA \n")
answer_1 = input("Resposta: ")

if answer_1 == "A":
    print("Correto!")
    score = score + 1

else:
    print("Incorreto")
    
print("Qual o protagonista do GTA San Andreas? \n (A) Carlos John \n (B) Carl jonhson \n (C) Carlos Jonhson \n (D) Carl jaqueline \n")
answer_2 = input("Resposta: ")

if answer_2 == "B":
    print("Correto!")
    score = score + 1

else:
    print("Incorreto")

print(f"Quiz acabou....Pontuação: {score}/2")    
