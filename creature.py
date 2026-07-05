from entity import Entity,Grass,Tree,Rock
from map import Map
from collections import deque


#Класс Существо, наслудуемся для удобства от Entity,дополняем нужными параметрами
class Creature(Entity):
    def __init__(self,creature_health,creature_speed,x,y):
        super().__init__(x,y)
        self.creature_health = creature_health
        self.creature_speed = creature_speed
        #Важный индикатор цели для преследования. Нужен для работы дальнейших функций
        self.food_class = None
    #Создаем одну из основных функций перемещения обьекта,ссылаемся на :Map для удобства
    def make_move(self,new_coordinate,core_map: Map):
        #Делаем барьер для будущих обьектов, чтобы не выходили за границы карты
        get_object = core_map.map_contain_entities.get(new_coordinate)
        current_coordinates = (self.object_coordinates)
        x,y = new_coordinate
        if x < 0 or y < 0 or x>= core_map.map_width or y>=core_map.map_height:
            return current_coordinates
        #Проверяем занята ли координата на карте обьектов
        else:
            if new_coordinate not in core_map.map_contain_entities or isinstance(get_object,self.food_class):
                core_map.map_contain_entities[new_coordinate]=self
                #Не забываем поменять значение так же в самом обьекте, а после подчистить хвосты
                self.object_coordinates = new_coordinate
                core_map.map_contain_entities.pop(current_coordinates)
                return True
            else:
                return False
    #Функция локатора для обьекта, ищет обьекту соотвествующую ему пищу для дальнейших операций
    def find_food_on_map(self,core_map: Map):
        #Заводим словарь для отбора всех претендентов на поедание
        food_contenders = {}
        min_contender = float("inf")
        #Выводим None если еды не осталось или нет на карте, для дальнейшей обработки
        closest_coordinate = None
        #Пробегаемся по словарю Обьектов и заносим в локальный словарь для операций
        for object_coordinate,object in core_map.map_contain_entities.items():
            if isinstance(object,self.food_class):
                food_contenders[object_coordinate] = object
        #С помощью манхеттенхской формулы ищем кратчайщий путь среди всей нужной еды на карте Обьектов
        for contender_coordinate,contender in food_contenders.items():
            x1,y1 = self.object_coordinates
            x2,y2 = contender_coordinate
            step_result = abs(x2-x1)+abs(y2-y1)
            #Находим минимальный кратчайший путь
            if step_result < min_contender:
                min_contender = step_result
                closest_coordinate = contender_coordinate
        #Возращаем координаты для дальнейшей обработки
        return closest_coordinate
    #Функция движения обьекта к ближайшей пище
    def find_path(self, start_pos, target_pos, core_map):
        queue = deque([start_pos])
        visited = {start_pos}
        came_from = {start_pos: None}

        # 1. Поиск пути
        found = False
        while queue:
            current_pos = queue.popleft()
            if current_pos == target_pos:
                found = True
                break

            x, y = current_pos
            for neighbor in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                # Проверяем границы карты и проходимость
                if (0 <= neighbor[0] < core_map.map_width and
                        0 <= neighbor[1] < core_map.map_height):

                    step_object = core_map.map_contain_entities.get(neighbor)
                    # Можно идти в пустоту или на еду
                    if (step_object is None or isinstance(step_object, self.food_class)) and neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
                        came_from[neighbor] = current_pos

        # 2. Восстановление пути
        if not found:
            return None

        path = []
        current = target_pos
        while current != start_pos:
            path.append(current)
            current = came_from[current]

        path.reverse()  # Разворачиваем, чтобы путь шел от волка к еде
        return path


    # Функия сделай ход, обьединяет все наработки в одну функцию
    def make_turn(self,core_map:Map):
        #Логика потери здоровья пассивно(старение)
            self.creature_health-=3
            #Проверяем хп
            if self.creature_health <= 0:
                core_map.remove_entity_from_map(self.object_coordinates)
                return False  # Останавливаем ход, в свзяи со смертью

            #Запускаем локатор еды если существо живо
            coords = self.find_food_on_map(core_map)

            #Если еда есть на карте выполняем движение к еде
            if coords != None:
                self.calculate_next_step(coords,core_map)
                #Дошли до еды хаваем
                if self.object_coordinates==coords:
                    self.creature_health +=20 #Отжор хп со сьеденной пищи
                return True
            #Если еды не нашли
            return False

class Predator(Creature):
    def __init__(self,creature_health,creature_speed,damage,x,y):
        super().__init__(creature_health,creature_speed,x,y)
        self.damage = damage
        self.food_class = Herbivore

class Herbivore(Creature):
    def __init__(self,creature_health,creature_speed,x,y):
        super().__init__(creature_health, creature_speed, x, y)
        self.food_class = Grass

