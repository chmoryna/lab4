def factorial(n):
    if not isinstance(n, int):
        raise TypeError("Факторіал визначений тільки для цілих чисел")
    if n < 0:
        raise ValueError("Факторіал не визначений для від’ємних чисел")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
