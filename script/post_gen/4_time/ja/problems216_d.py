Synthesizing 3/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    k = [0] * m
    a = [[] for _ in range(m)]
    for i in range(m):
        k[i] = int(input())
        a[i] = list(map(int, input().split()))
        for j in range(k[i]):
            a[i][j] -= 1
    #print(k)
    #print(a)
    #print()
    #print()
    #print()

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    #print(N, M)
    #
