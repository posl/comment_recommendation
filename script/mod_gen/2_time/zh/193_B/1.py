def main():
    print("请输入正常价格和折扣价格：")
    a,b = map(int,input().split())
    print("折扣率为：{:.2f}".format((a-b)/a*100))
main()
