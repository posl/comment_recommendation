def main():
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    if D == 1:
        print(A[K - 1])
    else:
        # Dの倍数の個数を数える
        # Dの倍数がK個未満なら、Dの倍数はK個
        # Dの倍数がK個以上なら、Dの倍数はK+1個
        # Dの倍数がK個以上なら、Dの倍数はK+1個
        cnt = 0
        for i in range(N):
            if A[i] % D == 0:
                cnt += 1
        if cnt < K:
            print(A[K - 1])
        else:
            print(A[K])
