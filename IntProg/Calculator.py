operation = 10
while operation != "0":
    print("Digite a operação que deseja")
    print("1 - adição")
    print ("2 - subtração")
    print ("3 - divisão")
    print ("4 - multiplicação")
    print ("0 - sair")
    operation = (input("Escolha a operação:"))
    if operation == "0":
        exit
    elif operation not in "1 2 3 4 0":
        print ("Operação não valida")
    else:
        n1 = float(input("1 Numero: "))
        n2 = float(input("2 Numero: "))
        if operation == "2":
            print ("Resultado: ", n1-n2)
        elif operation == "3":
            print ("Resultado: ", n1/n2)
        elif operation == "4":
            print ("Resultado: ", n1*n2)
        elif operation == "1":
            print ("Resultado: ", n1+n2)
print ("Fechando calculadora")