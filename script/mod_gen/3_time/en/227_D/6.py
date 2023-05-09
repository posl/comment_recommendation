def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n-k+1):
        ans = max(ans, a[i] * a[n-k+i])
    print(ans)

if __name__ == '__main__':
    main()