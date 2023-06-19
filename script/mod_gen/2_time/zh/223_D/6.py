def main():
    n, m = map(int, input().split())
    a = []
    b = []
    for _ in range(m):
        a1, b1 = map(int, input().split())
        a.append(a1)
        b.append(b1)
    ans = [0] * n
    for i in range(n):
        ans[i] = i + 1
    for i in range(m):
        if ans[a[i] - 1] > ans[b[i] - 1]:
            ans[a[i] - 1], ans[b[i] - 1] = ans[b[i] - 1], ans[a[i] - 1]
    print(*ans)

if __name__ == '__main__':
    main()