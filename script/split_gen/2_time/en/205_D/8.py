def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    K = [int(input()) for _ in range(Q)]
    # 1. Aの隣り合う要素の差を求める
    # 2. 差の中にK[i]を入れることができるかを二分探索で探す
    # 3. 2.で見つけた差の中で最小のものをK[i]に加える
    # 4. 3.で求めた値をAに挿入する
    # 5. 1.に戻る
    for i in range(Q):
        diff = []
        for j in range(N - 1):
            diff.append(A[j + 1] - A[j])
        ok = -1
        ng = N
        while ng - ok > 1:
            mid = (ok + ng) // 2
            if diff[mid] > K[i]:
                ng = mid
            else:
                ok = mid
        if ok == -1:
            ans = A[0] + K[i]
        elif ok == N - 1:
            ans = A[N - 1] + K[i] - diff[ok - 1]
        else:
            ans = A[ok] + K[i] - diff[ok - 1]
        A.append(ans)
        A.sort()
        print(ans)
