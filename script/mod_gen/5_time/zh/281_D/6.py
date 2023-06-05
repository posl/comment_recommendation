def main():
    n, k, d = map(int, input().split())
    a = list(map(int, input().split()))
    ans = -1
    for i in range(1, n+1):
        for j in range(0, n-i+1):
            if sum(a[j:j+i]) % d == 0:
                ans = max(ans, sum(a[j:j+i]))
    print(ans)

if __name__ == '__main__':
    main()