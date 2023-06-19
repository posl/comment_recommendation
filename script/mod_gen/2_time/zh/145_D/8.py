def knight(x, y):
    if x < 0 or y < 0:
        return 0
    if x == 0 and y == 0:
        return 1
    if x < y:
        x, y = y, x
    if x - y == 1:
        return 3 * knight(x - 2, y - 1) + 2 * knight(x - 3, y - 3)
    if x - y == 0:
        return 3 * knight(x - 2, y - 1) + 2 * knight(x - 3, y - 3) + knight(x - 3, y - 2)
    else:
        return 3 * knight(x - 2, y - 1) + 2 * knight(x - 3, y - 3) + knight(x - 3, y - 2) + 2 * knight(x - 4, y - 2)
x, y = map(int, input().split())
print(knight(x, y) % (10 ** 9 + 7))
