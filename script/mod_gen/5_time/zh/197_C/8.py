def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        x = a[i]
        for j in range(i, n):
            x = x | a[j]
            y = x
            for k in range(j + 1, n):
                y = y ^ a[k]
                ans = max(ans, y)
    print(ans)

if __name__ == '__main__':
    main()