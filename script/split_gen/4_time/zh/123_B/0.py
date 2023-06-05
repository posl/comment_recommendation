def main():
    # 读入数据
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    # 计算最后一道菜的最早送达时间
    print((a+9)//10*10 + (b+9)//10*10 + (c+9)//10*10 + (d+9)//10*10 + (e+9)//10*10)
