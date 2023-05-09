def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    sumA = sum(A)
    if (N * M) - sumA <= 0:
        print(0)
    elif (N * M) - sumA <= K:
        print((N * M) - sumA)
    else:
        print(-1)
