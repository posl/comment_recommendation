def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A = [a % M for a in A]
    # 累積和
    B = [0] * (N + 1)
    for i in range(N):
        B[i+1] = (B[i] + A[i]) % M
    # 累積和の値をキーにして、その値が出現するインデックスを保存する
    # 例えば、B = [0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4] のとき
    # C = {0: [0], 1: [1, 2, 3], 2: [4, 5, 6], 3: [7, 8, 9, 10], 4: [11, 12, 13]}
    C = {}
    for i, b in enumerate(B):
        if b in C:
            C[b].append(i)
        else:
            C[b] = [i]
    ans = 0
    for k, v in C.items():
        # 同じ値が出現するインデックスの差分を計算する
        # 例えば、B = [0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4] のとき
        # C = {0: [0], 1: [1, 2, 3], 2: [4, 5, 6], 3: [7, 8, 9, 10], 4: [11, 12, 13]}
        # のとき、v = [1, 2, 3] ならば、
        # 2 - 1 = 1
        # 3 - 2 = 1
        # 1 + 1 = 2
        # となり、2 が答えになる