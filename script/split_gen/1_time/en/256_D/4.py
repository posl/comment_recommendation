def solve():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    A.sort()
    ans = [[A[0][0], A[0][1]]]
    for i in range(1, N):
        if ans[-1][1] < A[i][0]:
            ans.append([A[i][0], A[i][1]])
        else:
            ans[-1][1] = max(ans[-1][1], A[i][1])
    for i in range(len(ans)):
        print(ans[i][0], ans[i][1])
    return 0
