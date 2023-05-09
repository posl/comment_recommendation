def calc_tax(price, rate):
    return price * rate // 100
a, b = map(int, input().split())
for i in range(1, 1000):
    if calc_tax(i, 8) == a and calc_tax(i, 10) == b:
        print(i)
        exit()
print(-1)
