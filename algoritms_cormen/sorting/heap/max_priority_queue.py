import math

class MaxPriorityQueue():
    """
    Implementa uma fila de prioridade baseada na propriedade de max_heap.


    """

    def __init__(self, initial_array):
        self.heap = initial_array
        self.heap_size = len(initial_array)-1

        self._build_heap()

    def _swap_index(self, a, b):
        tmp = self.heap[a]
        self.heap[a] = self.heap[b]
        self.heap[b] = tmp

    def _right_node(self, i):
        return i*2 + 2

    def _left_node(self, i):
        return i*2 + 1

    def _parent(self, i):
        return int((i-1)/2)

    def _max_heapify(self, i):

        while i <= self.heap_size:
            left = self._left_node(i)
            right = self._right_node(i)

            if left <= self.heap_size and self.heap[left] > self.heap[i]:
                max_index = left
            else:
                max_index = i 

            if right <= self.heap_size and self.heap[right] > self.heap[max_index]:
                max_index = right
        
            if max_index != i:
                self._swap_index(i, max_index)
                i = max_index
            else:
                break

    def _build_heap(self):
        for i in range(int(self.heap_size/2), -1, -1):
            self._max_heapify(i)
    
    def maximum(self):
        return self.heap[0]

    def extract_max(self):
        """Remove e retorna  o elemento da heap com a maior Key
        """

        if self.heap_size < 0:
            raise ValueError("Heap underflow")

        max = self.heap[0]
        self.heap[0] = self.heap[self.heap_size]

        self.heap.pop(self.heap_size)
        self.heap_size -= 1
        # reorganiza a heap após a remoção do primeiro elemento
        self._max_heapify(0) 

        return max

    def increase_key(self, i, key):
        """Aumenta o index i com a nova key. 
        Assume que a key > heap[i]. 
        """

        if key < self.heap[i]:
            raise ValueError("Nova key é menor que a atual")

        self.heap[i] = key

        # Se não obedecer a propriedade de max_heap, 
        #   troque os elementos até que seja verdade.
        while i > 0 and self.heap[self._parent(i)] < self.heap[i]:
            self._swap_index(i, self._parent(i))
            i = self._parent(i)

    def insert(self, key):

        self.heap_size += 1

        
        
        # ao criar um nó novo, atribuir um valor "infinitamente pequeno"
        #   para poder realizar a movimentação desse novo valor para a posição
        #   correta na heap
        self.heap.append(-math.inf)

        # Mantem a propriedade de max_heap e "flutua" a nova key para o lugar certo.
        # Assumindo que a heap ja está num estado de max_heap
        self.increase_key(self.heap_size, key)


if __name__ == "__main__":
    
    array1 = [15, 13, 9, 5, 12, 8, 7, 4, 0, 6, 2, 1]

    queue = MaxPriorityQueue(array1)
    print("Max - Heap: ", queue.heap)
    print("Max element: ", queue.maximum())
    print("Pop first: ", queue.extract_max())
    print("Heap after pop: ", queue.heap)

    print("Max heap, after pop: ", queue.maximum())

    queue.increase_key(0, 15)
    print("Increase key 13 to 15: ", queue.heap)

    queue.insert(100)
    print("Insert 100 in heap: ", queue.heap)