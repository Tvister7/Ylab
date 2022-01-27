from main import get_best_route

test1 = []
test2 = [()]
test3 = [(3, ), (1, 2)]
test4 = "test"
test5 = (4, 2)
test6 = 3
test7 = [(3, ), (1, 2)]
test8 = {(0, 2), (2, 5), (5, 2), (6, 6), (8, 3)}
test9 = ((0, 2), (2, 5), (5, 2), (6, 6), (8, 3))

assert get_best_route(test1) == "Неверный формат данных"
assert get_best_route(test2) == "Неверный формат данных"
assert get_best_route(test3) == "Неверный формат данных"
assert get_best_route(test4) == "Неверный формат данных"
assert get_best_route(test5) == "Неверный формат данных"
assert get_best_route(test6) == "Неверный формат данных"
assert get_best_route(test7) == "Неверный формат данных"
assert get_best_route(test8) == "Неверный формат данных"
assert get_best_route(test9) == "(0, 2) -> (2, 5)[3.605551275463989] -> (6, 6)[4.123105625617661] ->" \
                                " (8, 3)[3.605551275463989] -> (5, 2)[3.1622776601683795] = 14.496485836714019"
