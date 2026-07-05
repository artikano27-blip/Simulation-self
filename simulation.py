import pygame
from map import Map
from random import randint

# Импортируем всех существ и объекты из тех файлов, где они у тебя лежат
from creature import Predator, Herbivore, Grass, Creature, Rock, Tree
from random import randint

class Simulation:
    def __init__(self):
        screen_width = 800
        screen_height = 600
        pygame.init()
        self.core_map = Map()
        self.clock = pygame.time.Clock()
        self.grass_chance = 20
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.set_init_data()

    # Функция создания групп заданных обьектов, для удобного редактирования и теста мира.
    def produce_entities(self, entity, len_entity, creature_health=None, creature_speed=None, damage=None):
        produce_attempts = 0
        #Обходим возможность того что обьект не разместится на карте из-за конфликта координат
        while len_entity > 0:
            # Ломаем While если попыток создания обьекта превысило 2000 раз.
            if produce_attempts == 2000: break
            x = randint(0, 40)
            y = randint(0, 30)
            if entity is Predator:
                produce_entity = entity(creature_health, creature_speed, damage, x, y)
            elif entity is Herbivore:
                produce_entity = entity(creature_health, creature_speed, x, y)
            else:
                produce_entity = entity(x, y)
            if self.core_map.add_entity_to_map(produce_entity, produce_entity.object_coordinates):
                len_entity -= 1
            produce_attempts += 1

    # Заполняем карту обьектами
    def set_init_data(self):
        self.produce_entities(Predator, 10, 100, 100, 100)
        self.produce_entities(Grass, 10)
        self.produce_entities(Herbivore, 10, 100, 100)
        self.produce_entities(Tree,10)
        self.produce_entities(Rock,10)

    # Функция обновить всех существ на карте
    def update_all_creatures(self):
        # Собираем всех существ в список
        creatures_ready_to_moved_on = []
        for entity_coordinate, entity in self.core_map.map_contain_entities.items():
            if isinstance(entity, Creature):
                creatures_ready_to_moved_on.append(entity)
        # Делаем ход каждым существом
        for creature in creatures_ready_to_moved_on:
            get_object = self.core_map.map_contain_entities.get(creature.object_coordinates)
            if get_object == creature:
                creature.make_turn(self.core_map)

    # Функция контроля травы на карте, с шансом 20 % спавнится трава, но если этого не произошло прибавляем к шансу 5%. после спавна возращаем шанс.
    def grass_balance_function(self):
        make_toss =  randint(1, 100)
        if make_toss>self.grass_chance:
            self.grass_chance+=5
        else:
            self.produce_entities(Grass,2)
            self.grass_chance = 20

    # Функция запуска симуляции в реальном времени
    def run_loop_simulation(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.screen.fill((255, 255, 255))
            self.core_map.render_map(self.screen)
            self.grass_balance_function()
            self.update_all_creatures()
            pygame.display.flip()
            self.clock.tick(2)
        pygame.quit()
