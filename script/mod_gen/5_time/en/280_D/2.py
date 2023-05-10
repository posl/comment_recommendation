def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
k = int(input())
n = 1
while factorial(n) % k != 0:
    n += 1
print(n)

if __name__ == '__main__':
    factorial()