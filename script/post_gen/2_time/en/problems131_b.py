Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, L = map(int, input().split())
    if L >= 0:
        print(sum(range(L, L+N-1)))
    elif L+N-1 <= 0:
        print(sum(range(L+1, L+N)))
    else:
        print(sum(range(L, L+N-1))-L)

main()

=======
Suggestion 2

def main():
    N, L = map(int, input().split())
    A = [L + i - 1 for i in range(1, N + 1)]
    print(sum(A) - min(A, key=abs))

=======
Suggestion 3

def main():
    n, l = map(int, input().split())
    if l <= 0 <= l + n - 1:
        print(sum(range(l, l + n)))
    elif l > 0:
        print(sum(range(l, l + n - 1)))
    else:
        print(sum(range(l + 1, l + n)))

=======
Suggestion 4

def main():
    N, L = map(int, input().split())
    if L > 0:
        print(sum(range(L, L+N)))
    elif L+N-1 < 0:
        print(sum(range(L, L+N)))
    else:
        print(sum(range(L, L+N)) - L)

=======
Suggestion 5

def main():
    N, L = map(int, input().split())
    A = [L + i - 1 for i in range(1, N + 1)]
    if L <= 0 <= L + N - 1:
        print(sum(A))
    elif L + N - 1 < 0:
        print(sum(A) - A[-1])
    else:
        print(sum(A) - A[0])

=======
Suggestion 6

def main():
    N, L = map(int, input().split())
    apple = [L+i-1 for i in range(1, N+1)]
    if apple[0] >= 0:
        print(sum(apple[1:]))
    elif apple[-1] <= 0:
        print(sum(apple[:-1]))
    else:
        print(sum(apple[:apple.index(0)])+sum(apple[apple.index(0)+1:]))

=======
Suggestion 7

def main():
    N, L = map(int, input().split())
    ans = 0
    if L <= 0 <= L + N - 1:
        ans = sum(range(L, L + N))
    elif L > 0:
        ans = sum(range(L, L + N - 1))
    else:
        ans = sum(range(L + 1, L + N))
    print(ans)

=======
Suggestion 8

def main():
    N, L = map(int, input().split())
    apple = [L + i - 1 for i in range(1, N + 1)]
    apple.sort()
    print(sum(apple) - apple[0])

main()

=======
Suggestion 9

def main():
    N, L = map(int, input().split())
    ans = 0
    if L <= 0 <= L+N-1:
        ans = 0
    elif L+N-1 < 0:
        ans = sum(range(L, L+N))
    elif 0 < L:
        ans = sum(range(L, L+N-1))
    print(ans)

main()

=======
Suggestion 10

def main():
    N, L = map(int, input().split())
    flv = [L + i - 1 for i in range(1, N + 1)]
    minflv = min(flv)
    print(sum(flv) - minflv)
