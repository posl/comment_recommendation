def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 2**30
    for i in range(n):
        for j in range(i, n):
            x = a[i]
            for k in range(i+1, j+1):
                x |= a[k]
            ans = min(ans, x)
    print(ans)

if __name__ == '__main__':
    main()