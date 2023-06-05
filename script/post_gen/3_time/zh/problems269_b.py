Synthesizing 10/10 solutions

=======
Suggestion 1

def get_strs():
    strs = []
    for i in range(10):
        strs.append(input())
    return strs

=======
Suggestion 2

def problems269_b():
    pass

=======
Suggestion 3

def main():
    strs = []
    for i in range(10):
        strs.append(input())
    for i in range(10):
        for j in range(10):
            if strs[i][j] == '#':
                print(i+1,j+1)
                break
main()

=======
Suggestion 4

def find_min_max(string):
    a = 0
    b = 0
    c = 0
    d = 0
    for i in range(10):
        if '#' in string[i]:
            a = i+1
            break
    for i in range(9,-1,-1):
        if '#' in string[i]:
            b = i+1
            break
    for i in range(10):
        if '#' in string[i]:
            for j in range(10):
                if string[i][j] == '#':
                    c = j+1
                    break
            break
    for i in range(9,-1,-1):
        if '#' in string[i]:
            for j in range(9,-1,-1):
                if string[i][j] == '#':
                    d = j+1
                    break
            break
    return a, b, c, d

=======
Suggestion 5

def main():
    strs = []
    for i in range(10):
        strs.append(input())
    #print(strs)
    for i in range(10):
        for j in range(10):
            if strs[i][j] == '#':
                print(i+1,j+1)
                return

=======
Suggestion 6

def main():
    s = []
    for i in range(10):
        s.append(input())
    print(s)
    for i in range(10):
        if '#' in s[i]:
            print(i)
            break
    for j in range(10):
        if '#' in s[i][j]:
            print(j)
            break
    for i in range(9, -1, -1):
        if '#' in s[i]:
            print(i)
            break
    for j in range(9, -1, -1):
        if '#' in s[i][j]:
            print(j)
            break

=======
Suggestion 7

def find(s):
    for i in range(10):
        for j in range(10):
            if s[i][j] == '#':
                return [i, j]

s = []
for i in range(10):
    s.append(list(input()))

x, y = find(s)

A = x + 1
C = y + 1

x, y = find(s[::-1])

B = 10 - x
D = 10 - y

print(A, B)
print(C, D)

=======
Suggestion 8

def main():
    list = []
    for i in range(10):
        list.append(input())
    for i in range(10):
        for j in range(10):
            if list[i][j] == '#':
                print(i+1, j+1)
                break
        else:
            continue
        break
    for i in range(9, -1, -1):
        for j in range(9, -1, -1):
            if list[i][j] == '#':
                print(i+1, j+1)
                break
        else:
            continue
        break

=======
Suggestion 9

def main():
    # 读取输入
    s = []
    for i in range(10):
        s.append(input())
    # 计算
    row = 0
    col = 0
    for i in range(10):
        for j in range(10):
            if s[i][j] == "#":
                row = i
                col = j
                break
    # 输出
    print(row+1, col+1)
    print(row+2, col+2)

=======
Suggestion 10

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
                    a = i + 1
                if b == 0:
                    b = i + 1
                if c == 0:
                    c = j + 1
                if d == 0:
                    d = j + 1
                if a > i + 1:
                    a = i + 1
                if b < i + 1:
                    b = i + 1
                if c > j + 1:
                    c = j + 1
                if d < j + 1:
                    d = j + 1
    print(str(a) + " " + str(b))
    print(str(c) + " " + str(d))
