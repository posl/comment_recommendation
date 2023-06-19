Synthesizing 10/10 solutions

=======
Suggestion 1

def is_same(str1, str2):
    if len(str1) != len(str2):
        return False
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            return False
    return True

=======
Suggestion 2

def findHash(strList):
    #print(strList)
    for i in range(10):
        for j in range(10):
            if strList[i][j] == "#":
                return i,j

=======
Suggestion 3

def main():
    # 读取输入
    lines = []
    for i in range(10):
        lines.append(input())
    # print(lines)

    # 寻找第一个字符
    for i in range(10):
        if lines[i].find("#") != -1:
            first = i
            break

    # 寻找最后一个字符
    for i in range(9, -1, -1):
        if lines[i].find("#") != -1:
            last = i
            break

    # 寻找第一个行
    for i in range(10):
        if lines[i][0] == "#":
            firstCol = i
            break

    # 寻找最后一行
    for i in range(9, -1, -1):
        if lines[i][9] == "#":
            lastCol = i
            break

    print(first+1, last+1)
    print(firstCol+1, lastCol+1)

=======
Suggestion 4

def main():
    #读取输入数据
    strs = []
    for i in range(10):
        strs.append(input())
    # print(strs)

    #找出A,B,C,D
    A, B, C, D = 0, 0, 0, 0
    for i in range(10):
        if strs[i].find('#') != -1:
            A = i + 1
            B = i + 1
            break
    for i in range(A, 10):
        if strs[i].find('#') == -1:
            B = i
            break
    for i in range(10):
        if strs[i].find('#') != -1:
            C = strs[i].find('#') + 1
            D = strs[i].find('#') + 1
            break
    for i in range(C, 10):
        if strs[i].find('#') == -1:
            D = strs[i].find('#')
            break
    # print(A, B, C, D)
    print(A, B)
    print(C, D)

=======
Suggestion 5

def main():
    S = []
    for i in range(10):
        S.append(input())
    A = B = C = D = 0
    for i in range(10):
        for j in range(10):
            if S[i][j] == '#':
                if A == 0:
                    A = i + 1
                if C == 0:
                    C = j + 1
                B = i + 1
                D = j + 1
    print(A, B)
    print(C, D)

=======
Suggestion 6

def main():
    S = []
    for i in range(10):
        S.append(input())

    for i in range(10):
        if "#" in S[i]:
            A = i+1
            break

    for i in range(10):
        if "#" in S[9-i]:
            B = 10-i
            break

    for i in range(10):
        if "#" in [s[i] for s in S]:
            C = i+1
            break

    for i in range(10):
        if "#" in [s[9-i] for s in S]:
            D = 10-i
            break

    print(A,B)
    print(C,D)

=======
Suggestion 7

def get_input():
    return [input() for _ in range(10)]

=======
Suggestion 8

def solve():
    s = []
    for i in range(10):
        s.append(input())
    for i in range(10):
        if s[i].count('#') != 4:
            continue
        for j in range(10):
            if s[j][i] != '#':
                continue
            print(i+1, j+1)
            return

solve()

=======
Suggestion 9

def main():
    strs = []
    for i in range(10):
        strs.append(input())
    for i in range(10):
        if strs[i].count('.') == 10:
            strs.pop(i)
            break
    for i in range(len(strs)):
        strs[i] = strs[i].replace('.', ' ')
    for i in range(len(strs)):
        strs[i] = list(strs[i])
    A = 0
    B = 0
    C = 0
    D = 0
    for i in range(10):
        if '#' in strs[i]:
            A = i + 1
            break
    for i in range(9, -1, -1):
        if '#' in strs[i]:
            B = i + 1
            break
    for i in range(10):
        for j in range(10):
            if strs[i][j] == '#':
                C = j + 1
                break
        if C != 0:
            break
    for i in range(9, -1, -1):
        for j in range(10):
            if strs[i][j] == '#':
                D = j + 1
                break
        if D != 0:
            break
    print(str(A) + ' ' + str(B))
    print(str(C) + ' ' + str(D))

=======
Suggestion 10

def main():
    # 读取输入
    s = []
    for i in range(10):
        s.append(input())
    # 找到A,B,C,D
    for A in range(1, 11):
        for B in range(A, 11):
            for C in range(1, 11):
                for D in range(C, 11):
                    # 检查是否满足条件
                    flag = True
                    for i in range(A-1, B):
                        for j in range(C-1, D):
                            if s[i][j] != '#':
                                flag = False
                                break
                        if not flag:
                            break
                    if flag:
                        print(A, B)
                        print(C, D)
                        return
