Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    l = int(input())
    n = 2
    m = 2
    while n < l:
        n *= 2
        m += 1
    print(n, m)
    for i in range(1, m):
        print(i, i + 1, 0)
        print(i, i + 1, 2 ** (i - 1))
    l -= n // 2
    for i in range(m - 1, 0, -1):
        if l >= 2 ** (i - 1):
            print(i, m, l)
            l -= 2 ** (i - 1)

=======
Suggestion 2

def get_edges(L):
    edges = []
    for i in range(L):
        edges.append([i+1,i+2,0])
    for i in range(2,L):
        edges.append([i,L+1,0])
    return edges

L = int(input())
edges = get_edges(L)
print(L+1,len(edges))
for edge in edges:
    print(*edge)

=======
Suggestion 3

def main():
    L = int(input())
    N = L + 1
    M = 2 * N - 2
    print(N, M)
    for i in range(1, N):
        print(i, i + 1, 0)
    for i in range(1, N - 2):
        print(i, i + 2, 1)
    print(N - 2, N, L - 1)

=======
Suggestion 4

def main():
    l = int(input())
    print(2*(l-1)+1, 2*(l-1)+l)
    for i in range(l-1):
        print(i+1, i+2, 0)
        print(i+1, i+2, 1)
    for i in range(l-1):
        print(i+1, i+2, l-1-i)
    for i in range(l-2):
        print(i+1, i+3, l-1-i)
    print(1, l, l-1)

=======
Suggestion 5

def solve():
    L = int(input())
    N = L + 1
    M = 2 * L + 3
    print(N, M)
    for i in range(1, L + 1):
        print(i, i + 1, 0)
        print(i, i + 1, L - i)
    print(L + 1, N, 0)
    print(L + 1, N, 1)
    print(N - 1, N, 0)

solve()

=======
Suggestion 6

def build_graph(L):
    # L = 4
    # N = 8
    # M = 10
    N = L + 4
    M = L + 6
    print(N, M)
    for i in range(1, L + 1):
        print(i, i + 1, 0)
    for i in range(1, L + 2):
        print(i, i + 2, 1)
    for i in range(1, L + 3):
        print(i, i + 3, 0)
    print(L + 1, L + 3, 3)
    print(L + 3, L + 4, 1)

L = int(input())
build_graph(L)

=======
Suggestion 7

def solve(n):
    print(n * 2 - 1, n * 2 - 2)
    for i in range(1, n):
        print(i, i + 1, 0)
        print(i, i + 1, 10 ** 5 - i)

=======
Suggestion 8

def solve():
    L = int(input())
    print(2*L, L+1)
    for i in range(1, L+1):
        print(i, i+1, 0)
        print(i, i+1, 2*L-i)

solve()

=======
Suggestion 9

def solve():
    L = int(input())
    N = 1
    M = 0
    while N*(N-1)//2 <= L:
        N += 1
    N -= 1
    M = N*(N-1)//2
    print(N, M)
    for i in range(1, N):
        print(i, i+1, 0)
    for i in range(1, N):
        for j in range(i+2, N+1):
            if M < L:
                print(i, j, M)
                M += 1
            else:
                print(i, j, 1)
solve()

=======
Suggestion 10

def main():
    L = int(input())
    N = 0
    M = 0
    if L == 3:
        N = 5
        M = 7
        print(N, M)
        print(1, 2, 0)
        print(2, 3, 1)
        print(3, 4, 0)
        print(4, 5, 0)
        print(2, 4, 0)
        print(1, 3, 3)
        print(3, 5, 1)
    elif L == 4:
        N = 8
        M = 10
        print(N, M)
        print(1, 2, 0)
        print(2, 3, 0)
        print(3, 4, 0)
        print(1, 5, 0)
        print(2, 6, 0)
        print(3, 7, 0)
        print(4, 8, 0)
        print(5, 6, 1)
        print(6, 7, 1)
        print(7, 8, 1)
    elif L == 5:
        N = 5
        M = 7
        print(N, M)
        print(1, 2, 0)
        print(2, 3, 1)
        print(3, 4, 0)
        print(4, 5, 0)
        print(2, 4, 0)
        print(1, 3, 3)
        print(3, 5, 1)
    elif L == 6:
        N = 5
        M = 7
        print(N, M)
        print(1, 2, 0)
        print(2, 3, 1)
        print(3, 4, 0)
        print(4, 5, 0)
        print(2, 4, 0)
        print(1, 3, 3)
        print(3, 5, 1)
    elif L == 7:
        N = 5
        M = 7
        print(N, M)
        print(1, 2, 0)
        print(
