Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    L = int(input())
    if L == 2:
        print(4, 4)
        print(1, 2, 0)
        print(2, 3, 0)
        print(3, 4, 0)
        print(1, 4, 1)
    else:
        print(2 * L, 2 * L)
        for i in range(L):
            print(1, i + 2, i)
            print(i + 2, L + i + 2, 0)
        print(1, L + 1, L - 1)

=======
Suggestion 2

def main():
    L = int(input())
    if L == 2:
        print(4, 5)
        print(1, 2, 0)
        print(2, 3, 0)
        print(3, 4, 0)
        print(1, 3, 1)
        print(2, 4, 1)
    else:
        print(2 * L + 1, 2 * L + 2)
        for i in range(1, L + 1):
            print(i, i + 1, 0)
            print(i, i + L + 1, 1)
        print(L + 1, 2 * L + 2, L)

=======
Suggestion 3

def main():
    L = int(input())
    N = 20
    M = 60
    print(N, M)
    for i in range(1, N):
        print(i, i+1, 0)
    for i in range(1, N):
        print(i, i+1, 10**6)
    for i in range(1, N):
        for j in range(i+2, N+1):
            print(i, j, 10**6)
    for i in range(1, N):
        print(i, i+1, 10**6 - 1)
    for i in range(1, N):
        for j in range(i+2, N+1):
            print(i, j, 10**6 - 1)
    for i in range(1, N):
        for j in range(i+2, N+1):
            print(i, j, 10**6 - 2)
    for i in range(1, N):
        for j in range(i+2, N+1):
            print(i, j, 10**6 - 3)
    for i in range(1, N):
        for j in range(i+2, N+1):
            print(i, j, 10**6 - 4)
    for i in range(1, N):
        for j in range(i+2, N+1):
            print(i, j, 10**6 - 5)
    for i in range(1, N):
        for j in range(i+2, N+1):
            print(i, j, 10**6 - 6)
    for i in range(1, N):
        for j in range(i+2, N+1):
            print(i, j, 10**6 - 7)
    for i in range(1, N):
        for j in range(i+2, N+1):
            print(i, j, 10**6 - 8)
    for i in range(1, N):
        for j in range(i+2, N+1):
            print(i, j, 10**6 - 9)
    for i in range(1, N):
        for j in range(i+2, N+1):
            print(i, j, 10**6 - 10)

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
        print(i, i+1, 10**6)
    for i in range(1, N):
        print(i, i+1, L-1)
    for i in range(1, N):
        print(i, i+1, L)

=======
Suggestion 5

def main():
    L = int(input())
    if L <= 3:
        print(L + 1, L)
        for i in range(L):
            print(i + 1, i + 2, 0)
    else:
        print(2 * L, 2 * L)
        for i in range(L - 1):
            print(i + 1, i + 2, 0)
        print(L - 1, L, 0)
        print(L, L + 1, 0)
        for i in range(L):
            print(i + 1, L + i + 1, i)

=======
Suggestion 6

def main():
    L = int(input())
    N = 20
    M = 60
    print(N,M)
    for i in range(1,N):
        print(i,i+1,0)
    for i in range(1,N):
        print(i,i+1,10**6)
    for i in range(1,N-1):
        print(i,i+2,1)
    L -= 2*(N-1)
    for i in range(1,N-1):
        if L <= 0:
            break
        print(i,i+2,10**6-1)
        L -= 1
    for i in range(1,N-1):
        if L <= 0:
            break
        print(i,i+2,10**6-2)
        L -= 1
    for i in range(1,N-1):
        if L <= 0:
            break
        print(i,i+2,10**6-3)
        L -= 1

main()

=======
Suggestion 7

def main():
    L = int(input())
    #L = 4
    #L = 5
    #L = 6
    #L = 7
    #L = 8
    #L = 9
    #L = 10
    #L = 11
    #L = 12
    #L = 13
    #L = 14
    #L = 15
    #L = 16
    #L = 17
    #L = 18
    #L = 19
    #L = 20
    #L = 21
    #L = 22
    #L = 23
    #L = 24
    #L = 25
    #L = 26
    #L = 27
    #L = 28
    #L = 29
    #L = 30
    #L = 31
    #L = 32
    #L = 33
    #L = 34
    #L = 35
    #L = 36
    #L = 37
    #L = 38
    #L = 39
    #L = 40
    #L = 41
    #L = 42
    #L = 43
    #L = 44
    #L = 45
    #L = 46
    #L = 47
    #L = 48
    #L = 49
    #L = 50
    #L = 51
    #L = 52
    #L = 53
    #L = 54
    #L = 55
    #L = 56
    #L = 57
    #L = 58
    #L = 59
    #L = 60
    #L = 61
    #L = 62
    #L = 63
    #L = 64
    #L = 65
    #L = 66
    #L = 67
    #L = 68
    #L = 69
    #L = 70
    #L = 71
    #L = 72
    #L = 73
    #

=======
Suggestion 8

def main():
    L = int(input())
    if L == 2:
        print(2, 1)
        print(1, 2, 1)
        return

    N = 2 * L - 1
    M = N - 1 + N // 2
    print(N, M)
    for i in range(1, N):
        print(i, i + 1, 0)
    for i in range(1, N, 2):
        print(i, i + 2, 1)
    for i in range(2, N, 2):
        print(i, i + 2, i // 2)

=======
Suggestion 9

def main():
    L = int(input())
    N = 2*L+1
    print(N,N-1)
    for i in range(1,N):
        print(i, i+1, 0)
    for i in range(1,L+1):
        print(i, i+L, 1)

=======
Suggestion 10

def get_input():
    L = int(input())
    return L
