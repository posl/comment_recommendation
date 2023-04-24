Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    p = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if p[i] != i + 1:
            count += 1
    if count <= 2:
        print("YES")
    else:
        print("NO")

=======
Suggestion 2

def main():
    N = int(input())
    p = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if p[i] != i + 1:
            count += 1
    if count <= 2:
        print("YES")
    else:
        print("NO")
    return

=======
Suggestion 3

def main():
    N = int(input())
    p = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if p[i] != i + 1:
            count += 1
    if count == 0 or count == 2:
        print("YES")
    else:
        print("NO")

=======
Suggestion 4

def main():
    N = int(input())
    p = list(map(int, input().split()))
    cnt = 0
    for i in range(N):
        if p[i] != i+1:
            cnt += 1
    if cnt <= 2:
        print('YES')
    else:
        print('NO')

=======
Suggestion 5

def main():
    N = int(input())
    p = list(map(int, input().split()))

    count = 0
    for i in range(N):
        if p[i] != i + 1:
            count += 1

    if count <= 2:
        print('YES')
    else:
        print('NO')

=======
Suggestion 6

def swap(A, i, j):
    tmp = A[i]
    A[i] = A[j]
    A[j] = tmp

=======
Suggestion 7

def main():
    N = int(input())
    p = list(map(int, input().split()))

    # N = 2
    # p = [2, 1]

    # N = 5
    # p = [5, 2, 3, 4, 1]

    # N = 5
    # p = [2, 4, 3, 5, 1]

    # N = 7
    # p = [1, 2, 3, 4, 5, 6, 7]

    # N = 7
    # p = [4, 2, 3, 1, 5, 6, 7]

    # N = 7
    # p = [1, 2, 3, 4, 5, 6, 7]

    # N = 10
    # p = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # N = 10
    # p = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]

    # N = 10
    # p = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # N = 10
    # p = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

    # N = 10
    # p = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # N = 10
    # p = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # N = 10
    # p = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

    # N = 10
    # p = [1, 2, 3, 4, 5, 6,

=======
Suggestion 8

def main():
    #Write code here
    N = int(input())
    p = list(map(int, input().split()))
    if p == sorted(p):
        print('YES')
    elif p == sorted(p, reverse=True):
        print('NO')
    else:
        if p[0] == 1:
            if p[1] == 2:
                print('YES')
            else:
                print('NO')
        elif p[-1] == N:
            if p[-2] == N-1:
                print('YES')
            else:
                print('NO')
        else:
            p1 = p[:]
            p1[p1.index(1)] = p1[p1.index(1)-1]
            p1[p1.index(1)-1] = 1
            if p1 == sorted(p1):
                print('YES')
            else:
                print('NO')

=======
Suggestion 9

def main():
    N = int(input())
    p = list(map(int, input().split()))
    #print(N)
    #print(p)
    num = 0
    for i in range(N):
        if (i+1) != p[i]:
            num += 1
    if num == 0 or num == 2:
        print("YES")
    else:
        print("NO")
