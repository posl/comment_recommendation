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
        if S[i] == '..........':
            A = i + 1
            B = i + 1
            break
    for i in range(10):
        if S[i] == '##########':
            B = i + 1
            break
    for i in range(10):
        for j in range(10):
            if S[i][j] == '#':
                C = j + 1
                break
        if C != 0:
            break
    for i in range(10):
        for j in range(10):
            if S[i][j] == '#':
                D = j + 1
    print(A,B)
    print(C,D)

=======
Suggestion 2

def main():
    s = [input() for _ in range(10)]
    a = b = c = d = 0
    for i in range(10):
        for j in range(10):
            if s[i][j] == "#":
                a, b, c, d = i + 1, i + 1, j + 1, j + 1
    for i in range(10):
        for j in range(10):
            if s[i][j] == "#":
                a = min(a, i + 1)
                b = max(b, i + 1)
                c = min(c, j + 1)
                d = max(d, j + 1)
    print(a, b)
    print(c, d)

=======
Suggestion 3

def main():
    S = []
    for i in range(10):
        S.append(input())
    A = -1
    B = -1
    C = -1
    D = -1
    for i in range(10):
        for j in range(10):
            if S[i][j] == "#":
                if A == -1:
                    A = i + 1
                if C == -1:
                    C = j + 1
                if A != -1 and B == -1:
                    B = i + 1
                if C != -1 and D == -1:
                    D = j + 1
    print(A,B)
    print(C,D)

=======
Suggestion 4

def main():
    S = [input() for _ in range(10)]
    A = 1
    B = 10
    C = 1
    D = 10
    for i in range(10):
        if S[i][0] == "#":
            A = i+1
            break
    for i in range(10):
        if S[i][9] == "#":
            B = i+1
            break
    for j in range(10):
        if S[0][j] == "#":
            C = j+1
            break
    for j in range(10):
        if S[9][j] == "#":
            D = j+1
            break
    print(A,B)
    print(C,D)

=======
Suggestion 5

def main():
    S = [input() for _ in range(10)]
    A = [0] * 10
    B = [0] * 10
    C = [0] * 10
    D = [0] * 10
    for i in range(10):
        for j in range(10):
            if S[i][j] == '#':
                A[i] = j + 1
                break
        for j in range(10):
            if S[i][9 - j] == '#':
                B[i] = 10 - j
                break
    for j in range(10):
        for i in range(10):
            if S[i][j] == '#':
                C[j] = i + 1
                break
        for i in range(10):
            if S[9 - i][j] == '#':
                D[j] = 10 - i
                break
    print(max(A), min(B))
    print(max(C), min(D))

=======
Suggestion 6

def main():
    S = [input() for _ in range(10)]
    A = 0
    B = 0
    C = 0
    D = 0
    for i in range(10):
        if S[i].count("#") != 0:
            A = i + 1
            break
    for i in range(10):
        if S[i].count("#") != 0:
            B = i + 1
    for i in range(10):
        if S[0][i] == "#":
            C = i + 1
            break
    for i in range(10):
        if S[0][i] == "#":
            D = i + 1
    print(A, B)
    print(C, D)

=======
Suggestion 7

def main():
    #入力
    #S_1,S_2,...,S_{10} は問題文中の方法で生成されうるそれぞれ長さ 10 の文字列
    S = []
    for i in range(10):
        S.append(input())

    #A,B,C,Dを求める
    A = 0
    B = 0
    C = 0
    D = 0
    for i in range(10):
        for j in range(10):
            if S[i][j] == '#':
                if A == 0:
                    A = i + 1
                    C = j + 1
                B = i + 1
                D = j + 1

    #出力
    print(A,B)
    print(C,D)

=======
Suggestion 8

def main():
    S = [input() for _ in range(10)]
    A, B, C, D = 1, 10, 1, 10
    for i in range(10):
        if S[i].count(".") == 10:
            A = i + 1
        if S[i].count("#") == 10:
            B = i
    for i in range(10):
        if S[0][i] == ".":
            C = i + 1
        if S[0][i] == "#":
            D = i
    print(A, B)
    print(C, D)

=======
Suggestion 9

def main():
    S = []
    for _ in range(10):
        S.append(input())

    A = 1
    B = 10
    C = 1
    D = 10
    for i in range(10):
        if S[i].count('#') == 0:
            A += 1
        else:
            break
    for i in range(10):
        if S[9-i].count('#') == 0:
            B -= 1
        else:
            break
    for i in range(10):
        if S[0][i] == '#':
            C += 1
        else:
            break
    for i in range(10):
        if S[0][9-i] == '#':
            D -= 1
        else:
            break
    print(A, B)
    print(C, D)

=======
Suggestion 10

def main():
    #入力
    s = []
    for i in range(10):
        s.append(input())
    #print(s)

    #処理
    a = 0
    b = 0
    c = 0
    d = 0
    for i in range(10):
        for j in range(10):
            if s[i][j] == "#":
                a = i + 1
                break
        if a > 0:
            break
    for i in range(10):
        for j in range(10):
            if s[9-i][9-j] == "#":
                b = 10 - i
                break
        if b > 0:
            break
    for i in range(10):
        for j in range(10):
            if s[j][i] == "#":
                c = i + 1
                break
        if c > 0:
            break
    for i in range(10):
        for j in range(10):
            if s[9-j][9-i] == "#":
                d = 10 - i
                break
        if d > 0:
            break

    #出力
    print(a,b)
    print(c,d)

main()
