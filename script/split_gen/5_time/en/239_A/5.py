def horizon(h):
    return ((h * (12800000 + h)) ** (1/2))
h = int(input())
print(horizon(h))
