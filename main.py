from numbers import Number
from typing import List, Tuple, Optional
from random import randint as rand
from itertools import permutations
from math import factorial


example = [(0, 2), (2, 5), (5, 2), (6, 6), (8, 3)]
example2 = [(0, 1), (1, 4), (4, 1), (5, 5), (7, 2)]


# функция для генерации произвольного набора точек
def gen_rand_dot_arr(number: int) -> List[Tuple]:
    dot_arr = []
    while number:
        dot = (rand(1, 10), rand(1, 10))
        dot_arr.append(dot)
        number -= 1

    return dot_arr


def get_distance(dot1: Tuple, dot2: Tuple) -> Optional[float]:
    try:
        if isinstance(dot1[0], Number) and isinstance(dot1[1], Number) \
                and isinstance(dot2[0], Number) and isinstance(dot2[1], Number):

            return ((dot1[0] - dot2[0]) ** 2 + (dot1[1] - dot2[1]) ** 2) ** 0.5
    except IndexError:
        return None
    except TypeError:
        return None
    return None


def get_route_length(sequence: Tuple, matrix: List[List]) -> float:
    total_length = 0
    for index in range(len(sequence) - 1):
        total_length += matrix[sequence[index] - 1][sequence[index + 1] - 1]
    return total_length


# функция для получения всех путей при фиксированной начальной и конечной точки
def get_permutations_fixed(n: int = 4) -> List[Tuple]:
    arr = [i + 1 for i in range(1, n + 1)]
    arr_to_return = []
    perm = permutations(arr)
    for _ in range(factorial(n)):
        arr_to_return.append((1, *perm.__next__(), 1))
    return arr_to_return


# функция для получения всех возможных путей
# параметр fixed в положении true говорит о том, что первая и последняя точки маршрута фиксированы
def get_permutations(n: int, fixed: bool = False) -> List[Tuple]:
    arr_to_return = []
    arr = [i for i in range(1, n + 1)] if not fixed else [i + 1 for i in range(1, n)]
    perm = permutations(arr)
    if fixed:
        for _ in range(factorial(n - 1)):
            arr_to_return.append((1, *perm.__next__(), 1))
    else:
        for _ in range(factorial(n)):
            arr_to_return.append(perm.__next__())
    return arr_to_return


def beautiful_output(matrix: List[List], dots: List[Tuple], route: Tuple, best_length: float) -> str:
    output = str(dots[route[0] - 1])
    for i in range(1, len(route)):
        output += f" -> {dots[route[i] - 1]}[{matrix[route[i - 1] - 1][route[i] - 1]}]"
    output += f" = {best_length}"
    return output


# получение матрицы расстояний
def get_all_distances(dots: List[Tuple]) -> Optional[List[List]]:
    matrix = []
    for _ in range(len(dots)):
        matrix.append([0 for _ in range(len(dots))])

    for i in range(len(dots) - 1):
        dot1 = dots[i]
        matrix[i][i] = 0
        for j in range(i + 1, len(dots)):
            dot2 = dots[j]
            matrix[i][j] = get_distance(dot1, dot2)
            if not isinstance(matrix[i][j], Number):
                return None
            matrix[j][i] = matrix[i][j]
    return matrix


def get_best_route(dots: List[Tuple]):
    if not dots or not hasattr(dots, '__iter__') or not hasattr(dots, "__getitem__"):
        return "Неверный формат данных"
    matrix = get_all_distances(dots)
    if not matrix:
        return "Неверный формат данных"

    # Для произвольных путей, без фиксированных начальной и конечной точкек
    # routes = get_permutations(len(dots))

    # Для набора с фиксированной точкой
    routes = get_permutations(len(dots), fixed=True)

    best_length = float('inf')
    best_route = tuple()
    for route in routes:
        current_length = get_route_length(route, matrix)
        if current_length < best_length:
            best_length = current_length
            best_route = route

    if best_length == 0:
        return "Неверный формат данных"
    return beautiful_output(matrix, dots, best_route, best_length)


if __name__ == "__main__":
    print(get_best_route(example))
    # проверка для произвольного набора точек
    # rand_dots = gen_rand_dot_arr(10)
    # print(f"Рандомный набор точек {rand_dots}")
    # print(get_best_route(rand_dots))
