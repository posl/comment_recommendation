def main():
    # 声明变量
    r = 0
    c = 0
    # 输入数据
    r, c = map(int, input().split())
    # 判断
    if (r + c) % 2 == 0:
