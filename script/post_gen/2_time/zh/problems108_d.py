Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    L = int(input())
    N = 0
    M = 0
    # 1. 从L开始，逐渐减小，直到找到一个L，使得N*M<=60
    while True:
        N = L
        while N >= 2:
            M = L // N
            if M * N == L:
                break
            N -= 1
        if M * N == L:
            break
        L -= 1
    print(N, M)
    # 2. 构建图
    for i in range(1, N):
        print(i, i+1, 0)
    for i in range(1, M-1):
        print(i, i+1, i)
    print(1, M, L)

=======
Suggestion 2

def main():
    pass

=======
Suggestion 3

def main():
    L = int(input())
    N = 2
    M = 2
    print(N,M)
    print(1,2,0)
    print(1,2,1)

=======
Suggestion 4

def main():
    L = int(input())
    N = 20
    M = 60
    print(N, M)
    for i in range(1, N):
        print(i, i+1, 0)
    for i in range(1, N-1):
        print(i, i+2, L-i)
    print(1, 3, L)

=======
Suggestion 5

def solve(L):
    N = 20
    M = 60
    print(N, M)
    for i in range(N - 1):
        print(i + 1, i + 2, 0)
    for i in range(M - N + 1):
        print(i + 1, i + N, i % L + 1)

=======
Suggestion 6

def main():
    L = int(input())
    N = 0
    M = 0
    print(N, M)
    print()

=======
Suggestion 7

def problem108d():
    pass

=======
Suggestion 8

def main():
    L = int(input())
    N = 2
    M = 2 * L + 1
    print(N, M)
    print(1, 2, 0)
    for i in range(1, L + 1):
        print(2 * i - 1, 2 * i + 1, 1)
        print(2 * i, 2 * i + 1, 0)
