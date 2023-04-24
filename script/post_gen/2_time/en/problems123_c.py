Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())

    M = min(A, B, C, D, E)

    print(((N + M - 1) // M) + 4)

=======
Suggestion 2

def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    print((N - 1) // min(A, B, C, D, E) + 5)

=======
Suggestion 3

def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    min_time = min(A, B, C, D, E)
    print((N + min_time - 1) // min_time + 4)

=======
Suggestion 4

def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())

    min_num = min(A, B, C, D, E)
    print((N + min_num - 1) // min_num + 4)

=======
Suggestion 5

def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    min_ = min(A, B, C, D, E)
    print((N + min_ - 1) // min_ + 4)

=======
Suggestion 6

def main():
    N = int(input())
    A, B, C, D, E = [int(input()) for _ in range(5)]
    print(-(-N // min(A, B, C, D, E)) + 4)

=======
Suggestion 7

def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    minT = min(A, B, C, D, E)
    print(-(-N // minT) + 4)

=======
Suggestion 8

def main():
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    if n % a == 0:
        ans = n // a
    else:
        ans = n // a + 1
    if n % b == 0:
        ans = max(ans, n // b)
    else:
        ans = max(ans, n // b + 1)
    if n % c == 0:
        ans = max(ans, n // c)
    else:
        ans = max(ans, n // c + 1)
    if n % d == 0:
        ans = max(ans, n // d)
    else:
        ans = max(ans, n // d + 1)
    if n % e == 0:
        ans = max(ans, n // e)
    else:
        ans = max(ans, n // e + 1)
    print(ans + 4)

=======
Suggestion 9

def main():
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    if n%a == 0:
        x = n//a
    else:
        x = n//a + 1
    if n%b == 0:
        y = n//b
    else:
        y = n//b + 1
    if n%c == 0:
        z = n//c
    else:
        z = n//c + 1
    if n%d == 0:
        w = n//d
    else:
        w = n//d + 1
    if n%e == 0:
        v = n//e
    else:
        v = n//e + 1
    print(4 + max(x,y,z,w,v))

=======
Suggestion 10

def main():
    #Read input
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())

    #Find the minimum value
    M = min(A, B, C, D, E)

    #Print output
    print((N + M - 1) // M + 4)
