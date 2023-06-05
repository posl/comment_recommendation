def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    if N*M-sum(A) <= K:
        print(max(0, N*M-sum(A)))
    else:
        print(-1)
