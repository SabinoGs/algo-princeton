"""Min-heapify

Realiza a operação contrária do max-heapify, deixando o elemento
com menor valor na raiz. Utilizado para implementações de fila prioritária e ordenações
decrescentes.

Deve obedecer a propriedade de min-heap: 
    A[parent(i) <= A[i]]
"""

def left(i):
    return 2*i + 1

def right(i):
    return 2*i + 2

def parent(i):
    return int((i-1)/2)


def min_heapify(array, indice):
    heap_size = len(array) - 1

    # While-loop evita uma recursão
    while indice < heap_size:
        left_node = left(indice)
        right_node = right(indice)

        if left_node <= heap_size and array[left_node] < array[indice]:
            small = left_node

        if right_node <= heap_size and array[right_node] < array[indice]:
            small = right_node

        if small != indice:
            tmp = array[indice]
            array[indice] = array[small]
            array[small] = tmp
            indice = small
        else:
            break


if __name__ == "__main__":

    # 27 17 3 16 13 10 1 5 7 12 4 8 9 0
    
    array = list(map(int, input("Insira o array: ").split()))
    indice = int(input("Indique o indice para realizar o max-heapify: "))
    min_heapify(array, indice)


    print(array)