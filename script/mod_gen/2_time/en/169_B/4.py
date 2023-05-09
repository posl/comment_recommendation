def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 1
    for i in range(n):
        if a[i] == 0:
            print(0)
            return
        ans *= a[i]
        if ans > 10**18:
            print(-1)
            return
    print(ans)

if __name__ == '__main__':
    main()