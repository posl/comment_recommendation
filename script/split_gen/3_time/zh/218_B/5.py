def main():
    # 读入数据
    p = list(map(int, input().split()))
    # 生成字母表
    alphabet = list(map(chr, range(ord('a'), ord('z') + 1)))
    # 生成字典
    d = dict(zip(p, alphabet))
    # 输出
    for i in range(1, 27):
        print(d[i], end='')
