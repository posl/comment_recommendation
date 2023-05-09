def lunlun(k):
    if k <= 9:
        return k
    n = 9
    a = [i for i in range(1, 10)]
    while n < k:
        x = a.pop(0)
        for i in range(-1, 2):
            y = x % 10 + i
            if y >= 0 and y <= 9:
                a.append(x * 10 + y)
        n += 1
    return a[0]
k = int(input())
print(lunlun(k))

if __name__ == '__main__':
    lunlun()