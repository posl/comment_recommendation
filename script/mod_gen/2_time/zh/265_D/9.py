def solve():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    #累加和
    Asum = [0] * (N + 1)
    for i in range(N):
        Asum[i + 1] = Asum[i] + A[i]
    #最大值和最小值
    maxA = A[0]
    minA = A[0]
    for i in range(N):
        maxA = max(maxA, A[i])
        minA = min(minA, A[i])
    #最大值和最小值的累加和
    maxAsum = [0] * (N + 1)
    minAsum = [0] * (N + 1)
    for i in range(N):
        maxAsum[i + 1] = maxAsum[i] + maxA - A[i]
        minAsum[i + 1] = minAsum[i] + minA - A[i]
    #最大值和最小值的累加和的最大值和最小值
    maxmaxAsum = maxAsum[0]
    minminAsum = minAsum[0]
    for i in range(N):
        maxmaxAsum = max(maxmaxAsum, maxAsum[i])
        minminAsum = min(minminAsum, minAsum[i])
    #判断
    if maxmaxAsum - minminAsum <= R - P and maxAsum[N] - minAsum[N] == R - P and \
            maxAsum[N] - minAsum[N] == Q - R and Asum[N] == Q:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    solve()