from datetime import date
print("Vamos verificar se o ano é bissexto! Digite o ano com 4 números. \nCaso queira verificar o ano atual basta digitar 0.")
ano = int(input("Digite o ano que deseja verificar: "))
if ano == 0:
    ano = date.today().year
if ano % 100 != 0 and ano % 4 == 0:
    print("O ano {} é Bissexto!".format(ano))
elif ano % 100 == 0 and ano % 400 == 0:
    print("O ano {} é Bissexto!".format(ano))
else:
    print("O ano não é Bissexto!".format(ano))
    