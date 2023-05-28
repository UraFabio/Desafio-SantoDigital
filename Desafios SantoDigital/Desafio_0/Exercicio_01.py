def gerar_lista_de_asteriscos(n):
    lista_de_asteriscos = [] 
    for i in range(1,n+1):
        lista_de_asteriscos.append('*'*i) #A cada iteração adiciono à lista_de_asteriscos uma string contendo o numero de asteriscos igual ao valor de i na iteração, que começa com 1 e vai até o numero digitado pelo usuário
    return lista_de_asteriscos

numero = int(input("Digite um numero inteiro: ")) 

lista_de_asteriscos = gerar_lista_de_asteriscos(numero) #Chamo a função 'gerar_lista_asteriscos' e guardo o valor retornado por ela na variável 'lista_de_asteriscos'

print(lista_de_asteriscos) 