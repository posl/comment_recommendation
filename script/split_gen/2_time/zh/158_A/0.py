def main():
    # 读入S
    S = input()
    # 初始化计数器
    count = 0
    # 循环统计S中B的个数
    for i in range(3):
        if S[i] == 'B':
            count += 1
    # 判断B的个数
    if count == 1 or count == 2:
        print('Yes')
    else:
        print('No')
