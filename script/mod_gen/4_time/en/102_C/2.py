def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0]*n
    for i in range(n):
        b[i] = a[i] - (i+1)
    b.sort()
    if n % 2 == 0:
        b1 = b[n//2]
        b2 = b[n//2-1]
        ans = 0
        for i in range(n):
            ans += abs(b1-b[i])
            ans += abs(b2-b[i])
        ans = min(ans, ans2)
    else:
        b1 = b[n//2]
        ans = 0
        for i in range(n):
            ans += abs(b1-b[i])
    print(ans)

if __name__ == '__main__':
    main()