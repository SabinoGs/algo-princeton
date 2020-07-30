def insertion_sort(arr):
    """Realiza a ordenação dos elementos do array in-place.

    Compara os elementos um a um e troca as posições dos menores para a esquerda,
    enquanto os elementos maiores ficam a direita.
    """

    tamanho = len(arr)

    # É realizado uma iteração do segundo elemento até o ultimo
    # Começa do Segundo elemento, pois esse algoritmo compara
    #   o elemento da esquerda com o da direita. Sendo assim,
    #   se começasse do elemento 0, teríamos que buscar o elemento -1 e
    #   "não é possivel" (Em python seria o ultimo elemento, caracteristica da linguagem)
    for i in range(1, tamanho):

        # Elemento que será comparado
        # Essa chave muda a cada for-loop
        key = arr[i]

        print("Chave: ", key)

        # Para pegar o elemento a esquerda da chave
        j = i - 1

        # j >= 0 para evitar tentar colocar um elemento numa posição que não existe
        # arr[j] > key é realizado a comparação se o elemento a esquerda
        #   é maior que o da direita. Enquanto for, faça a sequência de comandos a seguir

        print(" (ANTES) -->", arr)
        while j >= 0 and arr[j] > key:
            print("J: ", j, " Array[j]: ", arr[j])

            # Dá um passo pro lado direito. Já que o arr[j] é maior
            arr[j + 1] = arr[j]
            print(" (DURANTE) -->", arr)

            # Esse ajuste no index J quer dizer
            #  que vamos olhar os elementos anteriores
            #  e realizar a comparação com a Key novamente.
            # Isso será feito até que achamos o lugar mais a direita possível para a key.
            #
            j = j - 1

        # Devolvo um lugar novo para a key mais a direita possivel
        arr[j + 1] = key
        print(" (DEPOIS) -->", arr)


if __name__ == "__main__":

    arr = [80, 10, 3, 1, 2, 5, 81]
    insertion_sort(arr)
    print(arr)
