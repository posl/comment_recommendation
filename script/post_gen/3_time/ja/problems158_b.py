Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, A, B = map(int, input().split())
    if A == 0:
        print(0)
    elif A + B > N:
        print(N // (A + B) * A + min(N % (A + B), A))
    else:
        print(A * N // (A + B))

=======
Suggestion 2

def main():
    n, a, b = map(int, input().split())
    if a == 0:
        print(0)
        return
    elif b == 0:
        print(n)
        return
    elif a + b > n:
        print(n)
        return
    else:
        num_a = n // (a + b)
        num_b = n % (a + b)
        if num_b > a:
            num_b = a
        print(num_a * a + num_b)

=======
Suggestion 3

def main():
    N, A, B = map(int, input().split())
    if A == 0:
        print(0)
    elif A + B <= N:
        print((N // (A + B)) * A + min(N % (A + B), A))
    else:
        print(min(N, A))

=======
Suggestion 4

def main():
    N, A, B = map(int, input().split())
    if A == 0:
        print(0)
    elif A + B == 0:
        print(N)
    else:
        print(A * (N // (A + B)) + min(A, N % (A + B)))

=======
Suggestion 5

def main():
    N, A, B = map(int, input().split())
    if A == 0:
        print(0)
    elif A + B == 0:
        print(0)
    else:
        print((N // (A + B)) * A + min(A, N % (A + B)))

=======
Suggestion 6

def main():
    N, A, B = map(int, input().split())
    if A == 0:
        print(0)
        return
    elif B == 0:
        print(A)
        return
    else:
        if A > B:
            A, B = B, A
        loop = N // (A + B)
        mod = N % (A + B)
        if mod > A:
            mod = A
        print(A * loop + mod)

=======
Suggestion 7

def main():
    N, A, B = map(int, input().split())
    if A == 0:
        print(0)
    elif A+B == 0:
        print(0)
    else:
        print(min(N//A, N//(A+B)*A + N%(A+B)))

=======
Suggestion 8

def main():
    N,A,B = map(int,input().split())
    if A == 0:
        print(0)
        return

    if B == 0:
        print(N)
        return

    if A + B > N:
        print(0)
        return

    if A + B == N:
        print(A)
        return

    if A + B < N:
        if A > B:
            print(B)
            return
        else:
            print(A)
            return

=======
Suggestion 9

def main():
    n,a,b = map(int,input().split())
    if a == 0:
        print(0)
    elif b == 0:
        print(n)
    else:
        if a+b > n:
            print(n//a)
        else:
            print(a*(n//(a+b)) + min(a,n%(a+b)))

=======
Suggestion 10

def main():
    n, a, b = map(int, input().split())
    if a == 0:
        print(0)
        return
    elif b == 0:
        print(n)
        return
    # a+b = 1の時は、n%2回操作するので、n%2*a回青いボールがある
    elif a + b == 1:
        print(n % 2 * a)
        return
    # それ以外は、(n // (a + b)) * a + min(n % (a + b), a)回青いボールがある
    else:
        print((n // (a + b)) * a + min(n % (a + b), a))
        return
