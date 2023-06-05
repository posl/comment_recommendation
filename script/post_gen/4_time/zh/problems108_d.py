Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve(L):
    N = 20
    M = 60
    u = [0] * M
    v = [0] * M
    w = [0] * M
    # 1. 1->2->3->...->N
    for i in range(N - 1):
        u[i] = i + 1
        v[i] = i + 2
        w[i] = 0
    # 2. 1->2->3->...->N->1->2->3->...->N
    for i in range(N - 1, 2 * N - 2):
        u[i] = i + 1 - (N - 1)
        v[i] = i + 2 - (N - 1)
        w[i] = i - (N - 1) + 1
    # 3. 1->2->3->...->N->1->2->3->...->N->1->2->3->...->N
    for i in range(2 * N - 2, 3 * N - 4):
        u[i] = i + 1 - 2 * (N - 1)
        v[i] = i + 2 - 2 * (N - 1)
        w[i] = 2 * (i - 2 * (N

=======
Suggestion 2

def main():
    return

=======
Suggestion 3

def main():
    pass

=======
Suggestion 4

def solve():
    L = int(input())
    N = 2 * L
    M = L + 1
    print(N, M)
    for i in range(1, L):
        print(i, i+1, 0)
        print(i, i+1, 1)
    print(L, L+1, 0)

=======
Suggestion 5

def solve():
    L = int(input())
    N = 0
    M = 0
    #这里有个很重要的性质，就是当L为偶数时，构造的图中的边的长度可以为0~L-1之间的任意偶数，当L为奇数时，构造的图中的边的长度可以为0~L-1之间的任意奇数
    if L % 2 == 0:
        M = L
        N = L + 2
    else:
        M = L + 1
        N = L + 3

    print(N, M)
    for i in range(1, L + 1):
        print(i, i + 1, i % 2)

    if L % 2 == 0:
        for i in range(1, L + 1):
            print(i, i + L // 2 + 1, i % 2)
    else:
        for i in range(1, L + 1):
            print(i, i + L // 2 + 2, i % 2)

    if L % 2 == 0:
        print(1, L + 3, L - 1)
        print(L + 2, L + 3, L - 1)
    else:
        print(1, L + 3, L)
        print(L + 2, L + 3, L - 2)

=======
Suggestion 6

def solve():
    pass

=======
Suggestion 7

def main():
    L = int(input())
    N = 20
    M = 60
    print(N, M)
    for i in range(1, N):
        print(i, i+1, 0)
    for i in range(1, N-1):
        print(i, i+2, 1)
    for i in range(1, N-2):
        print(i, i+3, 2)
    for i in range(1, N-3):
        print(i, i+4, 3)
    for i in range(1, N-4):
        print(i, i+5, 4)
    for i in range(1, N-5):
        print(i, i+6, 5)
    for i in range(1, N-6):
        print(i, i+7, 6)
    for i in range(1, N-7):
        print(i, i+8, 7)
    for i in range(1, N-8):
        print(i, i+9, 8)
    for i in range(1, N-9):
        print(i, i+10, 9)
    for i in range(1, N-10):
        print(i, i+11, 10)
    for i in range(1, N-11):
        print(i, i+12, 11)
    for i in range(1, N-12):
        print(i, i+13, 12)
    for i in range(1, N-13):
        print(i, i+14, 13)
    for i in range(1, N-14):
        print(i, i+15, 14)
    for i in range(1, N-15):
        print(i, i+16, 15)
    for i in range(1, N-16):
        print(i, i+17, 16)
    for i in range(1, N-17):
        print(i, i+18, 17)
    for i in range(1, N-18):
        print(i, i+19, 18)
    for i in range(1, N-19):
        print(i, i+20, 19)
    for i in range(1, N-20):
        print(i,

=======
Suggestion 8

def main():
    L = int(input())
    N = 2
    M = 2
    print(N, M)
    print(1, 2, 0)
    print(2, 3, L-1)
    return
