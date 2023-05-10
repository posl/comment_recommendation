def main():
    N, K = map(int, input().split())
    D = []
    A = []
    for i in range(K):
        D.append(int(input()))
        A.append(list(map(int, input().split())))
    S = set()
    for i in range(K):
        S |= set(A[i])
    print(N - len(S))
