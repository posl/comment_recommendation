def check(k):
    num = 0
    for i in range(1000000):
        num = num * 10 + 7
        num %= k
        if num == 0:
            return i + 1
    return -1
k = int(input())
print(check(k))
