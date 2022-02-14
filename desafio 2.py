registro = True
senha = str(input('digite a sua senha\n'))
if len(senha)<6:
    print(f"sua senha precisa de no mínimo mais {6-len(senha)} caracteres")
    registro = False
if senha.__contains__("#") or senha.__contains__("!") or senha.__contains__("@") or senha.__contains__("%") or senha.__contains__("$") or senha.__contains__("&") or  senha.__contains__("^") or senha.__contains__("*") or senha.__contains__("(") or  senha.__contains__(")") or senha.__contains__("+") or senha.__contains__("-"):
    pass
else:
    print('sua senha precisa de um caractere especial')
    registro = False
if senha.islower() == True:
    print('sua senha precisa ao menos de uma letra maiúscula')
    registro = False
if senha.isupper() == True:
    print('sua senha precisa ao menos de uma letra minúscula')
    registro = False
if registro == True:
    print("senha cadastrada com sucesso")
else:
    print("tente novamente")