Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        A_i, B_i = map(int, input().split())
        A.append(A_i)
        B.append(B_i)
    min_time = 10**5 * 2
    for i in range(N):
        for j in range(N):
            if i == j:
                time = A[i] + B[j]
            else:
                time = max(A[i], B[j])
            if time < min_time:
                min_time = time
    print(min_time)

=======
Suggestion 2

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        A_i, B_i = map(int, input().split())
        A.append(A_i)
        B.append(B_i)

    A_min = min(A)
    B_min = min(B)

    if A.index(A_min) == B.index(B_min):
        A.remove(A_min)
        B.remove(B_min)
        A_min = min(A)
        B_min = min(B)
        print(min(A_min + B_min, max(A_min, B_min)))
    else:
        print(max(A_min, B_min))

=======
Suggestion 3

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A.sort()
    B.sort()
    print(min(A[0]+B[0], max(A[0], B[1]), max(A[1], B[0])))

=======
Suggestion 4

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    min_time = 10**10
    for i in range(N):
        for j in range(N):
            if i == j:
                time = A[i] + B[j]
            else:
                time = max(A[i], B[j])
            if time < min_time:
                min_time = time
    print(min_time)

=======
Suggestion 5

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    min_time = 10**5 * 2
    for i in range(N):
        for j in range(N):
            time = max(A[i], B[j])
            if min_time > time:
                min_time = time
    print(min_time)

=======
Suggestion 6

def main():
    N = int(input())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    min_time = 10**10
    for i in range(N):
        for j in range(N):
            time = max(A[i], B[j])
            min_time = min(min_time, time)

    print(min_time)

=======
Suggestion 7

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    a_min = min(a)
    b_min = min(b)
    a_min_index = a.index(a_min)
    b_min_index = b.index(b_min)
    if a_min_index == b_min_index:
        a.remove(a_min)
        b.remove(b_min)
        a_min2 = min(a)
        b_min2 = min(b)
        print(min(a_min + b_min2, a_min2 + b_min))
    else:
        print(a_min + b_min)

=======
Suggestion 8

def main():
    N = int(input())
    A_B = []
    for i in range(N):
        A, B = map(int, input().split())
        A_B.append((A, B))
    A_B.sort(key=lambda x: x[0])
    A_B.sort(key=lambda x: x[1])
    print(max(A_B[0][1], A_B[1][0]))

=======
Suggestion 9

def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]

    min_time = 10**5 * 2
    for i in range(N):
        for j in range(N):
            if i == j:
                time = AB[i][0] + AB[j][1]
            else:
                time = max(AB[i][0], AB[j][1])
            min_time = min(time, min_time)
    print(min_time)

=======
Suggestion 10

def main():
    N = int(input())
    AB = []
    for i in range(N):
        AB.append(list(map(int, input().split())))
    AB.sort(key=lambda x: x[0]+x[1], reverse=True)
    print(max(AB[0][0],AB[1][0])+AB[0][1])
