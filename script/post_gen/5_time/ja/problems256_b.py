Synthesizing 10/10 solutions

=======
Suggestion 1

def move(p, a):
    #print("move", p, a)
    p += 1
    #print("p:", p)
    if p == 4:
        p = 0
    p += a
    #print("p:", p)
    if p >= 4:
        p -= 4
    return p

n = int(input())
a = list(map(int, input().split()))
p = 0
ans = 0
for i in range(n):
    #print("i:", i)
    #print("a[i]:", a[i])
    if p == 0:
        ans += 1
    p = move(p, a[i])
print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    p = 0
    for i in range(n):
        p = p + a[i] - 1
    print(p)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    P = 0
    for i in range(N):
        P += A[i] - 1
        if P == 3:
            P = 0
    print(P)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    p = 0
    for i in range(n):
        p += 1
        p -= 1
        p += a[i]
        if p == 4:
            p = 0
    print(p)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    P = 0
    for i in range(N):
        P += A[i] - 1
    print(P)

=======
Suggestion 6

def main():
    n = int(input())
    A = list(map(int, input().split()))
    P = 0
    for i in range(n):
        P += A[i]-1
        P = P%4
    print(P)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int,input().split()))
    p = 0
    for i in range(n):
        p += a[i]
        if p >= 4:
            p -= 4
    print(p)

main()

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    p = 0
    for i in range(n):
        p += 1
        p += a[i] - 1
        p %= 4
    print(p)
main()

=======
Suggestion 9

def solve(n, a):
    p = 0
    for i in range(n):
        p += a[i]
        if p == 0:
            p += 1
        elif p == 1:
            p += 2
        elif p == 2:
            p += 3
        elif p == 3:
            p += 4
        if p >= 4:
            p -= 4
    return p

n = int(input())
a = list(map(int, input().split()))
print(solve(n, a))

=======
Suggestion 10

def get_input_int(): return int(input())
