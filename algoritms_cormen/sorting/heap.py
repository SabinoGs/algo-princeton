from math import log2

def left_node(indice):
    return 2*indice + 1

def right_node(indice):
    return 2*indice + 2

def max_heapify(array, indice):

    heap_size = int(log2(len(array)))
    left = left_node(indice)
    right = right_node(indice)


    print(heap_size, left, right)
    print("Array antes: ", array)
    if left <= heap_size and array[left] > array[indice]:
        largest = left
    else:
        largest = indice

    if right <= heap_size and array[right] > array[largest]:
        largest = right

    if largest != indice:
        tmp = array[indice]
        array[indice] = array[largest]
        array[largest] = tmp
        max_heapify(array, largest)

    print("Array Depois: ", array)


if __name__ == "__main__":
    
    array = list(map(int, input("Insira o array: ").split()))
    indice = int(input("Indique o indice para realizar o max-heapify: "))
    max_heapify(array, indice) 