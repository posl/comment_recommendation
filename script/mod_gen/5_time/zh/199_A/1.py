def main():
    #读取输入
    a,b,c = map(int,input().split())
    #判断
    if a*a+b*b<c*c:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()