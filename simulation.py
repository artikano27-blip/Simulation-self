import pygame
from map import Map

# Импортируем всех существ и объекты из тех файлов, где они у тебя лежат
from creature import Predator, Herbivore, Grass, Creature

class Simulation:
    def __init__(self):
        screen_width = 800
        screen_height = 600
        pygame.init()
        self.core_map = Map()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((screen_width,screen_height))
        self.set_init_data()
    #Заполняем карту обьектами
    def set_init_data(self):

        wolf = Predator(100, 100, 100, 20, 10)
        wolf_1 = Predator(100, 100, 100, 10, 20)
        wolf_2 = Predator(100, 100, 100, 8, 14)

        sheep = Herbivore(100, 100, 1, 1)
        sheep_1 = Herbivore(100, 100, 5, 2)
        sheep_2 = Herbivore(100, 100, 10, 5)

        grass = Grass(10, 4)
        grass_1 = Grass(4, 6)
        grass_2 = Grass(1, 5)

        self.core_map.add_entity_to_map(wolf, wolf.object_coordinates)
        self.core_map.add_entity_to_map(wolf_1, wolf_1.object_coordinates)
        self.core_map.add_entity_to_map(wolf_2, wolf_2.object_coordinates)

        self.core_map.add_entity_to_map(sheep, sheep.object_coordinates)
        self.core_map.add_entity_to_map(sheep_1, sheep_1.object_coordinates)
        self.core_map.add_entity_to_map(sheep_2, sheep_2.object_coordinates)
    #Функция обновить всех существ на карте
    def update_all_creatures(self):
        #Собираем всех существ в список
        creatures_ready_to_moved_on = []
        for entity_coordinate, entity in self.core_map.map_contain_entities.items():
            if isinstance(entity,Creature):
              creatures_ready_to_moved_on.append(entity)
        #Делаем ход каждым существом
        for creature in creatures_ready_to_moved_on:
            get_object = self.core_map.map_contain_entities.get(creature.object_coordinates)
            if get_object == creature:
                creature.make_turn(self.core_map)
    #Функция запуска симуляции в реальном времени
    def run_loop_simulation(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill((255, 255, 255))
            self.core_map.render_map(self.screen)
            self.update_all_creatures()
            pygame.display.flip()
            self.clock.tick(2)
        pygame.quit()

