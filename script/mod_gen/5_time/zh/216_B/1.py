def main():
    print("请输入N的值：")
    N = int(input())
    print("请输入人名：")
    name = []
    for i in range(N):
        name.append(input())
    for i in range(N):
        for j in range(i+1,N):
            if name[i]==name[j]:
                print("Yes")
                return
    print("No")

if __name__ == '__main__':
    main()