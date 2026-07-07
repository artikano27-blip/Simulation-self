import pygame


class Map:
    def __init__(self, map_width=40, map_height=30):
        self.map_width = map_width
        self.map_height = map_height
        # Словарь для хранения координат на Карте обьектов
        self.map_contain_entities = {}

    # Функция добавления Обьекта на Карту обьектов
    def add_entity_to_map(self, entity, entity_coordinate):
        if entity_coordinate not in self.map_contain_entities:
            self.map_contain_entities[entity_coordinate] = entity
            print(f"Обьект {entity} добавлен по координатам {entity_coordinate}")
            return True
        else:
            # Безопасно возвращаем булево для будущих конструкций с функцией.
            return False

    # Получаем обьект по координатам из Карты обьектов
    def get_entity_on_map(self, entity_coordinate):
        return self.map_contain_entities.get(entity_coordinate)

    # Удаляем обьект по координатам из Карты обьектов
    def remove_entity_from_map(self, entity_coordinate):
        self.map_contain_entities.pop(entity_coordinate)
        print("Успешно удален")

    def is_empty(self, entity_coordinate):
        return entity_coordinate not in self.map_contain_entities

    def is_in_bounds(self, entity_coordinate):
        return 0 <= entity_coordinate[0] < self.map_width and 0 <= entity_coordinate[1] < self.map_height

    # Запускаем рендер карты
    def render_map(self, screen):
        from entity import Grass, Tree, Rock
        from creature import Predator, Herbivore
        # Коеффициент Scale. для размера карты 30*40 = выход в отрисовку идет как 40*20 и 30*20 = 800*600
        coordinate_scale_size = 20
        # Пробегаемся по карте обьектов
        for y in range(self.map_height):
            for x in range(self.map_width):
                scaled_x = x * coordinate_scale_size
                scaled_y = y * coordinate_scale_size
                # Получаем объект по координатам
                entity = self.map_contain_entities.get((x, y))
                # Если в этой клетке кто-то есть
                if entity is not None:
                    entity_color = None  # Создаем пустую переменную для цвета
                    # 1. Только определяем цвет
                    if isinstance(entity, Predator):
                        entity_color = (220, 20, 60)  # Красный
                    elif isinstance(entity, Herbivore):
                        entity_color = (65, 105, 225)  # Синий
                    elif isinstance(entity, Rock):
                        entity_color = (128, 128, 128)  # Серый
                    elif isinstance(entity, Tree):
                        entity_color = (139, 69, 19)  # Коричневый
                    elif isinstance(entity, Grass):
                        entity_color = (50, 205, 50)  # Зеленый
                    # Подставляем если находим присвоенный цвет
                    if entity_color is not None:
                        pygame.draw.rect(screen, entity_color,
                                         (scaled_x, scaled_y, coordinate_scale_size, coordinate_scale_size))
        pygame.display.flip()
