def janken(x, y):
    if x == 0 and y == 1:
        return 2
    if x == 0 and y == 2:
        return 0
    if x == 1 and y == 0:
        return 0
    if x == 1 and y == 2:
        return 1
    if x == 2 and y == 0:
        return 2
    if x == 2 and y == 1:
        return 1
x, y = map(int, input().split())
print(janken(x, y))
