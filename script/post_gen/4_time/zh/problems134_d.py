Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def get_input():
    N = int(input())
    a = [int(i) for i in input().split()]
    return N, a

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int,input().split()))
    b = [0]*n
    for i in range(n-1,-1,-1):
        if sum(b[i::i+1])%2 != a[i]:
            b[i] = 1
    print(sum(b))
    if sum(b) != 0:
        print(*[i+1 for i in range(n) if b[i] == 1])

main()

=======
Suggestion 3

def solve(n, a):
    b = [0] * n
    for i in range(n):
        b[i] = a[i]
    for i in range(1, n + 1):
        if a[i - 1] == 1:
            for j in range(i * 2 - 1, n, i):
                b[j] = 1
    if sum(b) == 0:
        print(0)
    else:
        print(sum(b))
        for i in range(n):
            if b[i] == 1:
                print(i + 1, end=' ')
        print()

=======
Suggestion 4

def main():
    N = int(input())
    a = [int(i) for i in input().split()]
    b = [0]*N
    c = [0]*N
    d = []
    for i in range(N):
        if a[i] == 1:
            d.append(i+1)
    M = len(d)
    if M == 0:
        print(0)
        return
    for i in range(M):
        for j in range(M):
            if d[i] % d[j] == 0:
                b[i] += 1
    for i in range(M):
        if b[i] % 2 == 1:
            print(-1)
            return
    print(M)
    for i in range(M):
        print(d[i])

=======
Suggestion 5

def main():
    N = int(input())
    a = list(map(int, input().split()))
    b = [0]*N
    for i in range(N):
        if a[i] == 1:
            b[i] = 1
            for j in range(2, N//i+1):
                b[i*j-1] += 1
    c = []
    for i in range(N):
        if b[i] % 2 != a[i]:
            c.append(i+1)
    if len(c) == 0:
        print(0)
    else:
        print(len(c))
        print(*c)

=======
Suggestion 6

def check(a):
    n = len(a)
    # print(n)
    for i in range(n):
        if a[i] == 1:
            for j in range(n):
                if (j+1) % (i+1) == 0:
                    a[j] = (a[j] + 1) % 2
    if sum(a) == 0:
        return True
    else:
        return False

n = int(input())
a = list(map(int, input().split()))

=======
Suggestion 7

def main():
    pass

=======
Suggestion 8

def main():
    N = int(input())
    a = list(map(int,input().split()))
    b = [0]*N
    for i in range(N):
        if a[i] == 1:
            if i+1 < N:
                b[i+1] = 1
            else:
                b[0] = 1
    print(sum(b))
    for i in range(len(b)):
        if b[i] == 1:
            print(i+1)

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n)[::-1]:
        if sum(b[i::i+1]) % 2 != a[i]:
            b[i] = 1
    print(sum(b))
    print(*[i+1 for i in range(n) if b[i]])
