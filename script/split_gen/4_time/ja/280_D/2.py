def calc_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calc_factorial(n-1)
k = int(input())
n = 1
while True:
    if calc_factorial(n) % k == 0:
        print(n)
        break
    else:
        n += 1
