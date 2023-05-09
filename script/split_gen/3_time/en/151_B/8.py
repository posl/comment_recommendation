def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    s = sum(A)
    if s >= M*N:
        print(0)
        exit()
    if s + K < M*N:
        print(-1)
        exit()
    print(M*N - s)
