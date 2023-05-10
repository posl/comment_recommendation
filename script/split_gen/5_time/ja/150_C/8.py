def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    # 順列の作成
    def permutation(N):
        if N == 1:
            return [[1]]
        else:
            return [p[:i]+[N]+p[i:] for p in permutation(N-1) for i in range(N)]
    # 順列の辞書順を求める
    def permutation_number(P):
        n = len(P)
        if n == 1:
            return 0
        else:
            return (P[-1]-1) * math.factorial(n-1) + permutation_number(P[:-1])
    # 辞書順の差を求める
    print(abs(permutation_number(P)-permutation_number(Q)))
