def get_opposite(x):
    return 2 if x == 0 else 0
x, y = map(int, input().split())
print(get_opposite(x) if x == y else 1 if x != get_opposite(y) else y)
