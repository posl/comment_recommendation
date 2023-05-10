def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
p = int(input())
ans = 0
for i in range(10, 0, -1):
    if p >= factorial(i):
        ans += p // factorial(i)
        p %= factorial(i)
print(ans)

if __name__ == '__main__':
    factorial()