def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 1
    for i in range(n):
        ans *= a[i]
        if ans > 10**18:
            ans = -1
            break
    print(ans)

if __name__ == '__main__':
    main()