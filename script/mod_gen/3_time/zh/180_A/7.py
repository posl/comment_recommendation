def main():
    print("请输入N A B:")
    N,A,B = map(int,input().split())
    if 100<=N<=200 and 1<=A<=100 and 1<=B<=100:
        print(N+A-B)
    else:
        print("输入的数值不符合条件！")

if __name__ == '__main__':
    main()