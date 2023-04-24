Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, a, b = map(int, input().split())
    print(n // (a + b) * a + min(n % (a + b), a))

=======
Suggestion 2

def main():
    N, A, B = map(int, input().split())
    if A == 0:
        print(0)
    elif A + B > N:
        print(N // (A + B) * A + min(A, N % (A + B)))
    else:
        print(N // (A + B) * A + A)

=======
Suggestion 3

def main():
    N, A, B = map(int, input().split())
    if A == 0:
        print(0)
        return
    if A + B > N:
        print(N // (A + B) * A + min(N % (A + B), A))
    else:
        print(N // (A + B) * A + min(N % (A + B), A))

=======
Suggestion 4

def main():
    N, A, B = map(int, input().split())

    if A == 0:
        print(0)
    elif A + B > N:
        print(N // (A + B) * A)
    else:
        print(A * (N // (A + B)) + min(A, N % (A + B)))

=======
Suggestion 5

def main():
    n, a, b = map(int, input().split())
    if a == 0:
        print(0)
        return
    if b == 0:
        print(n // (a+b) * a)
        return
    if a + b > n:
        print(min(a, n))
        return
    if a + b == n:
        print(a)
        return
    if n % (a+b) <= a:
        print((n // (a+b)) * a + n % (a+b))
    else:
        print((n // (a+b)) * a + a)

main()

=======
Suggestion 6

def main():
    N, A, B = map(int, input().split())
    if A == 0:
        print(0)
    elif A + B == 0:
        print(0)
    elif A + B > N:
        print((N // (A + B)) * A + min(N % (A + B), A))
    else:
        print((N // (A + B)) * A + min(N % (A + B), A))

=======
Suggestion 7

def main():
    N, A, B = map(int, input().split())

    if A == 0 or B == 0:
        print(0)
        return

    if A + B > N:
        print(0)
        return

    if A + B == N:
        print(1)
        return

    if A + B < N:
        print((N - (A + B)) // (A + B) + 1)
        return

=======
Suggestion 8

def solve(N, A, B):
    if A == 0 or B == 0:
        return 0
    return (N // (A + B)) * A + min(N % (A + B), A)

=======
Suggestion 9

def main():
    n,a,b = map(int,input().split())
    if a == 0:
        print(0)
    else:
        print((n//(a+b))*a + min(n%(a+b),a))

=======
Suggestion 10

def main():
    #input
    N, A, B = map(int, input().split())
    #compute
    #output
    print(min(N//A*B + min(N%A, B), N))

main()
