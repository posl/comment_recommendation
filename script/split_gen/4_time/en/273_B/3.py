def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier
x, k = map(int, input().split())
for i in range(k):
    x = round_up(x, -i-1)
print(int(x))
