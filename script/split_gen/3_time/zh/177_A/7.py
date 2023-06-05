def main():
    # 读取输入
    D, T, S = map(int, input().split())
    # 判断是否能准时到达
    if D / S <= T:
        print('Yes')
    else:
        print('No')
