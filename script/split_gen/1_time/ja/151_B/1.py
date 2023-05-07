def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    if M * N - sum(A) <= K:
        print(max(0, M * N - sum(A)))
    else:
        print(-1)
