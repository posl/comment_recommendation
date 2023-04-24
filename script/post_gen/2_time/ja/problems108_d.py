Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    L = int(input())
    print(8, 10)
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

=======
Suggestion 2

def main():
    L = int(input())
    print(8, 10)
    print("1 2 0")
    print("2 3 0")
    print("3 4 0")
    print("1 5 0")
    print("2 6 0")
    print("3 7 0")
    print("4 8 0")
    print("5 6 1")
    print("6 7 1")
    print("7 8 1")
    return

=======
Suggestion 3

def main():
    L = int(input())
    N = 20
    M = 60
    print(N, M)
    print("1 2 0")
    print("2 3 0")
    print("3 4 0")
    print("1 5 0")
    print("2 6 0")
    print("3 7 0")
    print("4 8 0")
    print("5 6 1")
    print("6 7 1")
    print("7 8 1")
    print("5 7 2")
    print("6 8 2")
    print("5 8 3")
    for i in range(4, L):
        print("1", i + 2, i - 3)
        print(i + 2, "20", 0)
    for i in range(4, L):
        print(i + 2, "20", 1)
    for i in range(4, L):
        print(i + 2, "20", 2)
    for i in range(4, L):
        print(i + 2, "20", 3)
    for i in range(4, L):
        print(i + 2, "20", 4)
    for i in range(4, L):
        print(i + 2, "20", 5)
    for i in range(4, L):
        print(i + 2, "20", 6)
    for i in range(4, L):
        print(i + 2, "20", 7)
    for i in range(4, L):
        print(i + 2, "20", 8)
    for i in range(4, L):
        print(i + 2, "20", 9)
    for i in range(4, L):
        print(i + 2, "20", 10)
    for i in range(4, L):
        print(i + 2, "20", 11)
    for i in range(4, L):
        print(i + 2, "20", 12)
    for i in range(4, L):
        print(i + 2, "20", 13)
    for i in range(4, L):
        print(i + 2, "20",

=======
Suggestion 4

def main():
    L = int(input())
    N = 20
    M = 60
    print(N, M)
    for i in range(1, N):
        print(i, i + 1, 0)
    for i in range(1, N):
        print(i, i + 1, 10 ** 6)
    for i in range(1, N):
        print(i, i + 1, 10 ** 6 - 1)
    for i in range(1, N):
        print(i, i + 1, 10 ** 6 - 2)
    for i in range(1, N):
        print(i, i + 1, 10 ** 6 - 3)
    i = 0
    while i < L - 4:
        print(1, N, 10 ** 6 - 4 - i)
        i += 1

=======
Suggestion 5

def main():
    L = int(input())
    if L % 2 == 0:
        print(2 * L, L)
        for i in range(1, L + 1):
            print(i, i + 1, 0)
            print(i, i + 1, 1)
    else:
        print(2 * L + 1, L + 1)
        for i in range(1, L + 1):
            print(i, i + 1, 0)
            print(i, i + 1, 1)
        print(L + 1, L + 2, 0)

=======
Suggestion 6

def main():
    L = int(input())
    if L == 2:
        print(2, 1)
        print(1, 2, 1)
        return
    print(L+1, L+1)
    for i in range(L+1):
        print(i+1, i+2, 0)
    for i in range(L):
        print(i+1, i+2, 1)
    print(L+1, 1, L-1)

=======
Suggestion 7

def solve():
    L = int(input())
    N = 20
    M = 60
    print(N, M)
    for i in range(1, N):
        print(i, i+1, 0)
    for i in range(1, N):
        print(i, i+1, 10**6)
    for i in range(1, N-2):
        print(i, i+3, 1)
    for i in range(1, N-2):
        print(i, i+3, 10**6-1)
    for i in range(1, N-2):
        print(i, i+3, 2*(10**6-1))
    L -= 3*(N-3)
    for i in range(1, N-2):
        if L == 0:
            break
        print(i, i+3, 10**6-2)
        L -= 1
    for i in range(1, N-2):
        if L == 0:
            break
        print(i, i+3, 2*(10**6-2))
        L -= 1
    for i in range(1, N-2):
        if L == 0:
            break
        print(i, i+3, 3*(10**6-2))
        L -= 1
    for i in range(1, N-2):
        if L == 0:
            break
        print(i, i+3, 4*(10**6-2))
        L -= 1
    for i in range(1, N-2):
        if L == 0:
            break
        print(i, i+3, 5*(10**6-2))
        L -= 1
    for i in range(1, N-2):
        if L == 0:
            break
        print(i, i+3, 6*(10**6-2))
        L -= 1
    for i in range(1, N-2):
        if L == 0:
            break
        print(i, i+3, 7*(10**6-2))
        L -= 1
    for i in range(1, N-2):
        if L == 0:
            break
        print(i, i+

=======
Suggestion 8

def main():
    L = int(input())
    path = []
    for i in range(L):
        path.append([i + 1, i + 2, 0])
        path.append([i + 1, i + 2, i + 1])
    path.append([L + 1, L + 2, 0])
    print(L + 2, len(path))
    for p in path:
        print(*p)

=======
Suggestion 9

def main():
    L = int(input())
    N = 20
    M = 60
    print(N, M)
    for i in range(M):
        if i < L:
            print(i + 1, i + 2, 0)
        elif i < 2 * L:
            print(i - L + 1, i - L + 2, 1)
        elif i < 3 * L:
            print(i - 2 * L + 1, i - 2 * L + 2, 2)
        elif i < 4 * L:
            print(i - 3 * L + 1, i - 3 * L + 2, 3)
        else:
            print(1, 3, i - 3 * L + 1)

=======
Suggestion 10

def solve(l):
    n = 20
    m = 60
    ans = []
    for i in range(1, n):
        ans.append((i, i+1, 0))
    ans.append((1, n, 1))
    ans.append((n, 1, 1))
    m -= 2
    for i in range(1, n-1):
        ans.append((i, i+2, 1))
        m -= 1
    for i in range(1, n-1):
        ans.append((i, n, 1))
        m -= 1
    for i in range(1, n-1):
        ans.append((i, n, 2))
        m -= 1
    ans.append((1, n, l-1))
    m -= 1
    ans.append((1, n, l))
    m -= 1
    ans.append((1, n, l+1))
    m -= 1
    for i in range(1, n-1):
        ans.append((i, n, l+2))
        m -= 1
    for i in range(1, n-1):
        ans.append((i, n, l+3))
        m -= 1
    for i in range(1, n-1):
        ans.append((i, n, l+4))
        m -= 1
    for i in range(1, n-1):
        ans.append((i, n, l+5))
        m -= 1
    for i in range(1, n-1):
        ans.append((i, n, l+6))
        m -= 1
    for i in range(1, n-1):
        ans.append((i, n, l+7))
        m -= 1
    for i in range(1, n-1):
        ans.append((i, n, l+8))
        m -= 1
    for i in range(1, n-1):
        ans.append((i, n, l+9))
        m -= 1
    for i in range(1, n-1):
        ans.append((i, n, l+10))
        m -= 1
    for i in range(1, n-1):
        ans.append((i,
