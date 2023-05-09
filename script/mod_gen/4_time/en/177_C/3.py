def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        ans += a[i] * sum(a[i+1:])
    print(ans%(10**9+7))

if __name__ == '__main__':
    main()