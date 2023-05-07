def main():
    s = input()
    n = len(s)
    a = [0] * n
    b = [0] * n
    for i in range(n):
        if s[i] == "0":
            a[i] = 1
        else:
            b[i] = 1
    for i in range(1, n):
        a[i] += a[i - 1]
        b[i] += b[i - 1]
    ans = 0
    for i in range(n):
        ans = max(ans, a[i] + b[n - 1] - b[i])
    print(ans)

if __name__ == '__main__':
    main()