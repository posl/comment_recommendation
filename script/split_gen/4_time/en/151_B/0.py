def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    if M * N - sum(A) > K:
        print(-1)
    else:
        print(max(M * N - sum(A), 0))
