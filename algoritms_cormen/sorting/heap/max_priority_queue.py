class MaxPriorityQueue():


    def __init__(self, initial_array):
        self.heap = initial_array
        self.heap_size = len(initial_array)-1


    def _swap_index(self, a, b):
        tmp = self.heap[a]
        self.heap[a] = self.heap[b]
        self.heap[a] = tmp

    def right_node(self, i):
        return i*2 + 2

    def left_node(self, i):
        return i*2 + 1

    def parent(self, i):
        return (i-1)/2

    def max_heapify(self, i):

        max_index = i 

        while i <= self.heap_size:
            left = self.left_node(i)
            right = self.right_node(i)

            if left <= self.heap_size and self.heap[left] <= self.heap[i]:
                max_index = left

            if right <= self.heap_size and self.heap[right] <= self.heap[i]:
                max_index = right
        
            if max_index != i:
                self._swap_index(i, max_index)
                i = max_index
            else:
                break
        
    





