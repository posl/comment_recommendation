def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
p = int(input())
coin = 0
for i in range(10,0,-1):
    coin += p // factorial(i)
    p %= factorial(i)
print(coin)

if __name__ == '__main__':
    factorial()