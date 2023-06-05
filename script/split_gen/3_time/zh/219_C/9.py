def main():
    #输入
    x = input()
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    #处理
    y = list(x)
    y.sort()
    d = {}
    for i in range(26):
        d[y[i]] = chr(ord('a') + i)
    for i in range(n):
        s[i] = s[i].translate(str.maketrans(d))
    s.sort()
    for i in range(n):
        s[i] = s[i].translate(str.maketrans(d))
    #输出
    for i in range(n):
        print(s[i])
