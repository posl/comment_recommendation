def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.append(max(0, N * M - sum(A)))
    if sum(A) >= N * M:
        print(0)
    elif sum(A) < N * M:
        if max(A) <= K:
            print(max(A))
        else:
            print(-1)
