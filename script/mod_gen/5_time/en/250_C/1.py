def problems250_c():
    n, q = map(int, input().split())
    x = [int(input()) for _ in range(q)]
    ans = list(range(1, n+1))
    for i in range(q-1, -1, -1):
        ans[i], ans[i+1] = ans[i+1], ans[i]
        if ans[i+1] == x[i]:
            ans[i+1], ans[i+2] = ans[i+2], ans[i+1]
    print(*ans)

if __name__ == '__main__':
    problems250_c()