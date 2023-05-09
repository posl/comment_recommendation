Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(k):
        a.pop(0)
        a.append(0)
    print(' '.join(map(str, a)))

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(k):
        a.pop(0)
        a.append(0)
    print(" ".join(map(str, a)))

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    for _ in range(k):
        a.pop(0)
        a.append(0)
    print(' '.join(map(str, a)))

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    for _ in range(k):
        a.append(a.pop(0))
    print(' '.join([str(x) for x in a]))

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A = A[K:] + [0] * K
    print(*A)

=======
Suggestion 6

def main():
  n, k = map(int, input().split())
  a = list(map(int, input().split()))
  for i in range(k):
    a.append(a.pop(0))
    a.append(0)
  print(' '.join(map(str, a)))

=======
Suggestion 7

def main():
    n,k = map(int,raw_input().split())
    a = map(int,raw_input().split())

    for i in range(k):
        a.append(a.pop(0))

    print ' '.join(map(str,a))

=======
Suggestion 8

def solution():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    for i in range(k):
        a.append(0)
        a.pop(0)
    print(*a)

solution()

=======
Suggestion 9

def get_input():
    input = raw_input()
    return input
