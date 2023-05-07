def main():
    A, B, H, M = map(int, input().split())
    # 1時間あたりの角度の変化量
    theta_H = 360 / 12
    # 1分あたりの角度の変化量
    theta_M = 360 / 60
    # 時針の角度
    theta_H = theta_H * H + theta_H * M / 60
    # 分針の角度
    theta_M = theta_M * M
    # 2つの針の角度の差
    theta = abs(theta_H - theta_M)
    # 三角関数の関係より、
    # cosθ = (a^2 + b^2 - c^2) / (2ab)
    # となるので、
    # c = sqrt(a^2 + b^2 - 2abcosθ)
    # となる。
    # ただし、cは2つの針の長さの差、ここではCとする。
    # また、CはAとBの2つの値に依存するので、
    # C = sqrt(A^2 + B^2 - 2ABcosθ)
    # となる。
    # これを実装すると以下のようになる。
    # ただし、Cは実数なので、小数点以下の計算が必要になる。
    # そのため、mathモジュールをimportしている。
    # また、Cは実数なので、小数点以下の計算が必要になる。
    # そのため、mathモジュールをimportしている。
    import math
    C = math.sqrt(A**2 + B**2 - 2 * A * B * math.cos(math.radians(theta)))
    # 小数点以下の計算が必要なので、
    # print関数は使わず、
    # format関数を使って小数点以下の桁数を指定している。
    print(format(C, '.20f'))

if __name__ == '__main__':
    main()