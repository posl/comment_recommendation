def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    K = [int(input()) for _ in range(Q)]
    ans = []
    # Aに含まれない数をKより大きい順に並べる
    B = [i for i in range(1, A[0])] + [i for i in range(A[-1]+1, 10**18+1)]
    # print(B)
    # Kより小さい数をAに追加し、Aをソートする
    A += B
    A.sort()
    # print(A)
    for k in K:
        ans.append(A[k-1])
    print(*ans, sep='\n')
