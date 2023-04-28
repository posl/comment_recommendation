Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    min_time = 10**5
    for i in range(n):
        for j in range(n):
            if i == j:
                time = a[i] + b[j]
            else:
                time = max(a[i], b[j])
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
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    ans = 10**9
    for i in range(N):
        for j in range(N):
            if i == j:
                ans = min(ans, A[i] + B[j])
            else:
                ans = min(ans, max(A[i], B[j]))
    print(ans)
main()

=======
Suggestion 3

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    ans = 10 ** 9 + 1
    for i in range(n):
        for j in range(n):
            if i == j:
                ans = min(ans, a[i] + b[j])
            else:
                ans = min(ans, max(a[i], b[j]))
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    ans = 1000000
    for i in range(n):
        for j in range(n):
            if i == j:
                ans = min(ans, a[i] + b[j])
            else:
                ans = min(ans, max(a[i], b[j]))
    print(ans)
main()

=======
Suggestion 5

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)

    ans = 0
    for i in range(n):
        for j in range(n):
            if i != j:
                ans = max(ans, a[i]+b[j])
            else:
                ans = max(ans, a[i], b[j])

    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    a_list = []
    b_list = []
    for i in range(n):
        a,b = map(int,input().split())
        a_list.append(a)
        b_list.append(b)
    a_min = min(a_list)
    b_min = min(b_list)
    a_min_index = a_list.index(a_min)
    b_min_index = b_list.index(b_min)
    if a_min_index == b_min_index:
        a_list.pop(a_min_index)
        b_list.pop(b_min_index)
        a_min2 = min(a_list)
        b_min2 = min(b_list)
        print(min(a_min+b_min2,a_min2+b_min))
    else:
        print(max(a_min,b_min))

=======
Suggestion 7

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    print(min(A)+min(B))

=======
Suggestion 8

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a_, b_ = map(int, input().split())
        a.append(a_)
        b.append(b_)
    ans = 10**5
    for i in range(n):
        for j in range(n):
            if i == j:
                ans = min(ans, a[i]+b[j])
            else:
                ans = min(ans, max(a[i], b[j]))
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    min_A = min(A)
    min_B = min(B)
    if A.index(min_A) == B.index(min_B):
        if min_A < min_B:
            min_B = sorted(B)[1]
        else:
            min_A = sorted(A)[1]
    print(min(min_A,min_B))

=======
Suggestion 10

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        x, y = map(int, input().split())
        a.append(x)
        b.append(y)

    print(min(a) + min(b))
