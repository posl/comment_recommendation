def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0] * n
    x = [0] * q
    for i in range(q):
        x[i] = int(input())
    for i in range(n - 1):
        b[i] = a[i + 1] - a[i]
    b[n - 1] = 0
    ans = 0
    for i in range(n):
        ans += abs(b[i])
    for i in range(q):
        if x[i] == 0:
            print(ans)
        else:
            if x[i] - 1 >= 0:
                ans += abs(b[x[i] - 1])
            if x[i] < n:
                ans += abs(b[x[i]])
            if x[i] - 2 >= 0 and x[i] < n:
                ans -= abs(b[x[i] - 1] + b[x[i]])
            b[x[i] - 1] = 0
            b[x[i]] = 0
            print(ans)

if __name__ == '__main__':
    main()