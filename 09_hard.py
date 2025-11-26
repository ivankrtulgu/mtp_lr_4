from functools import reduce

def pipeline():
    data = list(range(1, 16))
    print("Исходные данные:", data)

    result = reduce(lambda n, m: n * m,
                    filter(lambda n: n < 100,
                           map(lambda n: n * 10,
                               filter(lambda n: n % 3 == 0, data)
                               )
                           )
                    )

    print("Результат:", result)

pipeline()
