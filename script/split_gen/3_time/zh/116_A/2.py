def main():
    #读取输入数据
    a,b,c = map(int, input().split())
    #计算三角形面积
    s = a * b / 2
    #输出结果
    print(int(s))
