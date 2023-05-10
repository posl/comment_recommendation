def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
k = int(input())
n = 1
while True:
    if factorial(n) % k == 0:
        print(n)
        break
    n += 1

if __name__ == '__main__':
    factorial()