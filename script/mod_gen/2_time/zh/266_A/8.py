def solve():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    # 从左到右的累加和
    S = [0] * N
    S[0] = A[0]
    for i in range(1, N):
        S[i] = S[i - 1] + A[i]
    # 从右到左的累加和
    T = [0] * N
    T[N - 1] = A[N - 1]
    for i in range(N - 2, -1, -1):
        T[i] = T[i + 1] + A[i]
    # 累加和的最大值和最小值
    maxS = S[0]
    minS = S[0]
    maxT = T[N - 1]
    minT = T[N - 1]
    for i in range(1, N):
        if maxS < S[i]:
            maxS = S[i]
        if minS > S[i]:
            minS = S[i]
        if maxT < T[i]:
            maxT = T[i]
        if minT > T[i]:
            minT = T[i]
    # 满足条件的元组
    Yes = False
    for i in range(N):
        if (minS <= P - S[i] <= maxS and minT <= Q - S[i] <= maxT and minT <= R - S[i] <= maxT):
            Yes = True
            break
    if Yes:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    solve()