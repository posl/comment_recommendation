Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = [input() for i in range(10)]
    A = 0
    B = 0
    C = 0
    D = 0
    for i in range(10):
        for j in range(10):
            if S[i][j] == '#':
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
Suggestion 2

def main():
    s = []
    for i in range(10):
        s.append(input())
    a = b = c = d = 0
    for i in range(10):
        for j in range(10):
            if s[i][j] == "#":
                if a == 0:
                    a = i + 1
                if c == 0:
                    c = j + 1
                if i + 1 > b:
                    b = i + 1
                if j + 1 > d:
                    d = j + 1
    print(a, b)
    print(c, d)

=======
Suggestion 3

def main():
    s = [input() for _ in range(10)]
    ans = []
    for i in range(10):
        for j in range(10):
            if s[i][j] == "#":
                ans.append([i,j])
    print(ans[0][0]+1,ans[0][1]+1)
    print(ans[-1][0]+1,ans[-1][1]+1)

=======
Suggestion 4

def main():
    S = []
    for i in range(10):
        S.append(input())
    for i in range(10):
        for j in range(10):
            if S[i][j] == "#":
                print(i+1,j+1)
                exit()

=======
Suggestion 5

def main():
    # input
    S = [input() for _ in range(10)]
    # compute
    A, B, C, D = 0, 0, 0, 0
    for i in range(10):
        for j in range(10):
            if S[i][j] == '#':
                if A == 0:
                    A = i + 1
                if B == 0:
                    B = i + 1
                if C == 0:
                    C = j + 1
                if D == 0:
                    D = j + 1
                if i + 1 < A:
                    A = i + 1
                if B < i + 1:
                    B = i + 1
                if j + 1 < C:
                    C = j + 1
                if D < j + 1:
                    D = j + 1
    # output
    print(A, B)
    print(C, D)

=======
Suggestion 6

def main():
    S = [input() for i in range(10)]
    ans = []
    for i in range(10):
        for j in range(10):
            if S[i][j] == '#':
                ans.append([i+1,j+1])
    print(ans[0][0],ans[0][1])
    print(ans[-1][0],ans[-1][1])

=======
Suggestion 7

def main():
    # input
    S = [input() for _ in range(10)]

    # compute
    A = B = C = D = 0
    for i in range(10):
        if '#' in S[i]:
            if A == 0:
                A = i+1
            else:
                B = i+1
                break
    for j in range(10):
        if '#' in [S[i][j] for i in range(10)]:
            if C == 0:
                C = j+1
            else:
                D = j+1
                break

    # output
    print(A, B)
    print(C, D)

=======
Suggestion 8

def get_input_data():
    input_data = []
    for i in range(10):
        input_data.append(input())
    return input_data

=======
Suggestion 9

def get_input():
    s = []
    for i in range(10):
        s.append(input())
    return s

=======
Suggestion 10

def main():
    # input
    S = []
    for _ in range(10):
        S.append(input())
    # compute
    # まず、Sを10個のリストに分割する
    S_list = []
    for i in range(10):
        S_list.append(list(S[i]))
    # 1行目の#の位置を探す
    for i in range(10):
        if S_list[0][i] == '#':
            A = i + 1
            break
    # 10行目の#の位置を探す
    for i in range(10):
        if S_list[9][i] == '#':
            B = i + 1
            break
    # 1列目の#の位置を探す
    for i in range(10):
        if S_list[i][0] == '#':
            C = i + 1
            break
    # 10列目の#の位置を探す
    for i in range(10):
        if S_list[i][9] == '#':
            D = i + 1
            break
    # output
    print(A, B)
    print(C, D)
