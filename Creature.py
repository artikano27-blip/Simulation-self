from Entity import Entity
from Map import Map
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
        current_coordinates = (self.object_coordinates)
        x,y = new_coordinate
        if x < 0 or y < 0 or x>= core_map.map_width or y>=core_map.map_height:
            return current_coordinates
        #Проверяем занята ли координата на карте обьектов
        else:
            if new_coordinate not in core_map.map_contain_entities:
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
    def calculate_next_step(self,closest_coordinate,core_map:Map):
        x1, y1 = self.object_coordinates
        x2, y2 = closest_coordinate

        # Задаем базовые значения, чтобы избежать ошибок и телепортаций
        new_coordinate_x = x1
        new_coordinate_y = y1

        # Логика L-образного движения
        if x1 != x2:
            if x1 > x2:
                new_coordinate_x = x1 - 1
            elif x1 < x2:
                new_coordinate_x = x1 + 1
        elif y1 != y2:
            if y1 > y2:
                new_coordinate_y = y1 - 1
            elif y1 < y2:
                new_coordinate_y = y1 + 1

        # Вызов родительского метода для фактического перемещения
        super().make_move((new_coordinate_x, new_coordinate_y), core_map)


