def main():
    N, K = map(int, input().split())
    d = []
    A = []
    for i in range(K):
        d.append(int(input()))
        A.append(list(map(int, input().split())))
    S = set()
    for i in range(K):
        for j in range(d[i]):
            S.add(A[i][j])
    print(N - len(S))
