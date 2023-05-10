def main():
    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n-1):
        if a[i] > a[i+1]:
            ans += (a[i] - a[i+1]) * l
            a[i+1] = a[i]
    for i in range(n-1,0,-1):
        if a[i] < a[i-1]:
            ans += (a[i-1] - a[i]) * r
            a[i-1] = a[i]
    print(ans)

if __name__ == '__main__':
    main()