def main():
    l, r = map(int, input().split())
    ans = 2018
    for i in range(l, r):
        for j in range(i + 1, r + 1):
            ans = min(ans, (i * j) % 2019)
            if ans == 0:
                break
        if ans == 0:
            break
    print(ans)

if __name__ == '__main__':
    main()