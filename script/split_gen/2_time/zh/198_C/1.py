def main():
    # 读入数据
    r,x,y = map(int,input().split())
    # 计算距离
    distance = (x**2+y**2)**0.5
    # 计算步数
    if distance == r:
        print(1)
    elif distance <= 2*r:
        print(2)
    else:
        print(int(distance//r)+1)
