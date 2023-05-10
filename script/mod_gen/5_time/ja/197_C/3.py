def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 2**31-1
    for i in range(n):
        for j in range(i, n):
            x = 0
            for k in range(i, j+1):
                x = x | a[k]
            ans = min(ans, x)
    print(ans)

if __name__ == '__main__':
    main()