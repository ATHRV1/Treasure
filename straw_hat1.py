import crewmate1
import heap1
from treasure1 import Treasure

class StrawHatTreasury:
    def __init__(self, m):
        self.crewmates = [crewmate1.CrewMate() for _ in range(m)]
        self.min_heap = heap1.Heap(lambda a, b: a.total_load < b.total_load, self.crewmates)

    def add_treasure(self, treasure):
        current_time = treasure.arrival_time

        best_crewmate = self.min_heap.extract_1(treasure.arrival_time)
        best_crewmate.total_load=max(0,(best_crewmate.total_load-(current_time-best_crewmate.last_updated_time)))
        best_crewmate.add_treasure(treasure, current_time)
        
        self.min_heap.insert_1(best_crewmate,treasure.arrival_time)

    def get_completion_time(self):
        treasures = []

        for crewmate in self.crewmates:
            treasures += crewmate.get_completion_times()

        treasures.sort(key=lambda t: t.id)
        return treasures


# Test with treasures
treasury = StrawHatTreasury(3)
treasure1 = Treasure(1, 60, 1)  
treasure2 = Treasure(2, 20, 2)  
treasure3 = Treasure(3, 60, 3) 
treasure4 = Treasure(4, 10, 4)
treasure5 = Treasure(5, 30, 5)
treasure6 = Treasure(6, 80, 6)
treasure7 = Treasure(7, 20, 7)
treasure8 = Treasure(8, 90, 8)

treasury.add_treasure(treasure1)
treasury.add_treasure(treasure2)
treasury.add_treasure(treasure3)
treasury.add_treasure(treasure4)
treasury.add_treasure(treasure5)
treasury.add_treasure(treasure6)
treasury.add_treasure(treasure7)
treasury.add_treasure(treasure8)

completion_times = treasury.get_completion_time()

for t in completion_times:
    print(f"Treasure {t.id}: completion_time={t.completion_time}")