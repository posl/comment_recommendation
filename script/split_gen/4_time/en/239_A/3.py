def horizon(h):
    return ((h * (12800000 + h)) ** 0.5)
h = int(input())
print(horizon(h))
