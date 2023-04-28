Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        B[A[i]-1] += 1
    for i in range(N):
        print(sum([1 for j in range(N) if B[j] > B[i]])+1)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * N
    cnt = [0] * N
    for i in range(N):
        cnt[A[i]-1] += 1
    for i in range(N):
        ans[cnt[i]-1] += 1
    for i in range(N):
        print(ans[i])

=======
Suggestion 3

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = [0] * N
    ans[0] = 1
    for i in range(1, N):
        if A[i] != A[i-1]:
            ans[i] = ans[i-1] + 1
        else:
            ans[i] = ans[i-1]
    for i in range(N):
        print(ans[i]-1)
    return 0

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    count = [0]*n
    for i in a:
        count[i-1] += 1
    for i in count:
        print(i)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    K = [0] * N
    for i in range(N):
        K[i] = A.count(A[i])
    ans = [0] * N
    for i in range(N):
        ans[i] = N - sum(K[:i])
    for i in ans:
        print(i)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = [0] * N
    cnt = 0
    for i in range(N):
        if i == 0:
            ans[i] = 1
            cnt = 1
        else:
            if A[i] != A[i-1]:
                ans[i] = cnt
                cnt = 1
            else:
                cnt += 1
    ans[N-1] = cnt
    ans = ans[::-1]
    ans2 = [0] * N
    ans2[0] = ans[0]
    for i in range(1, N):
        ans2[i] = ans2[i-1] + ans[i]
    ans2 = ans2[::-1]
    for i in range(N):
        print(ans2[i])

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A.append(-1)
    ans = [0] * N
    cnt = 1
    for i in range(N):
        if A[i] != A[i + 1]:
            ans[cnt - 1] += 1
            cnt = 1
        else:
            cnt += 1
    for i in range(N):
        print(ans[i])

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = [0] * n
    ans[0] = n - 1
    cnt = 1
    for i in range(1, n):
        if a[i] == a[i - 1]:
            cnt += 1
        else:
            cnt = 1
        ans[i] = n - i - 1 - cnt
    for i in range(n):
        print(ans[i])

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A.append(0)
    K = 0
    ans = 0
    for i in range(N):
        if A[i] != A[i+1]:
            ans += 1
            K = 0
        else:
            K += 1
        print(ans)

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a.append(-1)
    k = 0
    c = 1
    ans = [0] * n
    for i in range(n):
        if a[i] != a[i+1]:
            ans[k] = c
            k += 1
            c = 1
        else:
            c += 1
    print(*ans, sep="\n")
