def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    # A_i の値を X_i にするために必要な操作の最小回数を求める
    # A_i から X_i までの距離を d とすると
    # d が偶数のときは d // 2 回の操作で A_i を X_i にできる
    # d が奇数のときは (d + 1) // 2 回の操作で A_i を X_i にできる
    # d は A_i と X_i の偶奇が異なるときに 1 大きくなる
    # 偶奇が同じときは 0 になる
    # d は A_i と X_i の偶奇が異なるときに A_i と X_i の差の半分になる
    # 偶奇が同じときは A_i と X_i の差になる
    # d は A_i と X_i の偶奇が異なるときに A_i と X_i の差の半分になる
    # 偶奇が同じときは A_i と X_i の差になる
    # A_i と X_i の偶奇が異なるときに A_i と X_i の差の半分になる
    # 偶奇が同じときは A_i と X_i の差になる
    # A_i と X_i の偶奇が異なるときに A_i と X_i の差の半分になる
    # 偶奇が

if __name__ == '__main__':
    main()