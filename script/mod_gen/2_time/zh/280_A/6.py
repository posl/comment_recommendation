def main():
    #输入
    h,w = map(int,input().split())
    s = []
    for i in range(h):
        s.append(input())
    #计算
    count = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                count += 1
    #输出
    print(count)

if __name__ == '__main__':
    main()