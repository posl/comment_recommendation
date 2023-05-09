Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = [input() for _ in range(10)]
    a = 0
    b = 0
    c = 0
    d = 0
    for i in range(10):
        if s[i][0] == '#':
            a = i + 1
            break
    for i in range(10):
        if s[i][9] == '#':
            b = i + 1
            break
    for i in range(10):
        if s[0][i] == '#':
            c = i + 1
            break
    for i in range(10):
        if s[9][i] == '#':
            d = i + 1
            break
    print(a, b)
    print(c, d)

=======
Suggestion 2

def main():
    input = sys.stdin.readline
    S = [input().rstrip() for _ in range(10)]
    A, B, C, D = 0, 0, 0, 0
    for i in range(10):
        if '#' in S[i]:
            A = i
            break
    for i in range(9, -1, -1):
        if '#' in S[i]:
            B = i
            break
    for i in range(10):
        if '#' in [S[j][i] for j in range(10)]:
            C = i
            break
    for i in range(9, -1, -1):
        if '#' in [S[j][i] for j in range(10)]:
            D = i
            break
    print(A+1, B+1)
    print(C+1, D+1)

=======
Suggestion 3

def main():
    s = []
    for i in range(10):
        s.append(input())

    for i in range(10):
        if '#' in s[i]:
            a = i
            break

    for i in range(9,-1,-1):
        if '#' in s[i]:
            b = i
            break

    for i in range(10):
        if '#' in s[i]:
            c = s[i].index('#')
            break

    for i in range(9,-1,-1):
        if '#' in s[i]:
            d = s[i].rindex('#')
            break

    print(a+1,b+1)
    print(c+1,d+1)

=======
Suggestion 4

def main():
    S = [input() for i in range(10)]
    A = B = C = D = -1
    for i in range(10):
        if S[i].find('#') != -1:
            if A == -1:
                A = i + 1
            B = i + 1
            if C == -1:
                C = S[i].find('#') + 1
            D = max(D, S[i].rfind('#') + 1)
    print(A, B)
    print(C, D)

=======
Suggestion 5

def main():
    #input
    s = []
    for i in range(10):
        s.append(input())
    #compute
    a = 0
    b = 0
    c = 0
    d = 0
    for i in range(10):
        if s[i].find('#') == -1:
            continue
        else:
            a = i + 1
            break
    for i in range(9, -1, -1):
        if s[i].find('#') == -1:
            continue
        else:
            b = i + 1
            break
    for i in range(10):
        if s[i].find('#') == -1:
            continue
        else:
            for j in range(10):
                if s[i][j] == '#':
                    c = j + 1
                    break
            break
    for i in range(10):
        if s[i].find('#') == -1:
            continue
        else:
            for j in range(9, -1, -1):
                if s[i][j] == '#':
                    d = j + 1
                    break
            break
    #output
    print(a, b)
    print(c, d)

=======
Suggestion 6

def main():
    S = []
    for i in range(10):
        S.append(input())
    for i in range(10):
        if S[i].find("#") > -1:
            break
    A = i + 1
    for i in range(9, -1, -1):
        if S[i].find("#") > -1:
            break
    B = i + 1
    for i in range(10):
        if S[i].find("#") > -1:
            break
    C = S[i].find("#") + 1
    for i in range(9, -1, -1):
        if S[i].find("#") > -1:
            break
    D = S[i].rfind("#") + 1
    print(A, B)
    print(C, D)
    return

=======
Suggestion 7

def solve():
    s = [input() for _ in range(10)]
    for i in range(10):
        if s[i].count("#") == 1:
            a = i + 1
            break
    for i in range(9, -1, -1):
        if s[i].count("#") == 1:
            b = i + 1
            break
    for i in range(10):
        for j in range(10):
            if s[j][i] == "#":
                c = i + 1
                break
    for i in range(9, -1, -1):
        for j in range(10):
            if s[j][i] == "#":
                d = i + 1
                break
    print(a, b)
    print(c, d)
solve()

=======
Suggestion 8

def main():
    s = [input() for i in range(10)]
    #print(s)
    for i in range(10):
        if s[i].find('#') != -1:
            start = i
            break
    for i in range(9, -1, -1):
        if s[i].find('#') != -1:
            end = i
            break
    for i in range(10):
        if s[i].find('#') != -1:
            start2 = s[i].find('#')
            break
    for i in range(9, -1, -1):
        if s[i].find('#') != -1:
            end2 = s[i].rfind('#')
            break
    print(start+1, end+1)
    print(start2+1, end2+1)

=======
Suggestion 9

def get_input():
    S = []
    for i in range(10):
        S.append(input())
    return S

=======
Suggestion 10

def main():
    # input process
    S = [input() for i in range(10)]

    # process
    i = 0
    while i < 10:
        if S[i][0] == '.':
            i += 1
        else:
            break
    A = i+1

    i = 9
    while i >= 0:
        if S[i][9] == '.':
            i -= 1
        else:
            break
    B = i+1

    j = 0
    while j < 10:
        if S[0][j] == '.':
            j += 1
        else:
            break
    C = j+1

    j = 9
    while j >= 0:
        if S[9][j] == '.':
            j -= 1
        else:
            break
    D = j+1

    # output process
    print(A, B)
    print(C, D)
