def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
P = int(input())
coin = 0
for i in range(10, 0, -1):
    coin += P // factorial(i)
    P = P % factorial(i)
print(coin)

if __name__ == '__main__':
    factorial()