def main():
    print("请输入H W")
    H,W = map(int,input().split())
    print("请输入迷宫")
    s = []
    for i in range(H):
        s.append(input())
    print(s)
    #print(s[0][0])
    #print(s[1][1])
    #print(s[2][2])
    #print(s[2][3])
    #print(s[2][4])
    #print(s[1][4])
    #print(s[0][4])
    #print(s[0][3])
    #print(s[0][2])
    print(s[0][0])
    print(s[0][1])
    print(s[0][2])
    print(s[1][2])
    print(s[2][2])
    print(s[2][1])
    print(s[2][0])
    print(s[1][0])
    print(s[1][1])
