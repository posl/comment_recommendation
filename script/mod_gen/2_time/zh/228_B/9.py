def main():
    # 读入数据
    s,t,x = map(int,input().split())
    # 处理数据
    if x > s and x < t:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()