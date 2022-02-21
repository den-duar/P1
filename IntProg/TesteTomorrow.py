n1 = -1
n2 = 1
cont = 0
fb = 0 
while cont < 7:
    fb = n1+n2
    n1 = n2
    n2 = fb
    cont = cont + 1

print (fb)