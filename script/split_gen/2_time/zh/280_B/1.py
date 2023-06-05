def get_input():
    # 获取输入
    print("请输入H,W")
    h, w = map(int, input().split())
    print("请输入S_1, S_2, ..., S_H")
    s = []
    for i in range(h):
        s.append(input())
    return h, w, s
