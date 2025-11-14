import random

def rand_gen(min, max):
    while True:
        yield random.randint(min, max)


g = rand_gen(1, 100)

for i in range(5):
    print(next(g))
