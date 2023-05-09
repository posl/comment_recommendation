def main():
    L, R = map(int, input().split())
    if R - L >= 2019:
        print(0)
        exit()
    ans = 2018
    for i in range(L, R):
        for j in range(i + 1, R + 1):
            ans = min(ans, (i * j) % 2019)
        if ans == 0:
            break
    print(ans)

if __name__ == '__main__':
    main()