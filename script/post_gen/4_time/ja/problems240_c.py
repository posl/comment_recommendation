Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    sum = 0
    for i in range(n):
        if i % 2 == 0:
            sum += a[i]
        else:
            sum += b[i]
    if sum >= x:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    n, x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    sum = 0
    for i in range(n):
        if (i + 1) % 2 == 0:
            sum += b[i]
        else:
            sum += a[i]
    if sum >= x:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def solve():
    N, X = map(int, input().split())
    a = []
    b = []
    for i in range(N):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)

    if sum(a) <= X and X <= sum(b):
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    N, X = map(int, input().split())
    a = []
    b = []
    for i in range(N):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)

    pos = 0
    for i in range(N):
        pos += a[i]
        if pos > X:
            print("No")
            return
        pos += b[i]

    if pos > X:
        print("No")
    else:
        print("Yes")

=======
Suggestion 5

def solve():
    N,X = map(int,input().split())
    a = []
    b = []
    for i in range(N):
        a_i,b_i = map(int,input().split())
        a.append(a_i)
        b.append(b_i)
    x = 0
    for i in range(N):
        if a[i] <= X - x <= b[i]:
            print('Yes')
            exit()
        else:
            x += a[i]
    print('No')

=======
Suggestion 6

def main():
    N, X = map(int, input().split())
    a = []
    b = []
    for i in range(N):
        a1, b1 = map(int, input().split())
        a.append(a1)
        b.append(b1)

    sum = 0
    for i in range(N):
        sum += a[i] * b[i]

    if sum >= X:
        print("Yes")
    else:
        print("No")

main()

=======
Suggestion 7

def main():
    N,X = map(int,input().split())
    a = []
    b = []
    for i in range(N):
        ai,bi = map(int,input().split())
        a.append(ai)
        b.append(bi)

    for i in range(N):
        X -= a[i]
        if X < 0:
            print("No")
            return
        if i == N-1:
            X -= b[i]
            if X < 0:
                print("No")
                return
            else:
                print("Yes")
                return

=======
Suggestion 8

def main():
    n,x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a_i,b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    pos = 0
    for i in range(n):
        if i == 0:
            pos += a[i]
        else:
            pos += a[i] - b[i-1]
        if pos == x:
            print('Yes')
            return
    print('No')

=======
Suggestion 9

def main():
    N, X = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(N)]
    sum = 0
    for i in range(N):
        sum += ab[i][0] * ab[i][1]
        if sum > X * 100:
            print("No")
            exit()
    print("Yes")

=======
Suggestion 10

def main():
    n,x = map(int, input().split())
    d = 0
    for i in range(n):
        a,b = map(int, input().split())
        d += b - a
    if abs(d) <= x:
        print('Yes')
    else:
        print('No')
