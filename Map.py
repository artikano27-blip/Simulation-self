from Entity import Grass,Rock,Tree
class Map:
    def __init__(self,map_width=40,map_height=30):
        self.map_width = map_width
        self.map_height = map_height
        #Словарь для хранения координат на Карте обьектов
        self.map_contain_entities = {}
#Функция добавления Обьекта на Карту обьектов
def add_entity_to_map(entity,entity_coordinate,core_map):
    if entity_coordinate not in core_map.map_contain_entities:
        core_map.map_contain_entities[entity_coordinate]=entity
        print (f"Обьект {entity} добавлен по координатам {entity_coordinate}")
        return True
    else:
        #Безопасно возвращаем булево для будущих конструкций с функцией.
        return False
#Получаем обьект по координатам из Карты обьектов
def get_entity_on_map(entity_coordinate,core_map):
    return f"Обьект по заданным координатам: {core_map.map_contain_entities.get(entity_coordinate)}"

test_map = Map()
grass = Grass(2,4)
rock = Rock(4,4)
tree = Tree(4,5)
tree_2 = Tree(4,5)

add_entity_to_map(grass,grass.entity_coordinates,test_map)
add_entity_to_map(rock,rock.entity_coordinates,test_map)
add_entity_to_map(tree,tree.entity_coordinates,test_map)
add_entity_to_map(tree,tree_2.entity_coordinates,test_map)
