def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    if (N * M) - sum(A) > K:
        print(-1)
    elif (N * M) - sum(A) < 0:
        print(0)
    else:
        print((N * M) - sum(A))
