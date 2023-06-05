def get_input():
    # H:行数
    # W:列数
    # h:选择的行数
    # w:选择的列数
    H, W = map(int, input().split())
    h, w = map(int, input().split())
    return H, W, h, w

if __name__ == '__main__':
    get_input()