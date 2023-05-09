Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    L = int(input())
    if L == 2:
        print("2 1")
        print("1 2 0")
        return
    if L == 3:
        print("3 3")
        print("1 2 0")
        print("2 3 1")
        print("1 3 2")
        return
    if L == 4:
        print("4 5")
        print("1 2 0")
        print("2 3 1")
        print("3 4 0")
        print("2 4 2")
        print("1 3 3")
        return
    if L == 5:
        print("5 7")
        print("1 2 0")
        print("2 3 1")
        print("3 4 0")
        print("4 5 0")
        print("2 4 2")
        print("1 3 3")
        print("3 5 4")
        return
    if L == 6:
        print("6 9")
        print("1 2 0")
        print("2 3 1")
        print("3 4 0")
        print("4 5 0")
        print("5 6 0")
        print("2 4 2")
        print("1 3 3")
        print("3 5 4")
        print("4 6 5")
        return
    if L == 7:
        print("7 11")
        print("1 2 0")
        print("2 3 1")
        print("3 4 0")
        print("4 5 0")
        print("5 6 0")
        print("6 7 0")
        print("2 4 2")
        print("1 3 3")
        print("3 5 4")
        print("4 6 5")
        print("5 7 6")
        return
    if L == 8:
        print("8 13")
        print("1 2 0")
        print("2 3 1")
        print("3 4 0")
        print("4 5 0")
        print("5 6 0")
        print("6 7

=======
Suggestion 2

def solve():
    L = int(input())
    N = 1
    while 2 ** N <= L:
        N += 1
    M = N * (N - 1) // 2
    print(N, M)
    for i in range(1, N):
        print(i, i + 1, 0)
    for i in range(1, N):
        for j in range(i + 2, N + 1):
            print(i, j, 2 ** (i - 1))


solve()

=======
Suggestion 3

def solve():
    L = int(input())
    N = 20
    M = 60
    print(N, M)
    for i in range(1, N):
        print(i, i+1, 0)
    for i in range(1, N-2):
        if (L >> i) & 1:
            print(i, i+2, 1 << i)
    if L == 3:
        print(1, 3, 2)

=======
Suggestion 4

def main():
    L = int(input())
    print(2, 3)
    print(1, 2, 0)
    print(2, 3, 0)
    print(1, 3, 2 ** L - 1)

=======
Suggestion 5

def main():
    N = int(input())
    M = 2*N - 2
    print(N, M)
    for i in range(1, N):
        print(i, i+1, 0)
    for i in range(1, N-1):
        print(i, i+2, (1<<i-1))

=======
Suggestion 6

def main():
    l = int(input())
    n = 0
    m = 0
    for i in range(20):
        if (l>>i)&1:
            n = i+1
            m = i
    print(n,m)
    for i in range(1,n):
        print(i,i+1,0)
        print(i,i+1,2**(i-1))
    for i in range(m-n+1):
        print(i+1,n,2**(m-i-1))

=======
Suggestion 7

def main():
    L = int(input())
    N = 0
    M = 0
    print(N, M)

=======
Suggestion 8

def main():
    l = int(input())
    n = 0
    m = 0
    edges = []
    for i in range(20):
        if l & (1 << i):
            edges.append((i+1, i+2, 0))
            edges.append((i+1, i+2, 1 << i))
            n = i+2
            m += 2
    for i in range(19):
        if l & (1 << i):
            edges.append((i+1, i+2, (1 << i) - 1))
            n = i+2
            m += 1
    print(n, m)
    for u, v, w in edges:
        print(u, v, w)

=======
Suggestion 9

def main():
    L = int(input())
    # 1からLまでのパスを作る
    # 1 2 3 4 5 ... L
    # 1 2 3 4 5 ... L-1
    # 1 2 3 4 5 ... L-2
    # 1 2 3 4 5 ... L-3
    # ...
    # 1 2 3 4 5 ... 1
    # 1 2 3 4 1 ... 0
    # 1 2 3 1 0 ... 0
    # 1 2 1 0 0 ... 0
    # 1 1 0
