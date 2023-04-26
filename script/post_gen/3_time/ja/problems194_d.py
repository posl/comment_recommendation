Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    ans = 0
    for i in range(1,N):
        ans += N/(i*(N-i))
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    ans = 0
    for i in range(1, n):
        ans += (n / i)
    ans += n
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    ans = 0
    for i in range(1,N+1):
        ans += (i*(N/i))
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    print(N + (N - 1) / 2)

=======
Suggestion 5

def main():
    N = int(input())
    print(2 * N - 2)

=======
Suggestion 6

def main():
    N = int(input())
    print(2*(N-1)/(N*N))

=======
Suggestion 7

def main():
    n = int(input())
    print(n + (n-1)/2)

=======
Suggestion 8

def main():
    N = int(input())
    print(2.0 * N / (N - 1))

=======
Suggestion 9

def main():
    N = int(input())
    print(2*N - 1)

=======
Suggestion 10

def Graph(N):
    #グラフの作成
    graph = [[] for _ in range(N)]
    return graph
