'''
ganha 500 + 6% do que vende. vendeu 12,398
vendas do mes lidas pela entrada
'''
sales = float(input("Qual valor das vendas:"))
salary = 500 + 6/100*sales
print("Salario:{:.2f} ".format(salary))