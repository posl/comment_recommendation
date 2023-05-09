def main():
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    b = [0] * n
    b[0] = a[0]
    for i in range(1,n):
        b[i] = b[i-1] + a[i]
    ans = 0
    for i in range(1,n+1):
        ans = max(ans, b[i-1] + (m-i)*a[i-1])
    print(ans)

if __name__ == '__main__':
    main()