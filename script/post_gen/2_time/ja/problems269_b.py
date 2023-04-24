Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = []
    for i in range(10):
        S.append(input())
    A = 0
    B = 0
    C = 0
    D = 0
    for i in range(10):
        if S[i].find('#') != -1:
            A = i + 1
            break
    for i in range(10):
        if S[9-i].find('#') != -1:
            B = 10 - i
            break
    for i in range(10):
        if S[0][i] == '#':
            C = i + 1
            break
    for i in range(10):
        if S[0][9-i] == '#':
            D = 10 - i
            break
    print(A, B)
    print(C, D)

=======
Suggestion 2

def main():
    S = []
    for i in range(10):
        S.append(input())
    A = 0
    B = 0
    C = 0
    D = 0
    for i in range(10):
        for j in range(10):
            if S[i][j] == "#":
                if A == 0:
                    A = i + 1
                if B < i + 1:
                    B = i + 1
                if C == 0:
                    C = j + 1
                if D < j + 1:
                    D = j + 1
    print(A,B)
    print(C,D)

=======
Suggestion 3

def main():
    s = []
    for i in range(10):
        s.append(input())
    a = 0
    b = 0
    c = 0
    d = 0
    for i in range(10):
        for j in range(10):
            if s[i][j] == '#':
                if a == 0:
                    a = i + 1
                else:
                    b = i + 1
                if c == 0:
                    c = j + 1
                else:
                    d = j + 1
    print(a, b)
    print(c, d)

=======
Suggestion 4

def main():
    S = [input() for i in range(10)]
    A = 1
    B = 10
    C = 1
    D = 10
    for i in range(10):
        if S[i] == "..........":
            A += 1
        else:
            break
    for i in range(10):
        if S[9-i] == "..........":
            B -= 1
        else:
            break
    for i in range(10):
        if S[0][i] == ".":
            C += 1
        else:
            break
    for i in range(10):
        if S[0][9-i] == ".":
            D -= 1
        else:
            break
    print(A,B)
    print(C,D)

=======
Suggestion 5

def main():
    S = [input() for i in range(10)]
    A = 0
    B = 0
    C = 0
    D = 0
    for i in range(10):
        if S[i][0] == '#':
            A = i+1
            break
    for i in range(10):
        if S[9-i][0] == '#':
            B = 10-i
            break
    for j in range(10):
        if S[0][j] == '#':
            C = j+1
            break
    for j in range(10):
        if S[0][9-j] == '#':
            D = 10-j
            break
    print(A,B)
    print(C,D)

=======
Suggestion 6

def main():
    S = [input() for i in range(10)]
    A = 1
    B = 10
    C = 1
    D = 10
    for i in range(10):
        if S[i][0] == '#':
            A = i+1
            break
    for i in range(10):
        if S[i][9] == '#':
            B = i+1
            break
    for i in range(10):
        if S[0][i] == '#':
            C = i+1
            break
    for i in range(10):
        if S[9][i] == '#':
            D = i+1
            break
    print(A, B)
    print(C, D)

=======
Suggestion 7

def main():
    s = [list(input()) for _ in range(10)]
    a = b = c = d = 0
    for i in range(10):
        for j in range(10):
            if s[i][j] == "#":
                if a == 0:
                    a = i + 1
                b = i + 1
                if c == 0:
                    c = j + 1
                d = j + 1
    print(a, b)
    print(c, d)

=======
Suggestion 8

def solve():
    S = [input() for _ in range(10)]
    A = B = C = D = 0
    for i in range(10):
        if S[i].count("#") > 0:
            if A == 0:
                A = i + 1
            B = i + 1
            for j in range(10):
                if S[i][j] == "#":
                    if C == 0:
                        C = j + 1
                    D = j + 1
    print(A, B)
    print(C, D)

=======
Suggestion 9

def main():
    S = []
    for i in range(10):
        S.append(input())
    print(1,10)
    print(1,10)
    return

=======
Suggestion 10

def main():
    #入力
    S = []
    for i in range(10):
        S.append(input())
    #print(S)
    #print(S[0])

    #処理
    #まず、 S_i (1 ≦ i ≦ 10)= .......... ( . が 10 個並んだ文字列) とする。
    #次に、以下の条件を全て満たす 4 つの整数 A,B,C,D を選ぶ。
    #1 ≦ A ≦ B ≦ 10
    #1 ≦ C ≦ D ≦ 10
    #その後、以下の条件を全て満たす全ての整数組 (i,j) について、 S_i の j 文字目を # に書き換える。
    #A ≦ i ≦ B
    #C ≦ j ≦ D
    #print(S[0][0])
    #print(S[0][1])
    #print(S[0][2])
    #print(S[0][3])
    #print(S[0][4])
    #print(S[0][5])
    #print(S[0][6])
    #print(S[0][7])
    #print(S[0][8])
    #print(S[0][9])

    #A,B,C,Dを決定
    A = 0
    B = 0
    C = 0
    D = 0
    for i in range(10):
        for j in range(10):
            if(S[i][j] == "#"):
                if(A == 0):
                    A = i + 1
                if(B < i + 1):
                    B = i + 1
                if(C == 0):
                    C = j + 1
                if(D < j + 1):
                    D = j + 1

    #出力
    print(A,B)
    print(C,D)
