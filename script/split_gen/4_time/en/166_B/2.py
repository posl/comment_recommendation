def main():
    N, K = map(int, input().split())
    S = [0] * N
    for i in range(K):
        d = int(input())
        A = list(map(int, input().split()))
        for j in range(d):
            S[A[j] - 1] = 1
    print(S.count(0))
