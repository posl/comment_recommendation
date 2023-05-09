def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n):
        if a[i] > n - 1:
            print(-1)
            return
        b[a[i]] += 1
    ans = 0
    for i in range(n):
        if b[i] > i:
            ans += b[i] - i
    print(ans)

if __name__ == '__main__':
    main()