Synthesizing 10/10 solutions

=======
Suggestion 1

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
                    a = i
                if b == 0:
                    b = i
                if c == 0:
                    c = j
                if d == 0:
                    d = j
                if i < a:
                    a = i
                if i > b:
                    b = i
                if j < c:
                    c = j
                if j > d:
                    d = j
    print(a+1, b+1)
    print(c+1, d+1)

=======
Suggestion 2

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
            if s[i][j] == "#":
                if a == 0:
                    a = i
                if b < i:
                    b = i
                if c == 0:
                    c = j
                if d < j:
                    d = j
    print(a+1, b+1)
    print(c+1, d+1)

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
        if s[i].find('#') != -1:
            if a == 0:
                a = i + 1
            else:
                b = i + 1
            if s[i].find('#') == 0:
                c = 1
            else:
                c = s[i].find('#') + 1
            if s[i].rfind('#') == 9:
                d = 10
            else:
                d = s[i].rfind('#') + 1
    print(a, b)
    print(c, d)

=======
Suggestion 4

def main():
    s = []
    for i in range(10):
        s.append(list(input()))
    for i in range(10):
        for j in range(10):
            if s[i][j] == "#":
                s[i][j] = 1
            else:
                s[i][j] = 0
    a = 0
    b = 0
    c = 0
    d = 0
    for i in range(10):
        for j in range(10):
            if s[i][j] == 1:
                a = i
                break
        if a != 0:
            break
    for i in range(10):
        for j in range(9,-1,-1):
            if s[i][j] == 1:
                b = i
                break
        if b != 0:
            break
    for i in range(10):
        for j in range(10):
            if s[j][i] == 1:
                c = i
                break
        if c != 0:
            break
    for i in range(10):
        for j in range(9,-1,-1):
            if s[j][i] == 1:
                d = i
                break
        if d != 0:
            break
    print(c+1,d+1)
    print(a+1,b+1)

=======
Suggestion 5

def main():
    s = []
    for i in range(10):
        s.append(input())
    for i in range(10):
        if "#" in s[i]:
            a = i
            break
    for i in range(9, -1, -1):
        if "#" in s[i]:
            b = i
            break
    for i in range(10):
        if "#" in [s[j][i] for j in range(10)]:
            c = i
            break
    for i in range(9, -1, -1):
        if "#" in [s[j][i] for j in range(10)]:
            d = i
            break
    print(a + 1, b + 1)
    print(c + 1, d + 1)

=======
Suggestion 6

def main():
    S = []
    for i in range(10):
        S.append(input())
    for i in range(10):
        S[i] = list(S[i])
    #print(S)
    for i in range(10):
        for j in range(10):
            if S[i][j] == "#":
                S[i][j] = "O"
    #print(S)
    A = 0
    B = 0
    C = 0
    D = 0
    for i in range(10):
        for j in range(10):
            if S[i][j] == "O":
                A = i+1
                break
        if A != 0:
            break
    for i in range(9, -1, -1):
        for j in range(9, -1, -1):
            if S[i][j] == "O":
                B = i+1
                break
        if B != 0:
            break
    for j in range(10):
        for i in range(10):
            if S[i][j] == "O":
                C = j+1
                break
        if C != 0:
            break
    for j in range(9, -1, -1):
        for i in range(9, -1, -1):
            if S[i][j] == "O":
                D = j+1
                break
        if D != 0:
            break
    print(A, B)
    print(C, D)

=======
Suggestion 7

def main():
    s = []
    for i in range(10):
        s.append(input())
    for i in range(10):
        if s[i].find('#') != -1:
            a = i
            break
    for i in range(9, -1, -1):
        if s[i].find('#') != -1:
            b = i
            break
    for i in range(10):
        if s[i].find('#') != -1:
            c = s[i].find('#')
            d = s[i].rfind('#')
            break
    print(str(a+1) + ' ' + str(b+1))
    print(str(c+1) + ' ' + str(d+1))

=======
Suggestion 8

def main():
    strings = []
    for i in range(10):
        strings.append(input())
    #print(strings)

    for i in range(10):
        for j in range(10):
            if strings[i][j] == '#':
                print(i+1,j+1)
                exit()

=======
Suggestion 9

def solve():
    S = []
    for _ in range(10):
        S.append(input())

    for i in range(10):
        if '#' in S[i]:
            break

    A = i + 1

    for i in range(10):
        if '#' in S[9-i]:
            break

    B = 10 - i

    for i in range(10):
        if '#' in [S[j][i] for j in range(10)]:
            break

    C = i + 1

    for i in range(10):
        if '#' in [S[j][9-i] for j in range(10)]:
            break

    D = 10 - i

    print(A, B)
    print(C, D)

=======
Suggestion 10

def main():
    # input
    s = []
    for i in range(10):
        s.append(input())
    # compute
    row = [0] * 10
    col = [0] * 10
    for i in range(10):
        for j in range(10):
            if s[i][j] == '#':
                row[i] += 1
                col[j] += 1
    max_row = max(row)
    max_col = max(col)
    # output
    print(max_row, max_col)
