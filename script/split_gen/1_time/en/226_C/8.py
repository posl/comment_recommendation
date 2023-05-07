def main():
    # Get input
    N = int(input())
    T = []
    A = []
    for i in range(N):
        t, k = list(map(int, input().split()))
        T.append(t)
        A.append(list(map(lambda x: int(x)-1, input().split())))
    # Solve
    dp = [0] * N
    for i in range(1, N):
        dp[i] = T[i] + min([dp[j] for j in A[i]])
    print(dp[-1])
