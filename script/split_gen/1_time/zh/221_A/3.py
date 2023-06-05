def main():
    #print("请输入两个整数，中间用空格隔开")
    a,b = map(int,input().split())
    #print("a=",a,"b=",b)
    print(32**(a-b))
