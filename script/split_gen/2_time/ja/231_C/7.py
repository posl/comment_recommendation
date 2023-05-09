def main():
    #入力
    N,Q = map(int,input().split())
    A = list(map(int,input().split()))
    x = [int(input()) for _ in range(Q)]
    #Aを降順にソート
    A.sort(reverse=True)
    #Aの累積和を計算
    A_sum = [0] * (N+1)
    for i in range(N):
        A_sum[i+1] = A_sum[i] + A[i]
    #xを昇順にソート
    x.sort()
    #xの各要素に対して、Aの累積和で二分探索
    for i in range(Q):
        ok = N
        ng = 0
        while abs(ok-ng) > 1:
            mid = (ok+ng)//2
            if A_sum[mid] >= x[i]:
                ok = mid
            else:
                ng = mid
        print(N-ok)
