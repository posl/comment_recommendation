Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = [input() for _ in range(10)]
    A = 10
    B = 1
    C = 10
    D = 1
    for i in range(10):
        for j in range(10):
            if S[i][j] == "#":
                A = min(A, i + 1)
                B = max(B, i + 1)
                C = min(C, j + 1)
                D = max(D, j + 1)
    print(A, B)
    print(C, D)

=======
Suggestion 2

def main():
    S = [input() for _ in range(10)]
    A = 10
    B = 1
    C = 10
    D = 1
    for i in range(10):
        for j in range(10):
            if S[i][j] == '#':
                A = min(A, i + 1)
                B = max(B, i + 1)
                C = min(C, j + 1)
                D = max(D, j + 1)
    print(A, B)
    print(C, D)

=======
Suggestion 3

def main():
    S = []
    for i in range(10):
        S.append(input())
    A = 0
    B = 0
    C = 0
    D = 0
    for i in range(10):
        if S[i] == ".........":
            continue
        else:
            A = i + 1
            break
    for i in range(10):
        if S[9 - i] == ".........":
            continue
        else:
            B = 10 - i
            break
    for i in range(10):
        if S[0][i] == ".":
            continue
        else:
            C = i + 1
            break
    for i in range(10):
        if S[0][9 - i] == ".":
            continue
        else:
            D = 10 - i
            break
    print(A, B)
    print(C, D)

=======
Suggestion 4

def main():
    S = []
    for i in range(10):
        S.append(input())
    A = 1
    B = 10
    C = 1
    D = 10
    for i in range(10):
        for j in range(10):
            if S[i][j] == '#':
                if i + 1 < A:
                    A = i + 1
                if i + 1 > B:
                    B = i + 1
                if j + 1 < C:
                    C = j + 1
                if j + 1 > D:
                    D = j + 1
    print(A, B)
    print(C, D)

=======
Suggestion 5

def main():
    s = [input() for _ in range(10)]
    a = b = c = d = 0
    for i in range(10):
        for j in range(10):
            if s[i][j] == '#':
                if a == 0:
                    a = i + 1
                if c == 0:
                    c = j + 1
                b = i + 1
                d = j + 1
    print(a, b)
    print(c, d)

=======
Suggestion 6

def main():
    S = [input() for i in range(10)]
    A = 0
    B = 0
    C = 0
    D = 0
    for i in range(10):
        if S[i].count('#') > 0:
            A = i + 1
            break
    for i in range(10):
        if S[9 - i].count('#') > 0:
            B = 10 - i
            break
    for i in range(10):
        if S[0][i] == '#':
            C = i + 1
            break
    for i in range(10):
        if S[0][9 - i] == '#':
            D = 10 - i
            break
    print(A, B)
    print(C, D)

=======
Suggestion 7

def main():
    S = [input() for _ in range(10)]
    A = [i for i in range(10) if S[0][i] == '#']
    B = [i for i in range(10) if S[9][i] == '#']
    C = [i for i in range(10) if S[i][0] == '#']
    D = [i for i in range(10) if S[i][9] == '#']
    print(min(A)+1, max(A)+1, min(C)+1, max(C)+1, sep=' ')
    print(min(B)+1, max(B)+1, min(D)+1, max(D)+1, sep=' ')

=======
Suggestion 8

def main():
    S = [input() for _ in range(10)]
    A = 1
    B = 1
    C = 1
    D = 1
    for i in range(10):
        for j in range(10):
            if S[i][j] == '#':
                A = max(A, i + 1)
                B = max(B, i + 1)
                C = max(C, j + 1)
                D = max(D, j + 1)
    print(A, B)
    print(C, D)

=======
Suggestion 9

def main():
    S = [input() for _ in range(10)]
    #print(S)
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
    print(A,B)
    print(C,D)
main()

=======
Suggestion 10

def main():
    # read the input
    table = []
    for _ in range(10):
        table.append(input())
    # find the answer
    for i in range(10):
        if table[i] == ".........#":
            A = i + 1
    for i in range(10):
        if table[i] == "..........":
            B = i
    for i in range(10):
        if table[0][i] == "#":
            C = i + 1
    for i in range(10):
        if table[0][i] == ".":
            D = i
    # print the answer
    print(A, B)
    print(C, D)
