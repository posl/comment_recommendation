Synthesizing 10/10 solutions

=======
Suggestion 1

def get_input():
    s = []
    for i in range(10):
        s.append(input())
    return s

=======
Suggestion 2

def main():
    for i in range(10):
        print(input())
    for i in range(10):
        print(input())

=======
Suggestion 3

def main():
    # 读入数据
    data = []
    for i in range(10):
        data.append(input())

    # 找出最左边的#和最右边的#
    left = 10
    right = 0
    for i in range(10):
        for j in range(10):
            if data[i][j] == '#':
                if j < left:
                    left = j
                if j > right:
                    right = j

    # 找出最上面的#和最下面的#
    top = 10
    bottom = 0
    for i in range(10):
        for j in range(10):
            if data[i][j] == '#':
                if i < top:
                    top = i
                if i > bottom:
                    bottom = i

    # 输出结果
    print(top+1, right+1)
    print(bottom+1, left+1)

=======
Suggestion 4

def main():
    # 读入数据
    s = []
    for i in range(10):
        s.append(list(input()))

    # 从上往下找
    for i in range(10):
        for j in range(10):
            if s[i][j] == '#':
                print(i+1, j+1, end=' ')
                break
        if s[i][j] == '#':
            break

    # 从下往上找
    for i in range(9, -1, -1):
        for j in range(9, -1, -1):
            if s[i][j] == '#':
                print(i+1, j+1)
                break
        if s[i][j] == '#':
            break

=======
Suggestion 5

def solve():
    s = []
    for i in range(10):
        s.append(input())
    for i in range(10):
        for j in range(10):
            if s[i][j] == '#':
                return i+1, j+1

=======
Suggestion 6

def main():
    # 读入数据
    s = []
    for i in range(10):
        s.append(input())
    # 检查数据
    for i in range(10):
        if len(s[i]) != 10:
            print('输入数据有误')
            return
    # 找到A,B
    A = 10
    B = 1
    for i in range(10):
        if '#' in s[i]:
            if A > i:
                A = i
            if B < i:
                B = i
    # 找到C,D
    C = 10
    D = 1
    for i in range(10):
        for j in range(10):
            if s[i][j] == '#':
                if C > j:
                    C = j
                if D < j:
                    D = j
    # 输出结果
    print(A+1, B+1)
    print(C+1, D+1)
    return

=======
Suggestion 7

def get_input():
    input = []
    for i in range(10):
        input.append(raw_input())
    return input

=======
Suggestion 8

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
            a = i + 1
            b = i + 1
            c = s[i].find('#') + 1
            d = s[i].rfind('#') + 1
            break
    for i in range(a, 10):
        if s[i].find('#') != -1:
            b = i + 1
            break
    print(a, b)
    print(c, d)
main()

=======
Suggestion 9

def solve():
    for i in range(10):
        s = input()
        if s.find('#') >= 0:
            break
    for j in range(10):
        if s[j] == '#':
            break
    print(i+1,j+1)
    for k in range(10):
        if s[k] != '#':
            break
    print(k+1,j+1)

=======
Suggestion 10

def main():
    # 从标准输入读取数据
    s = []
    for i in range(10):
        s.append(input())
    # 求解
    for i in range(10):
        for j in range(10):
            if s[i][j] == '#':
                print(i+1,j+1)
                exit()
