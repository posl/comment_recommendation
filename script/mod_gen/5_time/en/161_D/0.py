def lunlun(n):
    if n < 10:
        return n
    last = n % 10
    if last == 0:
        return lunlun(n // 10 - 1) * 10 + 9
    if last == 9:
        return lunlun(n // 10) * 10 + 8
    return lunlun(n // 10) * 10 + last - 1
K = int(input())
for i in range(K):
    print(lunlun(i+1))
