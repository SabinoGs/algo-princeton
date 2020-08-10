"""Max-heapify

Realiza a operação de "flutuar" o elemento em direção a posição correta da arvore, com o maior valor na raiz. 


Deve obedecer a propriedade de max-heap: 
    A[parent(i) >= A[i]]
"""

def left_node(indice):
    return 2*indice + 1

def right_node(indice):
    return 2*indice + 2

def parent(i):
    return int((i-1)/2)

def max_heapify(array, indice):

    # O heap_size é algo que deve ser definido por nós
    heap_size = len(array) - 1

    while indice < heap_size:
        
        left = left_node(indice)
        right = right_node(indice)
        largest = indice

        if left <= heap_size and array[left] > array[indice]:
            largest = left

        if right <= heap_size and array[right] > array[largest]:
            largest = right

        if largest != indice:
            tmp = array[indice]
            array[indice] = array[largest]
            array[largest] = tmp

            indice = largest
        else:
            break
        



if __name__ == "__main__":

    # 27 17 3 16 13 10 1 5 7 12 4 8 9 0
    
    array = list(map(int, input("Insira o array: ").split()))
    indice = int(input("Indique o indice para realizar o max-heapify: "))
    max_heapify(array, indice) 

    print(array)