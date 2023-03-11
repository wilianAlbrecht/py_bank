import os

while True:

    os.system("cls")

    print("Bem vindo. ")
    print("1- Logar ")
    print("2- criar conta ")
    print("0 - sair ")
    
    try:
        op = int(input(""))

        if op == 1:
            ...
        elif op == 2:
            ...
        elif op == 0:
            ...
        elif op > 2:
            raise TypeError("Digite um numero valido.")



    except ValueError as err:
        os.system("cls")
        input("Digite apenas um digito")
    except TypeError as err:
        os.system("cls")
        input(err)
