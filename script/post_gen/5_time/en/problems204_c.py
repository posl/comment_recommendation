Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    ans = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i == j:
                continue
            if A.count(i) > 0 and B.count(j) > 0:
                ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N,M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i],B[i] = map(int, input().split())
    print(N*(N-1)//2 - M)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    print(N * (N - 1) // 2 - M)

=======
Suggestion 4

def main():
    N,M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    ans = 0
    for i in range(1,N+1):
        for j in range(1,N+1):
            if i == j:
                ans += 1
            else:
                for k in range(M):
                    if AB[k][0] == i and AB[k][1] == j:
                        break
                else:
                    ans += 1
    print(ans)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    print(N**2 - N - M)

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    print(n**2 - m)

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    print(n**2 - n - 2*m)

=======
Suggestion 8

def main():
    n,m = map(int, input().split())
    if m == 0:
        print(n)
        return
    else:
        print(n*(n-1)//2 - m)

=======
Suggestion 9

def solve():
    N,M = map(int,input().split())
    if M == 0:
        print(N)
        return
    else:
        ans = 0
        for i in range(1,N+1):
            ans += i
        print(ans)

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    print(N**2-M)
