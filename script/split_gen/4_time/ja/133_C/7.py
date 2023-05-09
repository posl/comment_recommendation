def main():
    L, R = map(int, input().split())
    if R - L >= 2019:
        print(0)
    else:
        x = L % 2019
        y = R % 2019
        if x >= y:
            print(0)
        else:
            ans = 2018
            for i in range(x, y):
                for j in range(i + 1, y + 1):
                    ans = min(ans, (i * j) % 2019)
            print(ans)
