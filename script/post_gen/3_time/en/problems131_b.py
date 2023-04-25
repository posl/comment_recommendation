Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, L = map(int, input().split())
    if L <= 0 and L+N-1 >= 0:
        print(sum(range(L, L+N)))
    elif L <= 0 and L+N-1 < 0:
        print(sum(range(L, L+N-1)))
    else:
        print(sum(range(L+1, L+N)))

=======
Suggestion 2

def main():
    N, L = map(int, input().split())
    A = [L + i - 1 for i in range(1, N + 1)]
    if 0 in A:
        print(sum(A))
    elif L >= 0:
        print(sum(A) - A[0])
    elif L < 0 and L + N - 1 >= 0:
        print(sum(A))
    else:
        print(sum(A) - A[-1])

=======
Suggestion 3

def main():
    N, L = map(int, input().split())
    if L <= 0 and L+N-1 >= 0:
        print(sum([i for i in range(L, L+N)]))
    elif L <= 0 and L+N-1 < 0:
        print(sum([i for i in range(L, L+N)]) - L+N-1)
    elif L > 0:
        print(sum([i for i in range(L, L+N)]) - L)

=======
Suggestion 4

def main():
    n, l = map(int, input().split())
    if l <= 0 and 0 <= l+n-1:
        print(sum(range(l, l+n)))
    elif l+n-1 < 0:
        print(sum(range(l, l+n-1)))
    else:
        print(sum(range(l+1, l+n)))

=======
Suggestion 5

def main():
    N, L = map(int, input().split())
    apple = [L+i-1 for i in range(1, N+1)]
    if L <= 0 and 0 <= L+N-1:
        print(sum(apple)-0)
    elif L < 0:
        print(sum(apple)-apple[0])
    else:
        print(sum(apple)-apple[-1])

=======
Suggestion 6

def main():
    N, L = map(int, input().split())
    ans = sum([i+L-1 for i in range(1, N+1)])
    if L <= 0 <= L+N-1:
        print(ans)
    elif L+N-1 < 0:
        print(ans - (L+N-1))
    else:
        print(ans - L)

=======
Suggestion 7

def main():
    N, L = map(int, input().split())
    apple = [L + i - 1 for i in range(1, N + 1)]
    apple.sort()
    if L >= 0:
        print(sum(apple) - apple[0])
    elif L + N - 1 <= 0:
        print(sum(apple) - apple[-1])
    else:
        print(sum(apple))

main()

=======
Suggestion 8

def main():
    N, L = map(int, input().split())
    print(N * (2 * L + N - 1) // 2 - L - max(0, L + N - 1))

=======
Suggestion 9

def main():
    import sys
    readline = sys.stdin.readline
    N, L = map(int, readline().split())
    apple = [L+i-1 for i in range(1, N+1)]
    if 0 in apple:
        print(sum(apple))
    else:
        if max(apple) > 0:
            print(sum(apple)-max(apple))
        else:
            print(sum(apple)-min(apple))

=======
Suggestion 10

def main():
    N, L = map(int, input().split())
    print(sum(range(L, L+N)) - (L-1 if L <= 0 <= L+N-1 else (L+N-1 if 0 <= L+N-1 else 0)))
