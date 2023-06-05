def main():
    #定义变量
    AB = 0
    BC = 0
    CA = 0
    #输入变量
    AB,BC,CA = map(int,input().split())
    #计算面积
    area = int(AB * BC / 2)
    #输出结果
    print(area)
