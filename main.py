from simulation import Simulation
print("1. Создаем объект симуляции...")
if __name__ == "__main__":
    world_1 = Simulation()
    print("2. Запускаем метод run()...")
    world_1.run_loop_simulation()