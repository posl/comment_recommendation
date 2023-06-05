def main():
    #输入
    s = []
    for i in range(10):
        s.append(input())
    #计算
    a = 0
    b = 0
    c = 0
    d = 0
    for i in range(10):
        if '#' in s[i]:
            if a == 0:
                a = i + 1
            else:
                b = i + 1
            for j in range(10):
                if s[i][j] == '#':
                    if c == 0:
                        c = j + 1
                    else:
                        d = j + 1
    #输出
    print(a, b)
    print(c, d)
