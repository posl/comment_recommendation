def round_down(num, divisor):
    return num - (num%divisor)
x,k = map(int, input().split())
for i in range(k):
    x = round_down(x, 10**i)
print(x)
