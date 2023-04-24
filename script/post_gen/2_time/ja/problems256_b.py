Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    P = 0
    B = [0, 0, 0, 0]
    for i in range(N):
        B[0] += 1
        for j in range(4):
            if B[j] > 0:
                B[j] -= 1
                if j + A[i] < 4:
                    B[j + A[i]] += 1
                else:
                    P += 1
    print(P)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    P = 0
    for i in range(N):
        if i == 0:
            P += 1
        else:
            P += A[i-1]
        if P >= 4:
            P -= 4
    print(P)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    P = 0
    for i in range(N):
        if i == 0:
            P += 1
        else:
            if A[i-1] == 1:
                P += 1
            elif A[i-1] == 2:
                P += 2
            elif A[i-1] == 3:
                P += 3
            elif A[i-1] == 4:
                P += 4
            else:
                pass
    print(P)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    p = 0
    for i in range(N):
        p += A[i]
        if p >= 4:
            p -= 4
    print(p)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    p = 0
    for i in range(n):
        p += 1
        p -= a[i] // 4
    print(p)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    P = 0
    for i in range(N):
        P += 1
        P -= A[i] // 4
    print(P)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int,input().split()))
    p = 0
    for i in range(n):
        p += 1
        for j in range(4):
            if j + a[i] >= 4:
                p += 1
    print(p)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int,input().split()))
    P = 0
    for i in range(N):
        P += 1
        if A[i] >= 4:
            P += 1
    print(P)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    P = 0
    for i in range(N):
        P += 1
        P -= (A[i] + P) // 4
    print(P)

main()

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int,input().split()))
    p = 0
    for i in range(n):
        if i == 0:
            p += 1
            continue
        p += 1
        if i + a[i] >= 4:
            p -= 1
    print(p)
