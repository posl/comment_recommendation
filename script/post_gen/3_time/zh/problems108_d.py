Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve():
    L = int(input())
    if L == 2:
        print(2, 1)
        print(1, 2, 0)
    elif L == 3:
        print(3, 2)
        print(1, 2, 0)
        print(2, 3, 1)
    elif L == 4:
        print(4, 4)
        print(1, 2, 0)
        print(2, 3, 1)
        print(3, 4, 2)
        print(2, 4, 0)
    elif L == 5:
        print(5, 7)
        print(1, 2, 0)
        print(2, 3, 1)
        print(3, 4, 0)
        print(4, 5, 0)
        print(2, 4, 0)
        print(1, 3, 3)
        print(3, 5, 1)
    else:
        print(L, L - 1)
        for i in range(1, L):
            print(i, i + 1, 0)

solve()

=======
Suggestion 2

def solve():
    pass

=======
Suggestion 3

def get_graph(L):
    N = L + 1
    M = 2 * L - 1
    graph = []
    for i in range(1, L):
        graph.append((i, i + 1, 0))
    for i in range(1, L - 1):
        graph.append((i, i + 2, 2 * i - 1))
    for i in range(1, L - 2):
        graph.append((i, i + 3, 2 * i))
    for i in range(1, L - 3):
        graph.append((i, i + 4, 2 * i + 1))
    return N, M, graph

=======
Suggestion 4

def main():
    pass

=======
Suggestion 5

def solve():
    L = int(input())
    N = 20
    M = 60
    print(N, M)
    for i in range(1, N):
        print(i, i+1, 0)
    for i in range(1, N-2):
        print(i, i+2, 10**6)
    print(1, 4, L-(N-2)*(10**6))
    for i in range(5, N+1):
        print(4, i, 10**5)

=======
Suggestion 6

def main():
    L = int(input())
    N = 2
    M = 2*(L-1)
    print(N, M)
    for i in range(1, L):
        print(i, i+1, 0)
    for i in range(1, L-1):
        print(i, i+2, 2*(i-1)+1)

=======
Suggestion 7

def main():
    L = int(input())
    N = 0
    M = 0
    for i in range(1,L+1):
        N += i
        M += i-1
    print(N,M)
    for i in range(1,L):
        print(i,i+1,0)
    for i in range(1,L):
        for j in range(i+2,L+1):
            print(i,j,i-1)

=======
Suggestion 8

def main():
    n = int(input())
    print(n, n)
    for i in range(n-1):
        print(i+1, i+2, 0)
    for i in range(n-1):
        print(i+1, i+2, 1)

=======
Suggestion 9

def main():
    L = int(input())
    N = 20
    M = 60
    print(N, M)
    for i in range(1, N):
        print(i, i+1, 0)
    for i in range(1, N-1):
        print(i, i+2, 0)
    for i in range(1, N-2):
        print(i, i+3, 0)
    for i in range(1, N-3):
        print(i, i+4, 0)
    for i in range(1, N-4):
        print(i, i+5, 0)
    for i in range(1, N-5):
        print(i, i+6, 0)
    for i in range(1, N-6):
        print(i, i+7, 0)
    for i in range(1, N-7):
        print(i, i+8, 0)
    for i in range(1, N-8):
        print(i, i+9, 0)
    print(1, 10, L)
    print(2, 11, L)
    print(3, 12, L)
    print(4, 13, L)
    print(5, 14, L)
    print(6, 15, L)
    print(7, 16, L)
    print(8, 17, L)
    print(9, 18, L)
    print(10, 19, L)
    print(11, 20, L)
    print(12, 20, L)
    print(13, 20, L)
    print(14, 20, L)
    print(15, 20, L)
    print(16, 20, L)
    print(17, 20, L)
    print(18, 20, L)
    print(19, 20, L)
