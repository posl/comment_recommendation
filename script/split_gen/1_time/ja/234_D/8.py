def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    # P[i]はi+1番目に小さい値とする
    for i in range(N):
        P[i] -= 1
    # 累積和
    s = [0] * (N+1)
    for i in range(N):
        s[i+1] = s[i] + P[i]
    # 二分探索
    def binary_search(x):
        ok = N
        ng = -1
        while abs(ok-ng) > 1:
            mid = (ok+ng)//2
            if s[mid] < x:
                ng = mid
            else:
                ok = mid
        return ok
    # 出力
    for i in range(K, N+1):
        print(binary_search(i))
