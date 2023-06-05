def main():
    #输入数据
    n = int(input())
    #s = input()
    s = []
    for i in range(n):
        s.append(input())
    #print(s)
    #print(s.count("For"))
    #print(s.count("Against"))
    if s.count("For") > s.count("Against"):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()