Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, A, B = map(int, input().split())
    print((N // (A + B)) * A + min(N % (A + B), A))

=======
Suggestion 2

def main():
    n, a, b = map(int, input().split())
    print(n // (a + b) * a + min(n % (a + b), a))

=======
Suggestion 3

def main():
    N, A, B = map(int, input().split())
    if A == 0:
        print(0)
    elif A + B > N:
        print(N // (A + B) * A)
    else:
        print(N // (A + B) * A + min(A, N % (A + B)))

=======
Suggestion 4

def main():
    N, A, B = map(int, input().split())
    if A == 0:
        print(0)
    elif A + B > N:
        print(N // (A + B) * A)
    else:
        print(N // (A + B) * A + min(N % (A + B), A))

=======
Suggestion 5

def main():
    N, A, B = map(int, input().split())
    if A == 0:
        print(0)
    elif B == 0:
        print(N)
    else:
        q, r = divmod(N, A + B)
        print(q * A + min(r, A))

=======
Suggestion 6

def solve(N, A, B):
    if A == 0:
        return 0
    if B == 0:
        return N
    q, r = divmod(N, A + B)
    return q * A + min(r, A)

N, A, B = map(int, input().split())
print(solve(N, A, B))

=======
Suggestion 7

def main():
    N, A, B = map(int, input().split())
    n = N // (A + B)
    m = N % (A + B)
    print(n * A + min(m, A))

=======
Suggestion 8

def main():
    N, A, B = map(int, input().split())
    if A == 0:
        print(0)
    elif A + B == 0:
        print(0)
    else:
        print(min(N // (A + B) * A + min(N % (A + B), A), N))

=======
Suggestion 9

def main():
    N, A, B = map(int, input().split())
    if A == 0:
        print(0)
        return
    if B == 0:
        print(N)
        return
    if A+B > N:
        print(0)
        return
    print(N//(A+B)*A + min(A,N%(A+B)))

main()

=======
Suggestion 10

def get_num_of_blue_balls(N, A, B):
    if A == 0:
        return 0
    if B == 0:
        return N
    if A + B > N:
        return (N // (A + B)) * A + min(A, N % (A + B))
    return (N // (A + B)) * A + A
