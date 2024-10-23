class Treasure:
    
    def __init__(self, id, size, arrival_time):
        
        self.id = id
        self.size = size
        self.arrival_time = arrival_time
        self.completion_time = None
        self.remaining_size = size 
    
    def priority_score(self):
        score = 0-self.remaining_size-self.arrival_time
        return score


    def process(self, units=1):
        self.remaining_size -= units
        if self.remaining_size <= 0:
            return False 
        return True 
    
    def copy(self):
        new_treasure = Treasure(self.id, self.size, self.arrival_time)
        new_treasure.completion_time = self.completion_time
        new_treasure.remaining_size = self.remaining_size
        return new_treasure