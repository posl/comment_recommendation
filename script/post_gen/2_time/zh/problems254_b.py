Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        a[i][0] = 1
        a[i][i] = 1
    for i in range(2, n):
        for j in range(1, i):
            a[i][j] = a[i-1][j-1] + a[i-1][j]
    for i in range(n):
        for j in range(i+1):
            print(a[i][j], end=" ")
        print()

=======
Suggestion 2

def main():
    n = int(input())
    a = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(i+1):
            if j == 0 or j == i:
                a[i][j] = 1
            else:
                a[i][j] = a[i-1][j-1] + a[i-1][j]
    for i in range(n):
        for j in range(i+1):
            print(a[i][j], end=' ')
        print()

=======
Suggestion 3

def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append([1]*(i+1))
        for j in range(1,i):
            a[i][j] = a[i-1][j-1] + a[i-1][j]
    for i in range(n):
        print(" ".join(map(str,a[i])))

=======
Suggestion 4

def pascal_triangle(n):
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    else:
        result = []
        for i in range(1, n + 1):
            if i == 1:
                result.append(1)
            elif i == 2:
                result.append(1)
            else:
                result.append(pascal_triangle(n - 1)[i - 2] + pascal_triangle(n - 1)[i - 3])
        return result

=======
Suggestion 5

def main():
    n = int(input())
    a = [[1 for i in range(n)] for j in range(n)]
    for i in range(2, n):
        for j in range(1, i):
            a[i][j] = a[i-1][j-1] + a[i-1][j]
    for i in range(n):
        for j in range(i+1):
            print(a[i][j], end = ' ')
        print()

=======
Suggestion 6

def print_list(list):
    for i in range(len(list)):
        print(list[i], end=' ')
    print()
    return

=======
Suggestion 7

def main():
    # 读取输入
    n = int(input())
    # 初始化
    a = [[0 for j in range(n)] for i in range(n)]
    # 迭代
    for i in range(n):
        for j in range(i + 1):
            if j == 0 or j == i:
                a[i][j] = 1
            else:
                a[i][j] = a[i - 1][j - 1] + a[i - 1][j]
    # 输出
    for i in range(n):
        for j in range(i + 1):
            print(a[i][j], end=" ")
        print()

=======
Suggestion 8

def pascal_triangle(n):
    if n == 1:
        return [[1]]
    elif n == 2:
        return [[1],[1,1]]
    else:
        new_line = [1]
        result = pascal_triangle(n-1)
        last_line = result[-1]
        for i in range(len(last_line)-1):
            new_line.append(last_line[i]+last_line[i+1])
        new_line.append(1)
        result.append(new_line)
        return result

n = int(input())
result = pascal_triangle(n)
for line in result:
    print(" ".join(str(x) for x in line))

=======
Suggestion 9

def func(n):
    l = [[1]]
    for i in range(1, n):
        l.append([1])
        for j in range(1, i):
            l[i].append(l[i-1][j-1] + l[i-1][j])
        l[i].append(1)
    return l

=======
Suggestion 10

def main():
    n=int(input())
    a=[[1]*n for i in range(n)]
    for i in range(n):
        for j in range(1,i):
            a[i][j]=a[i-1][j-1]+a[i-1][j]
    for i in range(n):
        print(" ".join(map(str,a[i][:i+1])))
