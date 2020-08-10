class HeapSort():

    def __init__(self, array):
        self.array = array
        self.heap_size = len(array) - 1

    def left_node(self, indice):
        return 2*indice + 1

    def right_node(self, indice):
        return 2*indice + 2

    def parent(i):
        return int((i-1)/2)

    def _swap_index(self, a, b):
        tmp = self.array[a]
        self.array[a] = self.array[b]
        self.array[b] = tmp


    def max_heapify(self, indice):

        while indice < self.heap_size: # Remove a necessidade de recursão
            
            left = self.left_node(indice)
            right = self.right_node(indice)
            largest = indice

            if left <= self.heap_size and self.array[left] > self.array[indice]:
                largest = left

            if right <= self.heap_size and self.array[right] > self.array[largest]:
                largest = right

            if largest != indice:
                tmp = self.array[indice]
                self.array[indice] = self.array[largest]
                self.array[largest] = tmp

                indice = largest
            else:
                break

    def build_heap(self):
        # Essa operação não garante um array ordenado em ordem decrescente
        # Lembrando da propriedade de max-heap: a[parent(i)] > a[i].
        # Isso não significa que está ordenado. Como por exemplo, a árvore a seguir:
        #   8
        #  2 4  <--- Não fere a propriedade de max-heap, mas não está ordenado.
        for i in range(int(self.heap_size/2), -1, -1):
            self.max_heapify(i)

    def heap_sort(self):
        
        self.build_heap()
        for i in range(len(array)-1, 0, -1):
            self._swap_index(0,i)

            # Remove um do tamanho da heap pq o ultimo elemento ja está no lugar 
            # que deveria estar. Portanto não precisa ser movido.
            self.heap_size -= 1 
            self.max_heapify(0)


if __name__ == "__main__":

    # 5 13 2 25 7 17 20 8 4
    
    array = list(map(int, input("Array: ").split()))
    print(array)

    heap_sort = HeapSort(array)
    heap_sort.heap_sort()

    print(heap_sort.array)