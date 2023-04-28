Synthesizing 10/10 solutions

=======
Suggestion 1

def pascals_triangle(n):
    if n == 1:
        return [[1]]
    else:
        new_row = [1]
        result = pascals_triangle(n-1)
        last_row = result[-1]
        for i in range(len(last_row)-1):
            new_row.append(last_row[i] + last_row[i+1])
        new_row += [1]
        result.append(new_row)
    return result
n = int(input())
for i in pascals_triangle(n):
    print(*i)

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
        print(' '.join(map(str, a[i])))

=======
Suggestion 3

def pascal(n):
    a = []
    for i in range(n):
        a.append([1]*(i+1))
        for j in range(1,i):
            a[i][j] = a[i-1][j-1] + a[i-1][j]
    return a

n = int(input())
a = pascal(n)
for i in a:
    print(' '.join(map(str,i)))

=======
Suggestion 4

def pascal_triangle(n):
    if n == 1:
        return [[1]]
    else:
        line = [1]
        triangle = pascal_triangle(n-1)
        last_line = triangle[-1]
        for i in range(len(last_line)-1):
            line.append(last_line[i] + last_line[i+1])
        line += [1]
        triangle.append(line)
    return triangle

n = int(input())
triangle = pascal_triangle(n)
for line in triangle:
    print(" ".join(map(str, line)))

=======
Suggestion 5

def main():
    n = int(input())
    ans = [[0] * i for i in range(1, n+1)]
    ans[0][0] = 1
    for i in range(1, n):
        for j in range(i+1):
            if j == 0 or j == i:
                ans[i][j] = 1
            else:
                ans[i][j] = ans[i-1][j-1] + ans[i-1][j]
    for i in range(n):
        print(*ans[i])

=======
Suggestion 6

def pascal_triangle(n):
    rows = []
    for i in range(n):
        rows.append([1]*(i+1))
        for j in range(1,i):
            rows[i][j] = rows[i-1][j-1] + rows[i-1][j]
    return rows

n = int(input())
rows = pascal_triangle(n)
for row in rows:
    print(" ".join(map(str,row)))

=======
Suggestion 7

def main():
    n = int(input())
    a = [0] * n
    for i in range(n):
        a[i] = [0] * (i + 1)
        a[i][0] = 1
        a[i][i] = 1
    for i in range(1, n):
        for j in range(1, i):
            a[i][j] = a[i - 1][j - 1] + a[i - 1][j]
    for i in range(n):
        print(*a[i])

=======
Suggestion 8

def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append([1] * (i+1))
        if i > 1:
            for j in range(1, i):
                A[i][j] = A[i-1][j-1] + A[i-1][j]
    for i in range(N):
        print(' '.join(map(str, A[i])))

=======
Suggestion 9

def solution(n):
    arr = [[0 for x in range(n)] for y in range(n)]
    for i in range(n):
        for j in range(i+1):
            if j == 0 or j == i:
                arr[i][j] = 1
            else:
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
    for i in range(n):
        print(' '.join(map(str, arr[i])))

=======
Suggestion 10

def get_input():
    return int(input())
