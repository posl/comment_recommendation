Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a = []
    for i in range(10):
        a.append(input())
    for i in range(10):
        for j in range(10):
            if a[i][j] == '#':
                print(i+1,j+1)
                return

=======
Suggestion 2

def main():
    s = []
    for i in range(10):
        s.append(input())
    A, B, C, D = 0, 0, 0, 0
    for i in range(10):
        for j in range(10):
            if s[i][j] == '#':
                if A == 0:
                    A = i + 1
                if B < i + 1:
                    B = i + 1
                if C == 0:
                    C = j + 1
                if D < j + 1:
                    D = j + 1
    print(A, B)
    print(C, D)

=======
Suggestion 3

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

=======
Suggestion 4

def main():
    # 读取输入
    S = []
    for i in range(10):
        S.append(input())
    # print(S)
    # print(len(S[0]))
    # print(len(S))
    # print(S[1][1])
    # print(S[1][2])
    # print(S[1][3])
    # print(S[1][4])
    # print(S[1][5])
    # print(S[1][6])
    # print(S[1][7])
    # print(S[1][8])
    # print(S[1][9])
    # print(S[1][10])
    # print(S[1][11])
    # print(S[1][12])
    # print(S[1][13])
    # print(S[1][14])
    # print(S[1][15])
    # print(S[1][16])
    # print(S[1][17])
    # print(S[1][18])
    # print(S[1][19])
    # print(S[1][20])
    # print(S[1][21])
    # print(S[1][22])
    # print(S[1][23])
    # print(S[1][24])
    # print(S[1][25])
    # print(S[1][26])
    # print(S[1][27])
    # print(S[1][28])
    # print(S[1][29])
    # print(S[1][30])
    # print(S[1][31])
    # print(S[1][32])
    # print(S[1][33])
    # print(S[1][34])
    # print(S[1][35])
    # print(S[1][36])
    # print(S[1][37])
    # print(S[1][38])
    # print(S[1][39])
    # print(S[1][40])
    # print(S[1][41])
    # print(S[1][42])
    # print(S[1][43])
    # print(S[1][44])
    # print(S[1][45])
    # print(S[1][46])
    # print(S[1][47])
    # print(S[1][48])
    # print(S[1][49])
    # print(S[1][50])
    # print(S[

=======
Suggestion 5

def main():
    for i in range(10):
        s = input()
        if '#' in s:
            left = i + 1
            break
    for i in range(9, -1, -1):
        s = input()
        if '#' in s:
            right = i + 1
            break
    for i in range(10):
        s = input()
        if '#' in s:
            top = i + 1
            break
    for i in range(9, -1, -1):
        s = input()
        if '#' in s:
            bottom = i + 1
            break
    print(left, top)
    print(right, bottom)

=======
Suggestion 6

def main():
    a = []
    for i in range(10):
        a.append(input())
    for i in range(10):
        if a[0][i] == '#':
            x1 = i
            break
    for i in range(9, -1, -1):
        if a[9][i] == '#':
            x2 = i
            break
    for i in range(10):
        if a[i][0] == '#':
            y1 = i
            break
    for i in range(9, -1, -1):
        if a[i][9] == '#':
            y2 = i
            break
    print(y1+1, x1+1)
    print(y2+1, x2+1)

=======
Suggestion 7

def main():
    s = []
    for i in range(10):
        s.append(list(input()))

    for i in range(10):
        for j in range(10):
            if s[i][j] == '#':
                print(i + 1, j + 1)
                return

=======
Suggestion 8

def solve():
    S = []
    for i in range(10):
        S.append(input())
    for i in range(10):
        if S[i][0] == '#':
            A = i+1
            break
    for i in range(10):
        if S[i][9] == '#':
            B = i+1
    for i in range(10):
        if S[0][i] == '#':
            C = i+1
            break
    for i in range(10):
        if S[9][i] == '#':
            D = i+1
    print(A,B)
    print(C,D)
solve()

=======
Suggestion 9

def main():
    pass

=======
Suggestion 10

def main():
    s = []
    for i in range(10):
        s.append(list(input()))
    #print(s)
    for i in range(10):
        for j in range(10):
            if s[i][j] == "#":
                if i == 0:
                    a = i
                else:
                    a = i - 1
                if j == 0:
                    b = j
                else:
                    b = j - 1
                if i == 9:
                    c = i
                else:
                    c = i + 1
                if j == 9:
                    d = j
                else:
                    d = j + 1
                for k in range(a,c+1):
                    for l in range(b,d+1):
                        s[k][l] = "#"
    for i in range(10):
        print("".join(s[i]))
