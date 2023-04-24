Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, L = map(int, input().split())
    A = [L+i-1 for i in range(1, N+1)]
    print(sum(A) - min(A, key=abs))

=======
Suggestion 2

def main():
    N, L = map(int, input().split())
    if L <= 0 <= L + N - 1:
        print(sum(range(L, L + N)))
    elif L < L + N - 1:
        print(sum(range(L, L + N - 1)))
    else:
        print(sum(range(L + 1, L + N)))

=======
Suggestion 3

def main():
    N, L = map(int, input().split())
    apple = [L+i-1 for i in range(1, N+1)]
    if L <= 0 <= L+N-1:
        print(sum(apple)-0)
    elif L+N-1 < 0:
        print(sum(apple)-apple[-1])
    else:
        print(sum(apple)-apple[0])

=======
Suggestion 4

def main():
    n, l = map(int, input().split())
    a = [l + i - 1 for i in range(1, n + 1)]
    b = [abs(i) for i in a]
    c = sum(a)
    d = b.index(min(b))
    print(c - a[d])

=======
Suggestion 5

def main():
    N,L = map(int,input().split())
    if L <= 0 and L+N-1 >= 0:
        print(sum(range(L,L+N)))
    elif L <= 0 and L+N-1 < 0:
        print(sum(range(L,L+N-1)))
    else:
        print(sum(range(L+1,L+N)))

=======
Suggestion 6

def main():
    n, l = map(int, input().split())
    if l <= 0 and l + n > 0:
        print(sum(range(l, l + n)))
    elif l > 0:
        print(sum(range(l, l + n - 1)))
    else:
        print(sum(range(l + 1, l + n)))

=======
Suggestion 7

def main():
    N, L = map(int, input().split())
    print(sum([L + i for i in range(N)]) - max([L + i for i in range(N)]))

=======
Suggestion 8

def main():
    n, l = map(int, input().split())
    #print(n, l)
    a = [i for i in range(l, l+n)]
    #print(a)
    if 0 in a:
        print(sum(a))
    elif l > 0:
        print(sum(a)-a[0])
    elif l < 0 and l+n-1 >= 0:
        print(sum(a)-a[-1])
    else:
        print(sum(a)-a[-1])

=======
Suggestion 9

def main():
    N, L = map(int, input().split())
    print(N*(L-1)+N*(N+1)//2)

=======
Suggestion 10

def main():
    N, L = map(int, input().split())
    min =
