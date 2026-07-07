from collections import deque

class PathFinder():
    def __init__(self):
        pass

    # Функция движения обьекта к ближайшей пище
    def find_path(self, start_pos, target_pos, core_map, food_class):
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
                if core_map.is_in_bounds(neighbor):

                    step_object = core_map.get_entity_on_map(neighbor)
                    # Можно идти в пустоту или на еду
                    if (step_object is None or isinstance(step_object,
                                                          food_class)) and neighbor not in visited:
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