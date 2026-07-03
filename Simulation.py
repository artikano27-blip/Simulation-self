from Creature import Creature
from Map import Map
class Simulation:
    def __init__(self):
        pass
    def update_all_entities(self,core_map: Map):
        creatures_ready_to_moved_on = []
        for entity_coordinate, entity in core_map.map_contain_entities.items():
            if isinstance(entity,Creature):
              creatures_ready_to_moved_on.append(entity)
        for creature in creatures_ready_to_moved_on:
            creature.make_turn(core_map)

    def run_loop_simulation(self,core_map):
        running = True
        while running:
            self.update_all_entities(core_map)
