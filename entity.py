# Создаем класы неподвижных обьектов
class Entity:
    # Указываем координаты для будущей работы с травой
    def __init__(self, x, y):
        self.object_coordinates = (x, y)


class Rock(Entity):
    pass


class Grass(Entity):
    pass


class Tree(Entity):
    pass
