def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    BC = [list(map(int, input().split())) for _ in range(Q)]
    # 1. Aの値がBの個数を求める
    # 2. Aの値がBの個数をCに置き換える
    # 3. Aの合計を求める
    # 4. Aの合計を出力
    # 5. 1~4をQ回繰り返す
    for i in range(Q):
        # Aの値がBの個数を求める
        count = 0
        for j in range(N):
            if A[j] == BC[i][0]:
                count += 1
        # Aの値がBの個数をCに置き換える
        for j in range(N):
            if A[j] == BC[i][0]:
                A[j] = BC[i][1]
        # Aの合計を求める
        sum = 0
        for j in range(N):
            sum += A[j]
        # Aの合計を出力
        print(sum)
