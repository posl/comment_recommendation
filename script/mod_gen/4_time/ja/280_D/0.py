def func(k):
    if k % 2 == 0:
        return 2
    elif k % 3 == 0:
        return 3
    elif k % 5 == 0:
        return 5
    else:
        return 1
k = int(input())
n = 1
while True:
    if n % k == 0:
        print(n)
        break
    else:
        n *= func(n)
