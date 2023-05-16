def main():
    N, M = map(int, input().split())
    balls = []
    for i in range(M):
        k = int(input())
        a = list(map(int, input().split()))
        balls.append(a)
    print(N, M)
    print(balls)
    # 2N 個のボールがあります。各ボールには 1 以上 N 以下の整数によって表される色が塗られており、各色で塗られたボールはちょうど 2 個ずつ存在します。
    # これらのボールが、底が地面と平行になるように置かれた M 本の筒に入れられています。はじめ、i  (1 ≦ i ≦ M) 本目の筒には k_i 個のボールが入っており、上から j  (1 ≦ j ≦ k_i) 番目のボールの色は a_{i, j} です。
    # あなたの目標は、以下の操作を繰り返すことで M 本の筒全てを空にすることです。
    # 異なる 2 本の空でない筒を選び、それぞれの筒の一番上にあるボールを取り出して捨てる。ここで、取り出して捨てた 2 つのボールは同じ色で塗られている必要がある。
    # 目標が達成可能かを判定してください。
    # 制約
    # 1 ≦ N ≦ 2 × 10^5
    # 2 ≦ M ≦ 2 × 10^5
    # 1 ≦ k_i (1 ≦ i ≦ M)
    # 1 ≦ a_{i,j} ≦ N (1 ≦ i ≦ M,1 ≦ j ≦ k_i)
    # sum_{i=1