def get_load(a, t):
    return max(0, a.total_load - (t - a.last_updated_time))

class Heap:
    
    def __init__(self, comparison_function, init_array):
        
        self.heap = []
        self.comparator = comparison_function
        if init_array:
            self.heap = init_array.copy()
            for i in range(len(self.heap) - 1, -1, -1):
                self._shift_down(i)

    def _shift_up(self, i):
        parent = (i - 1) // 2
        while i != 0 and self.comparator(self.heap[i], self.heap[parent]):
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent
            parent = (i - 1) // 2

    def _shift_down(self, i):
        left = 2 * i + 1
        right = 2 * i + 2
        while (left < len(self.heap) and self.comparator(self.heap[left], self.heap[i])) or (right < len(self.heap) and self.comparator(self.heap[right], self.heap[i])):
            largest = left if (right >= len(self.heap) or self.comparator(self.heap[left], self.heap[right])) else right
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            i = largest
            left = 2 * i + 1
            right = 2 * i + 2

    def insert(self, value):
        self.heap.append(value)
        self._shift_up(len(self.heap) - 1)
    
    def extract(self):
        
        if not self.heap:
            return None
        top = self.heap[0]
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.heap.pop()
        self._shift_down(0)
        return top
    
    def top(self):
        
        return self.heap[0] if self.heap else None

    def is_empty(self):
        return len(self.heap) == 0
    
    def extract_1(self, t):
        if len(self.heap) == 0:
            return None
        val = self.heap[0]
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.heap.pop()
        i = 0
        left = 2 * i + 1
        right = 2 * i + 2
        while (left < len(self.heap) and get_load(self.heap[left], t) < get_load(self.heap[i], t)) or (
                right < len(self.heap) and get_load(self.heap[right], t) < get_load(self.heap[i], t)):
            t = left if (right >= len(self.heap) or get_load(self.heap[left], t) < get_load(self.heap[right], t)) else right
            self.heap[i], self.heap[t] = self.heap[t], self.heap[i]
            i = t
            left = 2 * i + 1
            right = 2 * i + 2
        return val
   
    def insert_1(self, a, t):
        self.heap.append(a)
        i = len(self.heap) - 1
        parent = (i - 1) // 2
        while i != 0 and get_load(self.heap[parent], t) > get_load(self.heap[i], t):
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent
            parent = (i - 1) // 2
