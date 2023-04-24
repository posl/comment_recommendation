Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n):
        b[a[i] - 1] += 1
    for i in range(n):
        print(sum(b) - b[a[i] - 1] - 1)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    count = [0] * (N+1)
    for a in A:
        count[a] += 1
    ans = [0] * N
    for i in range(1,N+1):
        ans[i-1] = count[i] * (count[i]-1) // 2
    for a in A:
        print(sum(ans) - ans[a-1])

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = [0] * (N+1)
    for a in A:
        cnt[a] += 1
    total = 0
    for c in cnt:
        if c > 1:
            total += c * (c-1) // 2
    for a in A:
        print(total - (cnt[a] - 1))

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = [0] * (n + 1)
    for i in a:
        cnt[i] += 1
    ans = 0
    for i in cnt:
        ans += i * (i - 1) // 2
    for i in a:
        print(ans - cnt[i] + 1)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = [0 for _ in range(N+1)]
    for a in A:
        cnt[a] += 1
    ans = [0 for _ in range(N)]
    for i in range(N):
        ans[i] = sum(cnt) - cnt[A[i]]
    for a in ans:
        print(a//2)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int,input().split()))
    count = [0]*(N+1)
    for a in A:
        count[a] += 1
    ans = 0
    for c in count:
        ans += c*(c-1)//2
    for a in A:
        print(ans-count[a]+1)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [0] + A
    cnt = [0] * (N + 1)
    for i in range(1, N + 1):
        cnt[A[i]] += 1
    ans = [0] * (N + 1)
    for i in range(1, N + 1):
        ans[i] = (cnt[A[i]] - 1) * (N - cnt[A[i]]) + cnt[A[i]] * (cnt[A[i]] - 1) // 2
    for i in range(1, N + 1):
        print(ans[i])

=======
Suggestion 8

def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    count = [0]*(N+1)
    for i in A:
        count[i] += 1
    ans = [0]*(N+1)
    for i in range(1,N+1):
        ans[i] = count[i]*(count[i]-1)//2
    for i in range(1,N+1):
        print(sum(ans)-ans[A[i-1]]+count[A[i-1]]-1)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(A)
    #print(N)
    B = [0 for i in range(N+1)]
    for i in range(N):
        B[A[i]] += 1
    #print(B)
    C = [0 for i in range(N+1)]
    for i in range(1,N+1):
        C[i] = B[i]*(B[i]-1)//2
    #print(C)
    D = sum(C)
    for i in range(N):
        print(D-C[A[i]]+(B[A[i]]-1))

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    # Aの要素の個数をカウント
    A_count = [0] * (N+1)
    for a in A:
        A_count[a] += 1
    # 答えを求めて出力
    for a in A:
        print(sum(A_count) - A_count[a] - 1)
