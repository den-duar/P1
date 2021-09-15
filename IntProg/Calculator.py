print("Digite a operação que deseja")
print("1 - adição")
print ("2 - subtração")
print ("3 - divisão")
print ("4 - multiplicação")
operation = (input("Escolha a operação:"))
n1 = float(input("1 Numero: "))
n2 = float(input("2 Numero: "))
if operation == "1":
    print (n1+n2)
elif operation == "2":
    print (n1-n2)
elif operation == "3":
    print (n1/n2)
elif operation == "4":
    print (n1*n2)