def main():
    #读取数据
    n,x = map(int,input().split())
    x_list = list(map(int,input().split()))
    x_list.append(x)
    x_list.sort()
    #计算两个相邻城市的距离
    dis = []
    for i in range(n):
        dis.append(x_list[i+1]-x_list[i])
    #求最大公约数
    def gcd(a,b):
        if a<b:
            a,b = b,a
        while b!=0:
            a,b = b,a%b
        return a
    #求最大公约数的函数
    def gcd_list(numbers):
        return reduce(gcd,numbers)
    #求最大公约数
    print(gcd_list(dis))
