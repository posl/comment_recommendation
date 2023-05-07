def round_up(x, y):
    if x % y == 0:
        return x
    else:
        return (x // y + 1) * y
x, k = map(int, input().split())
for i in range(k):
    x = round_up(x, 10 ** (k - i))
print(x)
