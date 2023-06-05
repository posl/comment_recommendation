def main():
    print("请输入一个整数：")
    n = int(input())
    if n < 0 or n > 10 ** 7:
        print("输入的数不在范围内")
        return
    print("需要的最少硬币数为：")
    print(coin(n))
