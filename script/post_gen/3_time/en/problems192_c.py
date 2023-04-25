Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    for i in range(K):
        N = int(''.join(sorted(str(N), reverse=True))) - int(''.join(sorted(str(N))))
    print(N)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    for i in range(K):
        N = int("".join(sorted(str(N), reverse=True))) - int("".join(sorted(str(N))))
    print(N)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    a = N
    for i in range(K):
        a = f(a)
    print(a)

=======
Suggestion 4

def f(x):
    g1 = sorted([int(i) for i in str(x)],reverse=True)
    g2 = sorted([int(i) for i in str(x)])
    return int("".join([str(i) for i in g1])) - int("".join([str(i) for i in g2]))

=======
Suggestion 5

def g1(x):
    return int(''.join(sorted(str(x), reverse=True)))

=======
Suggestion 6

def g1(x):
    return int("".join(sorted(str(x), reverse=True)))

=======
Suggestion 7

def main():
    N,K = map(int, input().split())
    for i in range(K):
        N = f(N)
    print(N)
