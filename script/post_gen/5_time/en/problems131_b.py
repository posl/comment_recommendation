Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, l = map(int, input().split())
    if l >= 0:
        print(sum(range(l+1, l+n)))
    elif l+n <= 0:
        print(sum(range(l, l+n-1, -1)))
    else:
        print(sum(range(l, l+n)))

=======
Suggestion 2

def main():
    N, L = map(int, input().split())
    if L > 0:
        print((N-1)*L + N*(N-1)//2)
    elif L+N-1 < 0:
        print(N*L + N*(N-1)//2)
    else:
        print(N*L + N*(N-1)//2 - (L+N-1))

=======
Suggestion 3

def main():
    N, L = map(int, input().split())
    if L >= 0:
        print((N-1)*L + N*(N-1)//2)
    elif L + N - 1 < 0:
        print((N-1)*L + N*(N-1)//2 - L - N + 1)
    else:
        print((N-1)*L + N*(N-1)//2)

=======
Suggestion 4

def main():
    n, l = map(int, input().split())

    if l >= 0:
        print(sum(range(l+1, l+n)))
    elif -l < n:
        print(sum(range(l, l+n)))
    else:
        print(sum(range(l, l+n-1)))

=======
Suggestion 5

def solve():
    n, l = map(int, input().split())
    if l > 0:
        print((2 * l + n - 1) * n // 2 - l)
    elif l + n - 1 < 0:
        print((2 * l + n - 1) * n // 2 - l - n + 1)
    else:
        print((2 * l + n - 1) * n // 2 - l)

=======
Suggestion 6

def main():
    n, l = map(int, input().split())
    print(sum(range(l + 1, l + n)) - min(range(l + 1, l + n), key=abs))

=======
Suggestion 7

def solve():
    N, L = map(int, input().split())
    print(sum(range(L+1, L+N)) - min(range(L+1, L+N), key=abs))

=======
Suggestion 8

def main():
    N, L = map(int, input().split())
    apples = [L+i for i in range(N)]
    if L >= 0:
        print(sum(apples) - apples[0])
    elif L < 0 and L+N-1 >= 0:
        print(sum(apples))
    else:
        print(sum(apples) - apples[-1])

=======
Suggestion 9

def main():
    n, l = [int(x) for x in input().split()]
    if l >= 0:
        print(sum([l+i for i in range(1, n)]))
    elif -l >= n:
        print(sum([l+i for i in range(1, n)]))
    else:
        print(sum([l+i for i in range(1, n)])-min([l+i for i in range(1, n)]))

=======
Suggestion 10

def solve(n, l):
    return sum(l) - min(l, key=abs)
