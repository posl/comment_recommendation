def main():
    n = int(input())
    xy = [list(map(int, input().split())) for _ in range(n)]
    #print(xy)
    #print("-----")
    # 1. mを決める
    # 2. dを決める
    # 3. wを決める
    # 1. mを決める
    # mは、全てのxy座標の中で最大の座標の値を取る
    # ただし、最小値は1とする
    # つまり、最大値が10^9なら、mは10^9となる
    # また、最小値が-10^9なら、mは10^9となる
    # なお、mの最大値は40となる
    # 2. dを決める
    # dは、全てのxy座標の中で最大の座標の値を取る
    # ただし、最小値は1とする
    # つまり、最大値が10^9なら、dは10^9となる
    # また、最小値が-10^9なら、dは10^9となる
    # なお、dの最大値は10^12となる
    # 3. wを決める
    # wは、mの数だけ必要となる
    # wは、全てのxy座標の中で最大の座標の値を取る
    # ただし、最小値は1とする
    # つまり、最大値が10^9なら、wは10^9となる
    # また、最小値が-10^9なら、wは10^9となる
    # なお、wの最大値は40となる
    # 4. 1,2,3を満たすか確