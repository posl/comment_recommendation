def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1)
P = int(input())
coin = 0
for i in range(10, 0, -1):
    if P >= fact(i):
        coin += P // fact(i)
        P = P % fact(i)
print(coin)
