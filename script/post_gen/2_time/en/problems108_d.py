Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    L = int(input())
    if L == 2:
        print(2, 1)
        print(1, 2, 1)
        return
    if L == 3:
        print(3, 2)
        print(1, 2, 2)
        print(2, 3, 1)
        return
    N = 2
    M = 1
    while 2 ** N <= L:
        N += 1
    N += 1
    M += N - 2
    print(N, M)
    for i in range(1, N):
        print(i, i + 1, 0)
    L -= 2 ** (N - 2)
    for i in range(N - 2, 0, -1):
        if L >= 2 ** (i - 1):
            L -= 2 ** (i - 1)
            print(i + 1, N, 2 ** (i - 1))
    print(1, N, L)

main()

=======
Suggestion 2

def main():
    L = int(input())
    N = 20
    M = 60
    print(N, M)
    for i in range(1, N):
        print(i, i + 1, 0)
    for i in range(1, N):
        print(i, i + 1, L - 1)
    for i in range(1, N - 1):
        print(i, i + 2, L - i - 1)

=======
Suggestion 3

def main():
    L = int(input())
    N = 20
    M = 60
    print(N, M)
    for i in range(1, N):
        print(i, i + 1, 0)
    for i in range(1, N - 1):
        print(i, i + 2, 1)
    k = 2
    for i in range(1, N - 2):
        print(i, i + 3, k)
        k += 1
    for i in range(1, L):
        print(i, i + 1, 0)

=======
Suggestion 4

def main():
    L = int(input())
    N = 20
    M = 60
    print(N, M)
    for i in range(1, N):
        print(i, i+1, 0)
    for i in range(1, N):
        print(i, i+1, 1)
    for i in range(1, N):
        print(i, i+1, L-1)
    for i in range(1, N):
        print(i, i+1, L)
    for i in range(1, N):
        print(i, i+1, L+1)
    for i in range(1, N):
        print(i, i+1, L+2)
    for i in range(1, N):
        print(i, i+1, L+3)
    for i in range(1, N):
        print(i, i+1, L+4)
    for i in range(1, N):
        print(i, i+1, L+5)
    for i in range(1, N):
        print(i, i+1, L+6)
    for i in range(1, N):
        print(i, i+1, L+7)
    for i in range(1, N):
        print(i, i+1, L+8)
    for i in range(1, N):
        print(i, i+1, L+9)
    for i in range(1, N):
        print(i, i+1, L+10)
    for i in range(1, N):
        print(i, i+1, L+11)
    for i in range(1, N):
        print(i, i+1, L+12)
    for i in range(1, N):
        print(i, i+1, L+13)
    for i in range(1, N):
        print(i, i+1, L+14)
    for i in range(1, N):
        print(i, i+1, L+15)
    for i in range(1, N):
        print(i, i+1, L+16)
    for i in range(1, N):
        print(i, i+1, L+17)
    for i in range(1, N):
        print(i, i+

=======
Suggestion 5

def solve(l):
    if l == 2:
        print(2, 1)
        print(1, 2, 1)
        return

    if l == 3:
        print(3, 2)
        print(1, 2, 0)
        print(2, 3, 1)
        return

    if l == 4:
        print(4, 4)
        print(1, 2, 0)
        print(2, 3, 0)
        print(3, 4, 0)
        print(1, 3, 1)
        return

    if l == 5:
        print(5, 7)
        print(1, 2, 0)
        print(2, 3, 1)
        print(3, 4, 0)
        print(4, 5, 0)
        print(2, 4, 0)
        print(1, 3, 3)
        print(3, 5, 1)
        return

    print(l + 1, l + l - 1)
    for i in range(1, l):
        print(i, i + 1, 0)
    print(1, l + 1, 1)
    for i in range(1, l):
        print(i, i + 1, 1)

=======
Suggestion 6

def main():
    L = int(input())
    if L == 2:
        print(2, 1)
        print(1, 2, 1)
        return
    N = 2
    M = 2
    ans = [[1, 2, 1]]
    while N * (N - 1) // 2 < L:
        ans.append([N, N + 1, 0])
        M += 1
        N += 1
    if N * (N - 1) // 2 == L:
        print(N, M)
        for x, y, z in ans:
            print(x, y, z)
        return
    ans.append([N, N + 1, N * (N - 1) // 2 - L])
    M += 1
    print(N + 1, M)
    for x, y, z in ans:
        print(x, y, z)

main()

=======
Suggestion 7

def main():
    L = int(input())
    if L % 2 == 0:
        print(2 * L // 2 + 1, 2 * L)
        for i in range(1, L // 2 + 1):
            print(i, i + 1, 0)
            print(i, i + L // 2 + 1, 1)
        print(L // 2 + 1, 2 * L, 0)
    else:
        print(2 * L // 2 + 2, 2 * L + 1)
        for i in range(1, L // 2 + 1):
            print(i, i + 1, 0)
            print(i, i + L // 2 + 2, 1)
        print(L // 2 + 1, L // 2 + 2, 0)
        print(L // 2 + 2, 2 * L + 1, 1)

=======
Suggestion 8

def main():
    L = int(input())
    N = 1
    M = 0
    while N*(N-1)//2 < L:
        N += 1
    print(N, N*(N-1)//2)
    for i in range(1, N):
        for j in range(i+1, N+1):
            print(i, j, min(L, i+j-2))
            M += 1
            L -= min(L, i+j-2)
            if L == 0:
                break
        if L == 0:
            break
    for i in range(M, N*(N-1)//2):
        print(1, 2, 0)

=======
Suggestion 9

def find_path(L):
    if L == 1:
        return [(1, 2, 0)]
    elif L == 2:
        return [(1, 2, 0), (2, 3, 0), (1, 3, 1)]
    elif L == 3:
        return [(1, 2, 0), (2, 3, 1), (3, 4, 0), (2, 4, 0), (1, 3, 2), (3, 5, 1), (1, 5, 3)]
    elif L == 4:
        return [(1, 2, 0), (2, 3, 1), (3, 4, 0), (4, 5, 0), (2, 4, 0), (1, 3, 2), (3, 5, 1), (1, 5, 3), (5, 6, 0), (6, 7, 0), (7, 8, 0), (1, 6, 0), (2, 7, 0), (3, 8, 0), (4, 9, 0), (5, 10, 0), (6, 11, 0), (7, 12, 0), (8, 13, 0), (9, 14, 0), (10, 15, 0), (11, 16, 0), (12, 17, 0), (13, 18, 0), (14, 19, 0), (15, 20, 0), (1, 7, 1), (2, 8, 1), (3, 9, 1), (4, 10, 1), (5, 11, 1), (6, 12, 1), (7, 13, 1), (8, 14, 1), (9, 15, 1), (10, 16, 1), (11, 17, 1), (12, 18, 1), (13, 19, 1), (14, 20, 1), (

=======
Suggestion 10

def generate_graph(L):
    N = 20
    M = 60
    edges = []
    for i in range(1, N):
        edges.append((i, i + 1, 0))
        for j in range(1, i):
            edges.append((j, i + 1, 1))
    for i in range(1, N):
        edges.append((i, i + 1, 2))
    for i in range(1, L):
        edges.append((i, i + 1, 3))
    return N, M, edges
