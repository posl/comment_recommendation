def main():
    # 读入数据
    A,B,C,D,E,F,X = map(int,input().split())
    # 计算高桥走的距离
    T = 0
    disT = 0
    while T < X:
        if T % (A+C) < A:
            disT += B
        T += 1
    # 计算青木走的距离
    T = 0
    disA = 0
    while T < X:
        if T % (D+F) < D:
            disA += E
        T += 1
    # 判断谁走的距离多
    if disT > disA:
        prin
