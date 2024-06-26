def main():
    l, r = map(int, input().split())
    if r - l >= 2019:
        print(0)
        return
    ans = 2018
    for i in range(l, r):
        for j in range(i+1, r+1):
            ans = min(ans, (i*j) % 2019)
    print(ans)

if __name__ == '__main__':
    main()