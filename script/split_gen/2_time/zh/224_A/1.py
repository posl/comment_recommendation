def main():
    n, m = map(int, input().split())
    a = []
    b = []
    for i in range(m):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    # print(a)
    # print(b)
    ans = [0] * n
    for i in range(n):
        ans[i] = i + 1
    # print(ans)
    for i in range(m):
        if ans[a[i] - 1] > ans[b[i] - 1]:
            ans[a[i] - 1], ans[b[i] - 1] = ans[b[i] - 1], ans[a[i] - 1]
    # print(ans)
    for i in range(n):
        if ans[i] == i + 1:
            print(-1)
            return
    print(' '.join(map(str, ans)))
