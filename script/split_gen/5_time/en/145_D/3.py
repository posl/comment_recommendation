def ways(x, y):
    if x + y == 0:
        return 1
    elif x < 0 or y < 0:
        return 0
    else:
        return ways(x-1, y-2) + ways(x-2, y-1)
x, y = map(int, input().split())
print(ways(x, y) % (10**9 + 7))
