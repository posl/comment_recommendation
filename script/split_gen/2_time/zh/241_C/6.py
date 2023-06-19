def main():
    #输入数据
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    #判断是否有6x6的黑色正方形
    for i in range(n-5):
        for j in range(n-5):
            if s[i][j] == '#' and s[i+5][j] == '#' and s[i][j+5] == '#' and s[i+5][j+5] == '#' and s[i+1][j+1] == '#' and s[i+2][j+2] == '#' and s[i+3][j+3] == '#' and s[i+4][j+4] == '#' and s[i+1][j+4] == '#' and s[i+2][j+3] == '#' and s[i+3][j+2] == '#' and s[i+4][j+1] == '#':
                print("Yes")
                return
    print("No")
    return
