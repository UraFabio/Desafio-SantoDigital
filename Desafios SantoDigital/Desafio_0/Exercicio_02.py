def menor_diferenca(array):
    array.sort() #Ordeno em ordem crescente o array, para o resultado sair em ordem crescente
    tamanho = len(array)
    pares = [] 
    menorDiferenca = 0 

    for i in range(tamanho-1):
        for j in range(i+1, tamanho):

            diferenca = abs(array[i] - array[j])

            if j == 1: 
                menorDiferenca = diferenca
                pares = [(array[j], array[i])]

            elif diferenca == menorDiferenca:
                pares.append((array[j], array[i]))  

            elif diferenca < menorDiferenca:
                menorDiferenca = diferenca
                pares = [(array[j], array[i])] 

    return pares
            

array = [3, 8, 50, 5, 1, 18, 12]
resultado = menor_diferenca(array) #Chamo a função e guardo o resultado do processamento na variavel
print(resultado)