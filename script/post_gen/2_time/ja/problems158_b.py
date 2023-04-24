Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, a, b = map(int, input().split())
    print((n // (a + b)) * a + min(n % (a + b), a))

=======
Suggestion 2

def main():
    N, A, B = map(int, input().split())
    result = N // (A + B) * A
    rest = N % (A + B)
    if rest <= A:
        result += rest
    else:
        result += A
    print(result)

=======
Suggestion 3

def main():
    N, A, B = map(int, input().split())
    q, mod = divmod(N, A + B)
    ans = q * A
    ans += min(mod, A)
    print(ans)

=======
Suggestion 4

def main():
    N, A, B = map(int, input().split())
    if A == 0:
        print(0)
    elif A + B >= N:
        print(A)
    else:
        print((N // (A + B)) * A + min(A, N % (A + B)))

main()

=======
Suggestion 5

def main():
    n, a, b = map(int, input().split())
    #print(n, a, b)
    ans = (n // (a + b)) * a + min(n % (a + b), a)
    print(ans)

=======
Suggestion 6

def main():
    N, A, B = map(int, input().split())
    q, r = divmod(N, A+B)
    print(A*q + min(A, r))

=======
Suggestion 7

def main():
    N,A,B = map(int,input().split())
    print(N//(A+B)*A + min(N%(A+B),A))

=======
Suggestion 8

def main():
    N,A,B = map(int,input().split())
    q,r = divmod(N,A+B)
    print(q*A+min(r,A))
