def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a = [x-1 for x in a]
    x = []
    y = []
    for _ in range(n):
        xi, yi = map(int, input().split())
        x.append(xi)
        y.append(yi)
    # print(n, k)
    # print(a)
    # print(x)
    # print(y)
    # print()
    # 各人の明かりの強さの最小値を求める
    # 二分探索
    # 二分探索の範囲は 0 〜 10^5
    # 二分探索の中で、各人が明かりを持つかどうかを判定する
    # 明かりを持つ場合は、その明かりの強さを記録する
    # 明かりを持たない場合は、その明かりの強さを記録しない
    # 二分探索の終了時に、記録した明かりの強さの最大値が答え
    # 二分探索の終了時に、記録した明かりの強さの最大値が答え
    # このとき、各人が明かりを持つかどうかを判定するには、
    # 各人の座標と、各明かりの強さを用いて、
    # 各人が明かりを持つかどうかを判定するのに、
    # 各明かりの強さを用いて、
    # 各人が明かりを持つかどうかを判定するのに、
    # 各明かりの強さを用いて、
    # 各人が明かりを持つかどうかを判定するのに、
    # 各明かりの強さを用いて
