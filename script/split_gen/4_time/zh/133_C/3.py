def f(L, R):
    if L == R:
        return 0
    if R - L >= 2019:
        return 0
    else:
        min = 2019
        for i in range(L, R):
            for j in range(i + 1, R + 1):
                if min > (i * j) % 2019:
                    min = (i * j) % 2019
        return min
L, R = map(int, input().split())
print(f(L, R))
