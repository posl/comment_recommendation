def main():
    s = input()
    n = len(s)
    a = [0] * n
    b = [0] * n
    for i in range(n):
        if s[i] == 'R':
            a[i] += 1
            b[i+1] -= 1
        else:
            b[i] += 1
            a[i-1] -= 1
    for i in range(n):
        a[i+1] += a[i]
        b[i+1] += b[i]
    ans = [0] * n
    for i in range(n):
        ans[i] = a[i] + b[i]
    print(*ans)

if __name__ == '__main__':
    main()