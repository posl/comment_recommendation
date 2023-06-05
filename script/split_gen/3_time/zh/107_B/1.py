def get_input():
    # 获取输入
    H, W = map(int, input().split())
    a = []
    for i in range(H):
        a.append(input())
    return H, W, a
