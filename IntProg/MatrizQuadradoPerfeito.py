#Linguagem:Python
def matrizQuadradoMagico(matriz):
    somadiagonalp = 0
    somadiagonalsec = 0
    somalinhaanterior = 0
    somacolunaanterior = 0
    for i in range(len(matriz)):
        somalinha = 0
        somacoluna = 0
        somadiagonalp+=int(matriz[i][i])
        somadiagonalsec+=int(matriz[i][len(matriz)-i-1])
        for j in range(len(matriz)):
            somalinha+=int(matriz[i][j])
            somacoluna+=int(matriz[j][i])
        if(somalinhaanterior == 0 and somacolunaanterior == 0):
            somalinhaanterior = somalinha
            somacolunaanterior = somacoluna
        elif (somalinhaanterior != somalinha or somacolunaanterior != somacoluna):
            return False
    if(somadiagonalp != somadiagonalsec):
        print(somadiagonalp)
        print(somadiagonalsec)
        return False
    return True



matrizA = [[1,1,1],[1,1,1],[1,1,1]]
matrizB = [[5,12,7],[10,8,6],[9,4,11]]
matrizC = [[1,2],[1,2]]
matrizD = [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]
print(matrizQuadradoMagico(matrizA))
print(matrizQuadradoMagico(matrizB))
print(matrizQuadradoMagico(matrizC))
print(matrizQuadradoMagico(matrizD))