def main():
    L, R = map(int, input().split())
    r = 2019
    if R - L >= 2019:
        r = 0
    else:
        for i in range(L, R):
            for j in range(i + 1, R + 1):
                if (i * j) % 2019 < r:
                    r = (i * j) % 2019
    print(r)
