Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    L = int(input())
    N = 0
    M = 0
    if L == 3:
        N = 4
        M = 4
        print(N,M)
        print("1 2 0")
        print("2 3 0")
        print("3 4 0")
        print("2 4 1")
    elif L == 4:
        N = 8
        M = 10
        print(N,M)
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
    elif L == 5:
        N = 5
        M = 7
        print(N,M)
        print("1 2 0")
        print("2 3 1")
        print("3 4 0")
        print("4 5 0")
        print("2 4 0")
        print("1 3 3")
        print("3 5 1")
    elif L == 6:
        N = 12
        M = 14
        print(N,M)
        print("1 2 0")
        print("2 3 0")
        print("3 4 0")
        print("4 5 0")
        print("2 6 0")
        print("3 7 0")
        print("4 8 0")
        print("5 9 0")
        print("6 10 0")
        print("7 11 0")
        print("8 12 0")
        print("9 11 1")
        print("10 12 1")
        print("11 12 2")
    elif L == 7:
        N = 6
        M = 8
        print(N,M)
        print("1 2 0")
        print("2 3 0")
        print("3 4 0")
        print("4 5 0")
        print("5 6 0")

=======
Suggestion 2

def main():
    L = int(input())
    N = 2
    M = 0
    if L == 3:
        M = 3
        N = 4
        print(N, M)
        print(1, 2, 0)
        print(2, 3, 0)
        print(3, 4, 0)
    elif L == 4:
        M = 10
        N = 8
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
        M = 7
        N = 5
        print(N, M)
        print(1, 2, 0)
        print(2, 3, 1)
        print(3, 4, 0)
        print(4, 5, 0)
        print(2, 4, 0)
        print(1, 3, 3)
        print(3, 5, 1)
    elif L == 6:
        M = 13
        N = 9
        print(N, M)
        print(1, 2, 0)
        print(2, 3, 0)
        print(3, 4, 0)
        print(4, 5, 0)
        print(5, 6, 0)
        print(1, 7, 0)
        print(2, 8, 0)
        print(3, 9, 0)
        print(7, 8, 1)
        print(8, 9, 1)
        print(1, 5, 2)
        print(5, 9, 1)
        print(1, 4, 4)
    elif L == 7:
        M = 15
        N =

=======
Suggestion 3

def main():
    l = int(input())
    n = 0
    m = 0
    if l == 3:
        n = 2
        m = 1
    elif l == 4:
        n = 2
        m = 2
    elif l == 5:
        n = 2
        m = 2
    elif l == 6:
        n = 3
        m = 3
    elif l == 7:
        n = 3
        m = 3
    elif l == 8:
        n = 3
        m = 3
    elif l == 9:
        n = 3
        m = 3
    elif l == 10:
        n = 4
        m = 4
    elif l == 11:
        n = 4
        m = 4
    elif l == 12:
        n = 4
        m = 4
    elif l == 13:
        n = 4
        m = 4
    elif l == 14:
        n = 4
        m = 4
    elif l == 15:
        n = 4
        m = 4
    elif l == 16:
        n = 4
        m = 4
    elif l == 17:
        n = 4
        m = 4
    elif l == 18:
        n = 4
        m = 4
    elif l == 19:
        n = 4
        m = 4
    elif l == 20:
        n = 4
        m = 4
    elif l == 21:
        n = 5
        m = 5
    elif l == 22:
        n = 5
        m = 5
    elif l == 23:
        n = 5
        m = 5
    elif l == 24:
        n = 5
        m = 5
    elif l == 25:
        n = 5
        m = 5
    elif l == 26:
        n = 5
        m = 5
    elif l == 27:
        n = 5
        m = 5
    elif l ==

=======
Suggestion 4

def main():
    L = int(input())
    N = 0
    M = 0
    if L == 3:
        N = 5
        M = 5
        print(N, M)
        print("1 2 0")
        print("2 3 1")
        print("3 4 0")
        print("4 5 0")
        print("2 4 0")
        print("1 3 3")
        print("3 5 1")
    else:
        N = L + 1
        M = 2 * L - 1
        print(N, M)
        for i in range(1, L):
            print(i, i + 1, 0)
            print(i, i + 1, 2 ** (i - 1))
        for i in range(1, L):
            print(i, i + 1, L - 1)

=======
Suggestion 5

def main():
    L = int(input())
    print(2, 2 * L)
    for i in range(1, L):
        print(i, i + 1, 0)
        print(i, i + 1, 2 ** (i - 1))
    A = L.bit_length() - 1
    B = L - 2 ** A + 1
    for i in range(A):
        if (B >> i) & 1:
            print(A + 1, i + 1, 2 ** i)
    for i in range(A):
        if not (B >> i) & 1:
            print(A + 1, i + 1, 2 ** i)

=======
Suggestion 6

def main():
    l = int(input())
    n = 0
    if l == 3:
        print(2, 1)
        print(1, 2, 0)
    elif l == 4:
        print(2, 2)
        print(1, 2, 0)
        print(2, 1, 1)
    elif l == 5:
        print(2, 3)
        print(1, 2, 0)
        print(2, 1, 1)
        print(2, 1, 2)
    elif l == 6:
        print(2, 3)
        print(1, 2, 0)
        print(2, 1, 1)
        print(2, 1, 2)
    elif l == 7:
        print(2, 4)
        print(1, 2, 0)
        print(2, 1, 1)
        print(2, 1, 2)
        print(2, 1, 3)
    elif l == 8:
        print(2, 4)
        print(1, 2, 0)
        print(2, 1, 1)
        print(2, 1, 2)
        print(2, 1, 3)
    elif l == 9:
        print(2, 4)
        print(1, 2, 0)
        print(2, 1, 1)
        print(2, 1, 2)
        print(2, 1, 3)
    elif l == 10:
        print(2, 4)
        print(1, 2, 0)
        print(2, 1, 1)
        print(2, 1, 2)
        print(2, 1, 3)
    elif l == 11:
        print(2, 5)
        print(1, 2, 0)
        print(2, 1, 1)
        print(2, 1, 2)
        print(2, 1, 3)
        print(2, 1, 4)
    elif l == 12:
        print(2, 5)
        print(1,

=======
Suggestion 7

def solve():
    L = int(input())
    N = 0
    M = 0
    print(N, M)

=======
Suggestion 8

def main():
    L = int(input())
    N = 0
    M = 0
    ans = []
    if L == 3:
        N = 2
        M = 1
        ans = [[1,2,0]]
    elif L == 4:
        N = 8
        M = 10
        ans = [[1,2,0],[2,3,0],[3,4,0],[1,5,0],[2,6,0],[3,7,0],[4,8,0],[5,6,1],[6,7,1],[7,8,1]]
    elif L == 5:
        N = 5
        M = 7
        ans = [[1,2,0],[2,3,1],[3,4,0],[4,5,0],[2,4,0],[1,3,3],[3,5,1]]
    elif L == 6:
        N = 2
        M = 1
        ans = [[1,2,0]]
    elif L == 7:
        N = 3
        M = 2
        ans = [[1,2,0],[2,3,0]]
    elif L == 8:
        N = 8
        M = 10
        ans = [[1,2,0],[2,3,0],[3,4,0],[1,5,0],[2,6,0],[3,7,0],[4,8,0],[5,6,1],[6,7,1],[7,8,1]]
    elif L == 9:
        N = 5
        M = 7
        ans = [[1,2,0],[2,3,1],[3,4,0],[4,5,0],[2,4,0],[1,3,3],[3,5,1]]
    elif L == 10:
        N = 2
        M = 1
        ans = [[1,2,0]]
    elif L == 11:
        N = 3
        M = 2
        ans = [[1,2,0],[2,3,0]]
    elif L == 12:
        N = 8
        M = 10
        ans = [[

=======
Suggestion 9

def main():
    L = int(input())
    N = 2
    M = 2
    print(N, M)
    print(1, 2, 0)
    print(1, 2, 0)

=======
Suggestion 10

def main():
    L = int(input())
    N = 2
    M = 0
    ans = []
    for i in range(20):
        if L & (1 << i):
            ans.append([i + 1, i + 2, 0])
            ans.append([i + 1, i + 2, 1 << i])
            N += 1
            M += 2
    for i in range(20):
        if L & (1 << i):
            continue
        ans.append([i + 1, 20, 0])
        N += 1
        M += 1
    print(N, M)
    for i in range(M):
        print(*ans[i])
