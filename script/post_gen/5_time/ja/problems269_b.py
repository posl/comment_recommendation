Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    # 1行目の入力を受け取って出力する
    #print(input())
    #print(inp

=======
Suggestion 2

def main():
    # 入力
    s = []
    for i in range(10):
        s.append(input())
    # 処理
    a = 0
    b = 0
    c = 0
    d = 0
    for i in range(10):
        for j in range(10):
            if s[i][j] == '#':
                if a == 0:
                    a = i + 1
                if b < i + 1:
                    b = i + 1
                if c == 0:
                    c = j + 1
                if d < j + 1:
                    d = j + 1
    # 出力
    print(a, b)
    print(c, d)

=======
Suggestion 3

def main():
    # input
    S = [input() for i in range(10)]
    # compute
    A, B, C, D = 0, 0, 0, 0
    for i in range(10):
        for j in range(10):
            if S[i][j] == '#':
                if A == 0:
                    A = i+1
                if C == 0:
                    C = j+1
                B = i+1
                D = j+1
    # output
    print(A, B)
    print(C, D)

=======
Suggestion 4

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
            if S[i][j] == '#':
                A = i
                break
        if A != 0:
            break
    for i in range(9,-1,-1):
        for j in range(9,-1,-1):
            if S[i][j] == '#':
                B = i
                break
        if B != 0:
            break
    for i in range(10):
        for j in range(10):
            if S[j][i] == '#':
                C = i
                break
        if C != 0:
            break
    for i in range(9,-1,-1):
        for j in range(9,-1,-1):
            if S[j][i] == '#':
                D = i
                break
        if D != 0:
            break
    print(A+1,B+1)
    print(C+1,D+1)

=======
Suggestion 5

def main():
    # 文字列の入力
    s = []
    for i in range(10):
        s.append(input())
    # print(s)

    # 1行目の文字列を基準にする
    # 1行目の文字列の中で最初に出現する#の位置をstartに保存する
    for i in range(10):
        if s[0][i] == '#':
            start = i
            break
    # print(start)

    # 1行目の文字列の中で最後に出現する#の位置をendに保存する
    for i in range(9, -1, -1):
        if s[0][i] == '#':
            end = i
            break
    # print(end)

    # 1行目の文字列の中の#の数を数えてcountに保存する
    count = 0
    for i in range(10):
        if s[0][i] == '#':
            count += 1
    # print(count)

    # 1行目の文字列の中の#の数が1個の場合
    if count == 1:
        print('1 1')
        print('1 1')
        exit()

    # 1行目の文字列の中の#の数が2個以上の場合
    # 1行目の文字列の中で最初に出現する#の位置と最後に出現する#の位置の差をdiffに保存する
    diff = end - start
    # print(diff)

    # 1行目の文字列の中の#の数が2個以上の場合
    # 1行目の文字列の中で最初に出現する#の位置と最後に出現する#の位置の差が1の場合
    if diff == 1:
        # 1行目の文字列の中で最初に出現する#の位置が1の場合
        if start == 1:
            # 1行目の文字列の中で最後に出現する#の位置が8の場合
            if end ==

=======
Suggestion 6

def main():
    s = [input() for _ in range(10)]
    #print(s)
    for i in range(10):
        if s[i].count('#') >= 2:
            a = i
            break
    for i in range(9, -1, -1):
        if s[i].count('#') >= 2:
            b = i
            break
    for i in range(10):
        if '#' in [s[j][i] for j in range(10)]:
            c = i
            break
    for i in range(9, -1, -1):
        if '#' in [s[j][i] for j in range(10)]:
            d = i
            break
    print(a+1, b+1)
    print(c+1, d+1)

=======
Suggestion 7

def main():
    s = []
    for i in range(10):
        s.append(input())

    #print(s)
    #print(s[0][0])
    #print(s[0][1])

    #print(s[9][0])
    #print(s[9][1])
    #print(s[9][2])
    #print(s[9][3])
    #print(s[9][4])
    #print(s[9][5])
    #print(s[9][6])
    #print(s[9][7])
    #print(s[9][8])
    #print(s[9][9])

    #print(s[0][0])
    #print(s[1][0])
    #print(s[2][0])
    #print(s[3][0])
    #print(s[4][0])
    #print(s[5][0])
    #print(s[6][0])
    #print(s[7][0])
    #print(s[8][0])
    #print(s[9][0])

    #print(s[0][9])
    #print(s[1][9])
    #print(s[2][9])
    #print(s[3][9])
    #print(s[4][9])
    #print(s[5][9])
    #print(s[6][9])
    #print(s[7][9])
    #print(s[8][9])
    #print(s[9][9])

    #print(s[0][0])
    #print(s[0][1])
    #print(s[0][2])
    #print(s[0][3])
    #print(s[0][4])
    #print(s[0][5])
    #print(s[0][6])
    #print(s[0][7])
    #print(s[0][8])
    #print(s[0][9])

    #print(s[9][0])
    #print(s[9][1])
    #print(s[9][2])
    #print(s[9][3])
    #print(s[9][4])
    #print(s[9][5])
    #print(s[9][6])
    #print(s[9][7])
    #print(s[9][8])
    #print(s[9][9])

    #print(s[0][0

=======
Suggestion 8

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
                    B = i + 1
                    C = j + 1
                    D = j + 1
                else:
                    if i + 1 < A:
                        A = i + 1
                    if i + 1 > B:
                        B = i + 1
                    if j + 1 < C:
                        C = j + 1
                    if j + 1 > D:
                        D = j + 1

    print(A, D)
    print(B, C)

=======
Suggestion 9

def main():
    # input
    S = [list(input()) for _ in range(10)]

    # compute
    for i in range(10):
        for j in range(10):
            if S[i][j] == '#':
                if i == 0:
                    if j == 0:
                        S[i][j] = 'A'
                    elif j == 9:
                        S[i][j] = 'C'
                    else:
                        S[i][j] = 'B'
                elif i == 9:
                    if j == 0:
                        S[i][j] = 'G'
                    elif j == 9:
                        S[i][j] = 'I'
                    else:
                        S[i][j] = 'H'
                else:
                    if j == 0:
                        S[i][j] = 'D'
                    elif j == 9:
                        S[i][j] = 'F'
                    else:
                        S[i][j] = 'E'

    # output
    for i in range(10):
        print(''.join(S[i]))
