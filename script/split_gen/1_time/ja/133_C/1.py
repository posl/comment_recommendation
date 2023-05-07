def main():
    L, R = map(int, input().split())
    ans = 2019
    for i in range(L, min(L + 2019, R + 1)):
        for j in range(i + 1, min(L + 2019, R + 1)):
            ans = min(ans, (i * j) % 2019)
            if ans == 0:
                print(ans)
                return
    print(ans)
