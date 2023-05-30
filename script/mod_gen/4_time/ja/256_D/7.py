def solve():
    n = int(input())
    lr = [list(map(int, input().split())) for _ in range(n)]
    lr.sort(key=lambda x: x[0])
    ans = []
    ans.append([lr[0][0], lr[0][1]])
    for i in range(1, n):
        if ans[-1][1] < lr[i][0]:
            ans.append([lr[i][0], lr[i][1]])
        else:
            if ans[-1][1] < lr[i][1]:
                ans[-1][1] = lr[i][1]
    for i in range(len(ans)):
        print(*ans[i])
solve()
