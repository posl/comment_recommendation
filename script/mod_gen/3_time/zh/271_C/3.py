def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a[0] > 1:
        print(0)
        return
    ans = 1
    for i in range(1, n):
        ans *= a[i]
        if ans > 10**18:
            print(-1)
            return
    print(ans)

if __name__ == '__main__':
    main()