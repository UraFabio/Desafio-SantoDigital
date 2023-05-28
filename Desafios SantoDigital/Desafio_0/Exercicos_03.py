def encontrar_subconjuntos(conjunto):
    subconjuntos = [[]]  # Inicializo o subconjunto como vazio

    for num in conjunto:
        subconjuntos += [subset + [num] for subset in subconjuntos] # A cada iteração estou gerando um novo subconjunto adicionado o 'num' a todo subconjunto já esxistente

    subconjuntos.sort(key=len)  # Ordena os subconjuntos com base no tamanho para facilitar a leitura

    return subconjuntos

conjunto = [1,2,3,4]

resultado = encontrar_subconjuntos(conjunto)
print(resultado)