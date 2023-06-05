def main():
    n, x = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    a = [ab[i][0] for i in range(n)]
    b = [ab[i][1] for i in range(n)]
    # print(a)
    # print(b)
    # print(ab)
    # print(n)
    # print(x)
    # 二分探索
    left = 0
    right = 1000000000 * 1000000000
    while left < right:
        mid = (left + right) // 2
        # print("mid = ", mid)
        # print("left = ", left)
        # print("right = ", right)
        # print("check = ", check(mid, a, b, x))
        if check(mid, a, b, x):
            right = mid
        else:
            left = mid + 1
    print(left)
