def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    #print(N, K, P)
    sum = 0
    for i in range(K):
        sum += (P[i] + 1) / 2
    max = sum
    for i in range(N - K):
        sum -= (P[i] + 1) / 2
        sum += (P[i + K] + 1) / 2
        if sum > max:
            max = sum
    print(max)
