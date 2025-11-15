def memo(func):
    cache = {}

    def decorate(n):
        if n in cache:
            print("Результат из кэша: ", end='')
            return cache[n]
        result = func(n)
        cache[n] = result
        return result

    return decorate


@memo
def square(n):
    print("Вычисление происходит впервые: ", end='')
    return n * n


print(square(5))
print(square(5))
print(square(6))
print(square(7))
print(square(5))
print(square(6))
print(square(7))
print(square(8))

