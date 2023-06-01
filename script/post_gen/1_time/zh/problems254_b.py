Synthesizing 10/10 solutions

=======
Suggestion 1

def pascal_triangle(n):
    """打印帕斯卡三角形"""
    row = [1]
    yh = []
    for i in range(n):
        yh.append(row)
        row = [1] + [row[j] + row[j+1] for j in range(len(row)-1)] + [1]
    return yh

=======
Suggestion 2

def main():
    n = int(input())
    a = [[0 for i in range(n)] for i in range(n)]
    a[0][0] = 1
    for i in range(1,n):
        for j in range(i+1):
            if j == 0 or j == i:
                a[i][j] = 1
            else:
                a[i][j] = a[i-1][j-1] + a[i-1][j]
    for i in range(n):
        for j in range(i+1):
            print(a[i][j],end=' ')
        print()

=======
Suggestion 3

def pascal_triangle(n):
    if n == 1:
        return [[1]]
    else:
        new_row = [1]
        result = pascal_triangle(n-1)
        last_row = result[-1]
        for i in range(len(last_row)-1):
            new_row.append(last_row[i]+last_row[i+1])
        new_row += [1]
        result.append(new_row)
        return result

=======
Suggestion 4

def solve(n):
    a = [[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        a[i][0] = 1
        a[i][i] = 1
    for i in range(2, n):
        for j in range(1, i):
            a[i][j] = a[i - 1][j - 1] + a[i - 1][j]
    return a

=======
Suggestion 5

def func254_b(n):
    a = []
    for i in range(n):
        if i == 0:
            a.append([1])
        elif i == 1:
            a.append([1, 1])
        else:
            b = [1]
            for j in range(1, i):
                b.append(a[i-1][j-1] + a[i-1][j])
            b.append(1)
            a.append(b)
    return a

=======
Suggestion 6

def pascal_triangle(n):
    if n == 0:
        return []
    elif n == 1:
        return [[1]]
    else:
        new_row = [1]
        result = pascal_triangle(n-1)
        last_row = result[-1]
        for i in range(len(last_row)-1):
            new_row.append(last_row[i] + last_row[i+1])
        new_row += [1]
        result.append(new_row)
    return result

=======
Suggestion 7

def pascal_triangle(n):
    l = []
    for i in range(n):
        l.append([])
        for j in range(i+1):
            if j == 0 or j == i:
                l[i].append(1)
            else:
                l[i].append(l[i-1][j-1] + l[i-1][j])
    return l

=======
Suggestion 8

def main():
    n = int(input())
    list = []
    for i in range(n):
        list.append([])
        for j in range(i + 1):
            if j == 0 or j == i:
                list[i].append(1)
            else:
                list[i].append(list[i - 1][j - 1] + list[i - 1][j])
    for i in range(n):
        for j in range(i + 1):
            print(list[i][j], end=" ")
        print()

=======
Suggestion 9

def problems254_b():
    n = int(input())
    a = []
    for i in range(n):
        for j in range(i+1):
            if j == 0 or j == i:
                a.append(1)
            else:
                a.append(a[-i]+a[-i-1])
        print(' '.join([str(a[i]) for i in range(len(a))]))
        a = []

=======
Suggestion 10

def main():
    n = int(input())
    a = [[0 for i in range(n)] for j in range(n)]
    a[0][0] = 1
    for i in range(1, n):
        a[i][0] = 1
        a[i][i] = 1
        for j in range(1, i):
            a[i][j] = a[i-1][j-1] + a[i-1][j]
    for i in range(n):
        for j in range(i+1):
            print(a[i][j], end=' ')
        print()
