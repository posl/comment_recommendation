def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n-1):
        ans += (i+1)*a[i]
        ans -= (n-i-1)*a[i]
    print(ans%(10**9+7))
main()

if __name__ == '__main__':
    main()