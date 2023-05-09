def main():
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A = A[::-1]
    S = set()
    for i in range(N):
        for j in range(i+1, N):
            S.add(A[i] + A[j])
    S = list(S)
    S.sort()
    S = S[::-1]
    for i in range(len(S)):
        if S[i] % D == 0:
            print(S[i])
            exit()
    print(-1)
