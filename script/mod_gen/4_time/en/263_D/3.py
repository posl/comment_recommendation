def main():
    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n-1):
        if a[i+1] - a[i] > 0:
            ans += (a[i+1] - a[i]) * l
        else:
            ans += (a[i+1] - a[i]) * r
    print(ans)

if __name__ == '__main__':
    main()