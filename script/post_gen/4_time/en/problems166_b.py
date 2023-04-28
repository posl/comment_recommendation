Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    a = [0] * n
    for i in range(k):
        d = int(input())
        for j in map(int, input().split()):
            a[j - 1] += 1
    print(a.count(0))

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    Snuke = [0] * N
    for i in range(K):
        d = int(input())
        A = list(map(int, input().split()))
        for j in range(d):
            Snuke[A[j] - 1] += 1
    print(Snuke.count(0))

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    S = [0] * N
    for i in range(K):
        d = int(input())
        A = list(map(int, input().split()))
        for j in range(d):
            S[A[j] - 1] = 1
    print(S.count(0))

=======
Suggestion 4

def main():
    # input
    N, K = map(int, input().split())
    d = []
    A = []
    for i in range(K):
        d.append(int(input()))
        A.append(list(map(int, input().split())))

    # compute
    snukes = [0]*N
    for i in range(K):
        for j in range(d[i]):
            snukes[A[i][j]-1] = 1

    # output
    print(sum(snukes))

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    d = [0] * n
    for _ in range(k):
        for a in map(int, input().split()):
            d[a - 1] += 1
    print(sum(1 for i in range(n) if d[i] == 0))

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    A = []
    for _ in range(K):
        d = int(input())
        A += map(int, input().split())
    print(N - len(set(A)))

=======
Suggestion 7

def main():
    input_list = input().split()
    N = int(input_list[0])
    K = int(input_list[1])
    d = []
    A = []
    for i in range(K):
        d.append(int(input()))
        A.append(input().split())
    print(N - K)

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    d = []
    for i in range(K):
        d.append(input())
        d.append(input())
    print(N - d.count("1"))

=======
Suggestion 9

def main():
    # Get Input
    N, K = map(int, input().split())
    d = []
    for i in range(K):
        d.append(int(input()))
    A = []
    for i in range(K):
        A.append([int(x) for x in input().split()])
    
    # Solve
    ans = 0
    for i in range(N):
        for j in range(K):
            if (i+1) in A[j]:
                break
            if j == K-1:
                ans += 1
    
    # Output
    print(ans)

=======
Suggestion 10

def main():
    n, k = map(int, input().split())
    d = [0 for i in range(n)]
    for i in range(k):
        di = int(input())
        d = [d[j] + 1 if j+1 in map(int, input().split()) else d[j] for j in range(n)]
    print(d.count(0))
