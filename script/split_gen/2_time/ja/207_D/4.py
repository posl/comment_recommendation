def main():
    N = int(input())
    S = []
    T = []
    for _ in range(N):
        S.append([int(i) for i in input().split()])
    for _ in range(N):
        T.append([int(i) for i in input().split()])
    #print(S)
    #print(T)
    
    # まずは回転と移動を行う
    # まずは回転を行う
    # まずは時計回りに270度回転させる
    # 回転行列を用いる
    # 回転行列は
    # | cosθ -sinθ |
    # | sinθ  cosθ |
    # となる
    # 今回は時計回りに270度回転させるので、
    # | cosθ -sinθ |
    # | sinθ  cosθ |
    # となる
    # これをSにかける
    # 今回は時計回りに270度回転させるので、
    # | 0 -1 |
    # | 1  0 |
    # となる
    # これをSにかける
    # これをTにかける
    # これをTにかける
    # これをSにかける
    # これをSにかける
    # これをTにかける
    # これをTにかける
    # これをSにかける
    # これをSにかける
    # これをTにかける
    # これをTにかける
    # これをSにかける
    # これをSにかける
    # これをTにかける
    # これをTにかける
    # これをSにかける
    # これをSにかける
    # これをTにかける
    # これをTにかける
    # これをSにかけ
