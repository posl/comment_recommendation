def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 1<<30
    for i in range(1<<n-1):
        tmp = 0
        x = 0
        for j in range(n):
            x |= a[j]
            if i>>j&1:
                tmp ^= x
                x = 0
        tmp ^= x
        ans = min(ans, tmp)
    print(ans)

if __name__ == '__main__':
    main()