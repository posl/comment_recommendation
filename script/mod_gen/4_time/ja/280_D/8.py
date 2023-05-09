def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
K = int(input())
ans = 0
for i in range(1, 1000000):
    if K <= factorial(i):
        ans = i
        break
print(ans)

if __name__ == '__main__':
    factorial()