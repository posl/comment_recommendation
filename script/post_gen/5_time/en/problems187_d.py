Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A.sort(reverse=True)
    B.sort(reverse=True)
    aoki = sum(A)
    takahashi = 0
    for i in range(N):
        aoki -= A[i]
        takahashi += A[i] + B[i]
        if takahashi > aoki:
            return i + 1
    return N

print(solve())

=======
Suggestion 2

def solve():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    a.sort()
    b.sort()
    if n % 2 == 0:
        m1 = (a[n//2-1] + a[n//2]) / 2
        m2 = (b[n//2-1] + b[n//2]) / 2
        print(int((m2-m1)*2+1))
    else:
        m = (b[n//2] - a[n//2])
        print(m+1)
    return 0

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
    aoki = sum(a)
    takahashi = 0
    for i in range(n):
        if a[i] < b[i]:
            takahashi += b[i] - a[i]
    print(takahashi)

=======
Suggestion 4

def solve():
    n = int(input())
    a = [0]*n
    b = [0]*n
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    c = [a[i]+b[i] for i in range(n)]
    c.sort(reverse=True)
    print(sum(c[::2])-sum(c[1::2]))

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
    max_a = max(A)
    max_a_index = A.index(max_a)
    max_b = max(B)
    max_b_index = B.index(max_b)
    if max_a_index == max_b_index:
        if max_a > max_b:
            print(max_a)
        else:
            print(max_b)
    else:
        if max_a > max_b:
            print(max_a)
        else:
            print(max_b)

=======
Suggestion 6

def main():
    n = int(input())
    a = 0
    b = 0
    for _ in range(n):
        a1, b1 = map(int, input().split())
        a += a1
        b += b1
    print((a + b - 1) // b - 1)

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

    vote = 0
    for i in range(N):
        vote += A[i] + B[i]

    vote /= 2

    vote = int(vote)

    aoki = 0
    for i in range(N):
        aoki += A[i]
        if aoki >= vote:
            print(i+1)
            break

=======
Suggestion 8

def main():
    N = int(input())
    AB = []
    for i in range(N):
        AB.append(list(map(int, input().split())))
    result = 0
    for i in range(N):
        result += AB[i][0]
    result = result - result/2
    print(int(result))

=======
Suggestion 9

def solve():
    N = int(input())
    towns = []
    for i in range(N):
        A, B = map(int, input().split())
        towns.append((A, B))

    towns.sort(key=lambda x: x[0] + x[1], reverse=True)

    aoki = sum(x[0] for x in towns)
    takahashi = 0
    for i in range(N):
        if i % 2 == 0:
            takahashi += towns[i][0]
        else:
            aoki -= towns[i][0]

    print(takahashi - aoki)

=======
Suggestion 10

def solve():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]

    AB.sort(key=lambda x: x[0] + x[1], reverse=True)

    aoki = 0
    takahashi = 0

    for i, (a, b) in enumerate(AB):
        if i % 2 == 0:
            aoki += a
        else:
            takahashi += b

    print(aoki - takahashi)
