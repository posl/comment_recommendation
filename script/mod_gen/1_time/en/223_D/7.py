def main():
    n, m = map(int, input().split())
    x = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        x[a-1].append(b-1)
    ans = []
    for i in range(n):
        if len(x[i]) == 0:
            ans.append(i)
    if len(ans) == 0:
        print(-1)
        return
    for i in range(n):
        for j in range(i+1, n):
            if len(x[j]) == 0:
                ans.append(j)
                continue
            flag = False
            for k in range(len(x[j])):
                if x[j][k] == ans[i]:
                    flag = True
                    break
            if flag:
                ans.append(j)
                continue
    if len(ans) == n:
        for i in range(n):
            ans[i] += 1
        print(*ans)
    else:
        print(-1)

if __name__ == '__main__':
    main()