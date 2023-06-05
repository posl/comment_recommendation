def main():
    # 读入输入
    a,b,c = map(int,input().split())
    # 计算结果
    print(max(a*10+b+c,a+b*10+c,a+b+c*10))
