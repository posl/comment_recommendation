Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N, L = map(int, input().split())
    taste = [L + i for i in range(N)]
    print(sum(taste) - min(taste, key=abs))

=======
Suggestion 2

def main():
    n, l = map(int, input().split())
    s = 0
    for i in range(1, n+1):
        s += l + i - 1
    if s > 0:
        print(s - l)
    else:
        print(s - l + n - 1)

=======
Suggestion 3

def main():
    N, L = map(int, input().split())
    print(sum(range(L + 1, L + N)) - min(range(L + 1, L + N), key=abs))

=======
Suggestion 4

def main():
    N, L = map(int, input().split())
    if L > 0:
        print((N-1)*L - N*(N-1)//2)
    elif L < 0:
        print((N-1)*L + N*(N-1)//2)
    else:
        print(N*L)

=======
Suggestion 5

def main():
    n, l = map(int, input().split())
    l += 1
    ans = 0
    for i in range(1, n):
        ans += l + i - 1
    print(ans)

=======
Suggestion 6

def main():
    N, L = map(int, input().split())
    apple_pie = 0
    min_diff = 10000
    for i in range(1, N+1):
        apple = L + i - 1
        apple_pie = apple_pie + apple
        if min_diff > abs(apple):
            min_diff = abs(apple)
            min_apple = apple
    print(apple_pie - min_apple)

=======
Suggestion 7

def main():
    N, L = map(int, input().split())
    if L > 0:
        print((N * L + N * (N - 1)) // 2 - L)
    elif N + L <= 0:
        print((N * L + N * (N - 1)) // 2 - L - N + 1)
    else:
        print((N * L + N * (N - 1)) // 2)

=======
Suggestion 8

def myfun(n,l):
    return sum([l+i for i in range(n)])

=======
Suggestion 9

def main():
    pass
