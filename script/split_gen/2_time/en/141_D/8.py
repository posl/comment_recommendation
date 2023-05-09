def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    # 1. A を昇順にソートする
    # 2. A[i] が A[i-1] に対して 2^k 倍であるとして、
    #    A[i-1] を 2^k 倍したものを A[i] に置き換える
    # 3. A を降順にソートする
    # 4. A[i] に対して、M 個のチケットを使う
    # 5. A[i] を A[i-1] に置き換える
    # 6. A を降順にソートする
    # 7. 3 ～ 6 を A[0] に対して繰り返す
    # 8. A の総和を出力する
    for i in range(1, N):
        if A[i] % A[i-1] == 0:
            k = 0
            while A[i] % (2**k) == 0:
                k += 1
            A[i] = A[i-1] * (2**(k-1))
    for i in range(M):
        A[0] = A[0] // 2
    print(sum(A))
