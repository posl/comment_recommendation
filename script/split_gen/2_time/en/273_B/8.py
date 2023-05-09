def round_up_to_10_power_i(x, i):
    if i == 0:
        return x
    if x % (10**i) == 0:
        return x
    return x + (10**i - x % (10**i))
x, k = map(int, input().split())
for i in range(k):
    x = round_up_to_10_power_i(x, i)
print(x)
