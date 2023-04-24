Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = [[1] * (i + 1) for i in range(N)]
    for i in range(N):
        for j in range(1, i):
            A[i][j] = A[i - 1][j - 1] + A[i - 1][j]
    for i in range(N):
        print(' '.join(map(str, A[i])))

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
        print(" ".join([str(x) for x in a[i][:i+1]]))

=======
Suggestion 3

def main():
    n = int(input())
    a = [[1]]
    for i in range(1, n):
        a.append([1])
        for j in range(1, i):
            a[i].append(a[i - 1][j - 1] + a[i - 1][j])
        a[i].append(1)
    for i in range(n):
        print(*a[i])

=======
Suggestion 4

def pascal_triangle(n):
    if n == 0:
        return [1]
    if n == 1:
        return [1, 1]
    if n == 2:
        return [1, 2, 1]
    if n == 3:
        return [1, 3, 3, 1]
    if n == 4:
        return [1, 4, 6, 4, 1]
    if n == 5:
        return [1, 5, 10, 10, 5, 1]
    if n == 6:
        return [1, 6, 15, 20, 15, 6, 1]
    if n == 7:
        return [1, 7, 21, 35, 35, 21, 7, 1]
    if n == 8:
        return [1, 8, 28, 56, 70, 56, 28, 8, 1]
    if n == 9:
        return [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
    if n == 10:
        return [1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1]
    if n == 11:
        return [1, 11, 55, 165, 330, 462, 462, 330, 165, 55, 11, 1]
    if n == 12:
        return [1, 12, 66, 220, 495, 792, 924, 792, 495, 220, 66, 12, 1]
    if n == 13:
        return [1, 13, 78, 286, 715, 1287, 1716, 1716, 1287, 715, 286, 78, 13, 1]
    if n == 14:
        return [1, 14, 91, 364, 1001, 2002, 3003, 3432, 3003, 2002, 1001,

=======
Suggestion 5

def pascal(n):
    if n == 1:
        return [1]
    elif n == 2:
        return [1,1]
    else:
        return [1] + [pascal(n-1)[i-1] + pascal(n-1)[i] for i in range(1,n-1)] + [1]

N = int(input())
for i in range(1,N+1):
    print(*pascal(i))

=======
Suggestion 6

def main():
    N = int(input())
    A = [[1]]
    for i in range(1, N):
        A.append([1] + [A[i-1][j-1] + A[i-1][j] for j in range(1, i)] + [1])
    for a in A:
        print(*a)

=======
Suggestion 7

def main():
    n = int(input())
    for i in range(n):
        for j in range(i+1):
            if j==0 or j==i:
                print(1, end=' ')
            else:
                print(a[i-1][j-1]+a[i-1][j], end=' ')
        print()
        a.append([1]*(i+1))

=======
Suggestion 8

def pascal(N):
    if N==0:
        return [1]
    elif N==1:
        return [1,1]
    else:
        return [1]+[pascal(N-1)[i]+pascal(N-1)[i+1] for i in range(N-1)]+[1]

N=int(input())
for i in range(N):
    print(*pascal(i))

N=int(input())
for i in range(N):
    print(*[1]+[pascal(N-1)[i]+pascal(N-1)[i+1] for i in range(N-1)]+[1])

=======
Suggestion 9

def main():
    N = int(input())
    for i in range(N):
        tmp = [1]
        for j in range(i):
            tmp.append(tmp[j] + tmp[j-1])
        print(*tmp)

=======
Suggestion 10

def get_list(n):
    return [1] * (n+1)
