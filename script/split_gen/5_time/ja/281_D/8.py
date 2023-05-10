def main():
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.reverse()
    S = set()
    for i in range(K):
        S.add(A[i])
    if len(S) == 1:
        print(-1)
    else:
        print(max(S))
