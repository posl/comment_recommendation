Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    a = list(map(int, input().split()))
    ans = []
    for i in range(N, 0, -1):
        cnt = 0
        for j in range(i, N+1, i):
            if j in ans:
                cnt += 1
        if cnt % 2 != a[i-1]:
            ans.append(i)
    print(len(ans))
    print(*ans)

=======
Suggestion 2

def main():
    N = int(input())
    a = list(map(int, input().split()))
    b = [0] * N
    for i in range(N - 1, -1, -1):
        if sum(b[i::i + 1]) % 2 != a[i]:
            b[i] = 1
    print(sum(b))
    print(*[i + 1 for i in range(N) if b[i] == 1])

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N-1, -1, -1):
        if sum(B[i::i+1]) % 2 != A[i]:
            B[i] = 1
    print(sum(B))
    print(*[i+1 for i in range(N) if B[i] == 1])

=======
Suggestion 4

def main():
    N = int(input())
    a = list(map(int, input().split()))
    b = []
    for i in range(N, 0, -1):
        s = 0
        for j in range(i, N+1, i):
            s += a[j-1]
        if s%2 != a[i-1]:
            b.append(i)
    print(len(b))
    print(*b)

=======
Suggestion 5

def main():
    N = int(input())
    a = list(map(int, input().split()))
    ans = []
    for i in range(N):
        if a[N-i-1] == 1:
            ans.append(N-i)
            for j in range(1, N//ans[-1]+1):
                a[ans[-1]*j-1] = 1 - a[ans[-1]*j-1]
    print(len(ans))
    for i in range(len(ans)):
        print(ans[len(ans)-i-1], end=' ')
    print()

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = []
    for i in range(N):
        if A[N - i - 1] == 1:
            ans.append(N - i)
            for j in range(2, (N - i) // 2 + 1):
                if (N - i) % j == 0:
                    A[j - 1] = (A[j - 1] + 1) % 2
    print(len(ans))
    print(*ans)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = []
    for i in range(n):
        if a[n-1-i] == 1:
            ans.append(n-i)
            for j in range(1, n//ans[-1]+1):
                a[ans[-1]*j-1] = 1 - a[ans[-1]*j-1]
    print(len(ans))
    print(*ans)

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = []
    for i in range(n):
        if a[n-i-1] == 1:
            for j in range(2*(n-i-1)+1, n+1, n-i-1):
                a[j-1] = 1 - a[j-1]
            ans.append(n-i)
    print(len(ans))
    print(*ans)

=======
Suggestion 9

def main():
    N = int(input())
    a = list(map(int, input().split()))
    ans = []
    for i in range(N):
        if a[N - i - 1] == 1:
            if sum(a[N - i - 1::N - i]) % 2 == 0:
                ans.append(N - i)
    print(len(ans))
    print(*ans)

=======
Suggestion 10

def main():
    N = int(input())
    a = list(map(int, input().split()))
    #print(N)
    #print(a)
    b = []
    for i in range(N):
        if a[i] == 1:
            b.append(i+1)
    print(len(b))
    for i in range(len(b)):
        print(b[i])
