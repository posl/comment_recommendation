def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    x = a[0]
    y = a[-1]
    ans = 0
    for i in range(n):
        ans += (y-x)
        x = a[i]
        y = a[i+1]
    print(ans)

if __name__ == '__main__':
    main()