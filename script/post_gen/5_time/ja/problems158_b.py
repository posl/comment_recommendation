Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, a, b = map(int, input().split())
    print(n // (a + b) * a + min(n % (a + b), a))

=======
Suggestion 2

def main():
    n, a, b = map(int, input().split())
    ans = 0
    ans += n // (a + b) * a
    ans += min(n % (a + b), a)
    print(ans)

=======
Suggestion 3

def main():
    N, A, B = map(int, input().split())
    print((N // (A + B)) * A + min(N % (A + B), A))

=======
Suggestion 4

def main():
    n, a, b = map(int, input().split())
    ans = n//(a+b)*a
    ans += min(n%(a+b), a)
    print(ans)

=======
Suggestion 5

def main():
    n, a, b = map(int, input().split())
    q, mod = divmod(n, a + b)
    print(q * a + min(a, mod))

=======
Suggestion 6

def main():
    N, A, B = map(int, input().split())
    print(A * (N // (A + B)) + min(A, N % (A + B)))

=======
Suggestion 7

def main():
    n, a, b = map(int, input().split())
    if n == 1:
        if a > 0:
            print(1)
        else:
            print(0)
    else:
        if a == 0:
            print(0)
        else:
            if b == 0:
                print(1)
            else:
                if a > b:
                    print(1)
                else:
                    print((n-1)*a+b)

=======
Suggestion 8

def main():
    N, A, B = map(int, input().split())
    print(N // (A + B) * A + min(N % (A + B), A))
