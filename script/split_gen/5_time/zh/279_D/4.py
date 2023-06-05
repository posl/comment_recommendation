def solve(A, B):
    import math
    def get_time(g):
        return A / math.sqrt(g) + B * math.log(g, math.e)
    def get_g(t):
        return 1 / (t / A - B)
    # 二分探索で解を求める
    # 解は必ず存在する
    left = 0
    right = 10 ** 18
    while right - left > 10 ** -6:
        mid = (left + right) / 2
        if get_time(get_g(mid)) > mid:
            left = mid
        else:
            right = mid
    return get_time(get_g(left))
A, B = map(int, input().split())
print(solve(A, B))
