def main():
    N = int(input())
    S = input()
    W = [int(x) for x in input().split()]
    W1 = [W[i] for i in range(N) if S[i] == '1']
    W0 = [W[i] for i in range(N) if S[i] == '0']
    W1.sort()
    W0.sort()
    if len(W1) == 0 or len(W0) == 0:
        print(0)
        return
    W1sum = [0] * (len(W1) + 1)
    W0sum = [0] * (len(W0) + 1)
    for i in range(len(W1)):
        W1sum[i+1] = W1sum[i] + W1[i]
    for i in range(len(W0)):
        W0sum[i+1] = W0sum[i] + W0[i]
    ans = 0
    for i in range(len(W1) + 1):
        for j in range(len(W0) + 1):
            if W1sum[i] + W0sum[j] <= 2 * (i + j):
                ans = max(ans, i + j)
    print(ans)
