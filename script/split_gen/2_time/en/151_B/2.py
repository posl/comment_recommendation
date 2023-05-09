def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    if sum(A) + N * K >= N * M:
        print(max(0, N * M - sum(A)))
    else:
        print(-1)
