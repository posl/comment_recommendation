def main():
    # 读取输入
    N = int(input())
    T = list(map(int, input().split()))
    # 通过排序，从大到小排列
    T.sort(reverse=True)
    # 用两个烤箱
    oven1 = 0
    oven2 = 0
    for i in range(N):
        if oven1 < oven2:
            oven1 += T[i]
        else:
            oven2 += T[i]
    print(max(oven1, oven2))
