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
        print( f"Обьект по заданным координатам: {core_map.map_contain_entities.get(entity_coordinate)}")
    #Удаляем обьект по координатам из Карты обьектов
    def remove_entity_from_map(self,entity_coordinate):
        self.map_contain_entities.pop(entity_coordinate)
        print("Успешно удален")



    test_map = Map()
    grass = Grass(2,4)
    rock = Rock(4,4)
    tree = Tree(4,5)
    tree_2 = Tree(4,5)

    add_entity_to_map(grass,grass.object_coordinates,test_map)
    add_entity_to_map(rock,rock.object_coordinates,test_map)
    add_entity_to_map(tree,tree.object_coordinates,test_map)
    add_entity_to_map(tree,tree_2.object_coordinates,test_map)
    remove_entity_from_map(tree.object_coordinates,test_map)
    get_entity_on_map(tree.object_coordinates,test_map)