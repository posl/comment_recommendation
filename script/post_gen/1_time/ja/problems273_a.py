Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def f(x):
    if x == 0:
        return 1
    else:
        return x * f(x-1)

=======
Suggestion 2

def f(x):
    if x == 0:
        return 1
    else:
        return x * f(x-1)

N = int(input())
print(f(N))

=======
Suggestion 3

def f(n):
    if n == 0:
        return 1
    else:
        return n * f(n-1)

=======
Suggestion 4

def main():
    N = int(input())
    ans = 1
    for i in range(1,N+1):
        ans *= i
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    if N == 0:
        print(1)
    else:
        print(N * main(N-1))

=======
Suggestion 6

def main():
    N = int(input())
    print(f(N))
