import random

TIMES_TO_REPEAT = 10**5
LENGTH = 10**5

def in_circle(x, y):
    return x**2 + y**2 < LENGTH**2

inside_count = 0
for _ in range(TIMES_TO_REPEAT):
    point = random.randint(0,LENGTH), random.randint(0,LENGTH)
    if in_circle(*point):
        inside_count += 1

pi = (inside_count / TIMES_TO_REPEAT) * 4

print(pi)