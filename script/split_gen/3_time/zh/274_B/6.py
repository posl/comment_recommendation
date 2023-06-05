def get_input():
    #获取输入
    H, W = map(int, input().split())
    C = [input() for _ in range(H)]
    return H, W, C
