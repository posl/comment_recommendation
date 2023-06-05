def main():
    #读取输入
    S_x, S_y, G_x, G_y = map(int, input().split())
    #计算
    x = (S_x*G_y + S_y*G_x)/(S_y + G_y)
    #输出
    print(x)
