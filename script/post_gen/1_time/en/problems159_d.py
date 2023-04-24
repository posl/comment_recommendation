Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    count = [0] * (N + 1)
    for i in range(N):
        count[A[i]] += 1
    ans = [0] * N
    for i in range(N):
        ans[i] = N - 1 - count[A[i]]
    for i in range(N):
        print(ans[i])

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A_count = [0] * (N + 1)
    for i in range(N):
        A_count[A[i]] += 1
    total = 0
    for i in range(1, N + 1):
        total += A_count[i] * (A_count[i] - 1) // 2
    for i in range(N):
        print(total - (A_count[A[i]] - 1))

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * (N + 1)
    for a in A:
        B[a] += 1
    ans = 0
    for b in B:
        ans += b * (b - 1) // 2
    for a in A:
        print(ans - B[a] + 1)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int,input().split()))
    cnt = [0] * (N+1)
    for i in range(N):
        cnt[A[i]] += 1
    ans = [0] * (N+1)
    for i in range(1,N+1):
        ans[i] = cnt[i]*(cnt[i]-1)//2
    total = sum(ans)
    for i in range(N):
        print(total-ans[A[i]]+1)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = [0 for i in range(N + 1)]
    for a in A:
        cnt[a] += 1
    ans = [0 for i in range(N)]
    for i in range(N):
        ans[i] = N - 1 - cnt[A[i]]
    for i in range(N):
        if cnt[A[i]] > 1:
            ans[i] += cnt[A[i]] * (cnt[A[i]] - 1) // 2
    print(*ans, sep='
')

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int,input().split()))
    B = [0] * (N+1)
    for a in A:
        B[a] += 1
    ans = [0] * N
    for i in range(N):
        ans[i] = B[A[i]] - 1
    for a in ans:
        print(a)

=======
Suggestion 7

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    C = [0] * N
    for a in A:
        C[a-1] += 1
    S = sum([c*(c-1)//2 for c in C])
    for a in A:
        print(S - (C[a-1]-1))

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    
    count = [0] * (N+1)
    for a in A:
        count[a] += 1

    ans = [0] * N
    for i in range(N):
        ans[i] = count[A[i]] - 1

    for a in A:
        print(ans[a])

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)
    B = [0] * (N+1)
    for i in range(N):
        B[A[i]] += 1
    #print(B)
    C = [0] * (N+1)
    for i in range(1, N+1):
        if B[i] > 1:
            C[i] = B[i] * (B[i]-1) // 2
    #print(C)
    for i in range(N):
        ans = 0
        ans += C[A[i]]
        ans -= B[A[i]] - 1
        print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    A = [int(a) for a in input().split()]
    A = [0] + A
    B = [0] * (N + 1)
    for i in range(1, N + 1):
        B[A[i]] += 1
    C = [0] * (N + 1)
    for i in range(1, N + 1):
        C[i] = B[i] * (B[i] - 1) // 2
    for i in range(1, N + 1):
        print(sum(C) - C[A[i]] + (B[A[i]] - 1) * (B[A[i]] - 2) // 2)
