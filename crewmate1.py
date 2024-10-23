import heap1
from treasure1 import Treasure

def max_heap(a, b):
    if a.priority_score() > b.priority_score() or (a.priority_score() == b.priority_score() and a.id < b.id):
        return True
    return False

class CrewMate:
    def __init__(self):
        self.priority_queue = heap1.Heap( max_heap, [])
        self.total_load = 0
        self.last_updated_time = 0
        self.history = [] 
        self.t = [] 
        self.prev_time=0

    def add_treasure(self, treasure, current_time):
        self.t.append(treasure)
        self.total_load += treasure.size
        self.update_last_time(current_time)

    def process_treasures(self,hp, current_time, prev_time,history):
        
        while hp.top() and prev_time<current_time:
            a = hp.extract()
            if prev_time + a.remaining_size <= current_time:
                prev_time += a.remaining_size
                a.completion_time = prev_time
                history.append(a)
            else:
                a.remaining_size -= (current_time - prev_time)
                prev_time = current_time
                hp.insert(a)

    def update_last_time(self, current_time):
        self.last_updated_time = current_time

    def get_completion_times(self):
        for treasure in self.t:
            self.process_treasures(self.priority_queue,treasure.arrival_time, self.prev_time,self.history)
            self.priority_queue.insert(treasure)
            self.prev_time=treasure.arrival_time

        treasures = []
        local_time = self.prev_time

        for treasure in self.priority_queue.heap:
            t = treasure.copy()
            t.completion_time = local_time + t.remaining_size
            local_time = t.completion_time
            treasures.append(t)

        self.t.clear()

        return self.history+treasures