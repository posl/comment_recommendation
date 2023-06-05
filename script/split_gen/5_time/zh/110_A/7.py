def main():
    # 读取数据
    a,b,c = map(int,input().split())
    # 计算结果
    result = max(a+b+c,(a+b)*c,a*(b+c),a*b*c)
    # 输出结果
    print(result)
