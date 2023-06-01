Synthesizing 10/10 solutions

=======
Suggestion 1

def get_input():
    x = input()
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    return x, n, s

=======
Suggestion 2

def main():
    x = input()
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    for i in range(n):
        s[i] = s[i].translate(str.maketrans(x, 'abcdefghijklmnopqrstuvwxyz'))
    s.sort()
    for i in range(n):
        s[i] = s[i].translate(str.maketrans('abcdefghijklmnopqrstuvwxyz', x))
    print(*s, sep='\n')
    return

=======
Suggestion 3

def str2int(str):
    int = 0
    for s in str:
        int = int * 26 + ord(s) - ord('a')
    return int

=======
Suggestion 4

def get_order():
    return input()

=======
Suggestion 5

def main():
    x = input()
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort(key=lambda x: [x.index(c) for c in x])
    s.sort(key=lambda x: [x.index(c) for c in x], reverse=True)
    print(s)
    print(x)
    print(n)
    print(s)

=======
Suggestion 6

def main():
    #print("请输入字母表顺序：")
    #x = input()
    #print("请输入人数：")
    #n = int(input())
    #print("请输入人名：")
    #s = []
    #for i in range(n):
    #    s.append(input())
    #print("字母表顺序为：",x)
    #print("人数为：",n)
    #print("人名为：",s)
    x = "bacdefghijklmnopqrstuvwxzy"
    n = 4
    s = ["abx","bzz","bzy","caa"]
    #x = "zyxwvutsrqponmlkjihgfedcba"
    #n = 5
    #s = ["a","ab","abc","ac","b"]
    #x = "abcdefghijklmnopqrstuvwxyz"
    #n = 2
    #s = ["ac","ab"]
    #x = "zyxwvutsrqponmlkjihgfedcba"
    #n = 2
    #s = ["ac","ab"]
    #x = "zyxwvutsrqponmlkjihgfedcba"
    #n = 2
    #s = ["ab","ac"]
    #x = "zyxwvutsrqponmlkjihgfedcba"
    #n = 3
    #s = ["ab","ac","abc"]
    #x = "zyxwvutsrqponmlkjihgfedcba"
    #n = 3
    #s = ["abc","ab","ac"]
    #x = "zyxwvutsrqponmlkjihgfedcba"
    #n = 3
    #s = ["abc","ac","ab"]
    #x = "zyxwvutsrqponmlkjihgfedcba"
    #n = 3
    #s = ["ac","abc","ab"]
    #x = "zyxwvutsrqponmlkjihgfedcba"
    #n = 3
    #s = ["ac","ab","abc"]
    #x = "zyxwvutsrqponmlkjihgfedcba"
    #n = 3
    #s = ["ab","abc","ac"]
    #x =

=======
Suggestion 7

def main():
    x = input()
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    #print(x)
    #print(n)
    #print(s)
    d = {}
    for i in range(len(x)):
        d[x[i]] = i
    #print(d)
    s.sort(key = lambda x: [d[c] for c in x])
    for i in s:
        print(i)

=======
Suggestion 8

def main():
    X = input()
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    X = list(X)
    X.sort()
    X = ''.join(X)
    X = X[::-1]
    S.sort(key = lambda x:X.index(x[0]))
    S.sort(key = lambda x:X.index(x[1]))
    S.sort(key = lambda x:X.index(x[2]))
    S.sort(key = lambda x:X.index(x[3]))
    S.sort(key = lambda x:X.index(x[4]))
    S.sort(key = lambda x:X.index(x[5]))
    S.sort(key = lambda x:X.index(x[6]))
    S.sort(key = lambda x:X.index(x[7]))
    S.sort(key = lambda x:X.index(x[8]))
    S.sort(key = lambda x:X.index(x[9]))
    S.sort(key = lambda x:X.index(x[10]))
    S.sort(key = lambda x:X.index(x[11]))
    S.sort(key = lambda x:X.index(x[12]))
    S.sort(key = lambda x:X.index(x[13]))
    S.sort(key = lambda x:X.index(x[14]))
    S.sort(key = lambda x:X.index(x[15]))
    S.sort(key = lambda x:X.index(x[16]))
    S.sort(key = lambda x:X.index(x[17]))
    S.sort(key = lambda x:X.index(x[18]))
    S.sort(key = lambda x:X.index(x[19]))
    S.sort(key = lambda x:X.index(x[20]))
    S.sort(key = lambda x:X.index(x[21]))
    S.sort(key = lambda x:X.index(x[22]))
    S.sort(key = lambda x:X.index(x[23]))
    S.sort(key = lambda x:X.index(x[24]))
    S.sort(key = lambda x:X.index(x[25]))
    for i in range(N):
        print(S[i])

=======
Suggestion 9

def main():
    # 读取输入
    x = raw_input()
    n = int(raw_input())
    s = []
    for i in range(n):
        s.append(raw_input())
    # 解决问题
    # 排序
    # 用一个字典来存储字母和新字母的映射
    x_dict = {}
    for i in range(26):
        x_dict[x[i]] = chr(ord('a')+i)
    # 用一个字典来存储新字母和字母的映射
    x_dict_reverse = {}
    for i in range(26):
        x_dict_reverse[chr(ord('a')+i)] = x[i]
    # 用一个字典来存储字符串和新字符串的映射
    s_dict = {}
    for i in range(n):
        s_dict[s[i]] = ''
        for j in range(len(s[i])):
            s_dict[s[i]] += x_dict[s[i][j]]
    # 排序
    s_dict_sorted = sorted(s_dict.items(), key=lambda d:d[1])
    # 输出
    for i in range(n):
        print s_dict_sorted[i][0]

=======
Suggestion 10

def main():
    x = input()
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort(key = lambda a: [x.index(c) for c in a])
    for i in s:
        print(i)
