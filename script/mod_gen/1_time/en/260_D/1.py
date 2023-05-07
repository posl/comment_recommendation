def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    ans = [-1] * n
    for i in range(n):
        p[i] -= 1
    for i in range(n):
        if ans[i] != -1:
            continue
        cur = i
        cnt = 0
        while ans[cur] == -1:
            ans[cur] = i
            cur = p[cur]
            cnt += 1
        if cnt % k == 0:
            continue
        cur = i
        while ans[cur] == i:
            ans[cur] = -1
            cur = p[cur]
    for i in range(n):
        if ans[i] == -1:
            print(-1)
        else:
            print(ans[i] + 1)

if __name__ == '__main__':
    main()