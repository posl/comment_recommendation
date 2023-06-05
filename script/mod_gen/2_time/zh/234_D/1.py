def f(n):
    if n == 0:
        return 0
    else:
        return n % 2 + 10 * f(n // 2)
k = int(input())
i = 0
while True:
    if f(i) == k:
        print(i)
        break
    i += 1

if __name__ == '__main__':
    f()