Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    for i in range(K):
        N = int("".join(sorted(str(N), reverse=True))) - int("".join(sorted(str(N))))
    print(N)

=======
Suggestion 2

def main():
    n,k = map(int,input().split())
    for i in range(k):
        g1 = int("".join(sorted(str(n),reverse=True)))
        g2 = int("".join(sorted(str(n))))
        n = g1 - g2
    print(n)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    for i in range(K):
        N = int(''.join(sorted(str(N), reverse=True))) - int(''.join(sorted(str(N))))
    print(N)

=======
Suggestion 4

def main():
    N, K = list(map(int, input().split()))
    for i in range(K):
        N = int(''.join(sorted(str(N), reverse=True))) - int(''.join(sorted(str(N))))
    print(N)

=======
Suggestion 5

def readinput():
    n,k=map(int,input().split())
    return n,k

=======
Suggestion 6

def g1(x):
    return int(''.join(sorted(str(x), reverse=True)))

=======
Suggestion 7

def g1(x):
    return int("".join(sorted(str(x), reverse=True)))

=======
Suggestion 8

def g1(x):
  return int(''.join(sorted(str(x))[::-1]))
