def main():
    N, K = map(int, input().split())
    A = []
    for i in range(K):
        A.append(list(map(int, input().split())))
    print(N - len(set([A[i][j] for i in range(K) for j in range(1, len(A[i]))])))
