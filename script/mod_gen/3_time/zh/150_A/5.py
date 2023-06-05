def main():
    print("请输入硬币的个数和金钱数")
    k,x = map(int,input().split())
    if k*500 >= x:
        print("否")
    else:
        print("是")

if __name__ == '__main__':
    main()