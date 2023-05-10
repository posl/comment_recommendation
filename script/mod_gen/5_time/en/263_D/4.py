def main():
    n,l,r = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        ans += a[i]
    for i in range(n-1):
        ans += min(l,r) * (a[i] < a[i+1])
    print(ans)

if __name__ == '__main__':
    main()