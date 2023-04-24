Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    for i in range(n):
        b.append(0)
    for i in range(n):
        b[a[i]-1] += 1
    for i in range(n):
        print(b[i])

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * (2 * 10**5 + 1)
    for i in range(n):
        b[a[i]] += 1
    ans = 0
    for i in range(2 * 10**5 + 1):
        ans += b[i] * (b[i] - 1) // 2
    for i in range(n):
        print(ans - (b[a[i]] - 1))

=======
Suggestion 3

def main():
    N = int(input())
    a = list(map(int, input().split()))
    b = []
    for i in range(N):
        b.append(0)
    for i in range(N):
        b[a[i]-1] += 1
    print(b.count(1))

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * (2 * 10**5 + 1)
    for i in range(N):
        B[A[i]] += 1
    ans = 0
    for i in range(2 * 10**5 + 1):
        ans += B[i] % 2
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    a = list(map(int, input().split()))
    ans = [0] * N
    ans[0] = 1
    for i in range(1, N):
        if a[i] == a[i - 1]:
            ans[i] = ans[i - 1]
        else:
            ans[i] = ans[i - 1] + 1
    for i in range(N - 1, 0, -1):
        if a[i] == a[i - 1]:
            ans[i - 1] = ans[i]
    print('\n'.join(map(str, ans)))

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * (N + 1)
    for i in range(N - 1, -1, -1):
        B[i] = B[i + 1] + A[i]
    C = [0] * (N + 1)
    for i in range(N - 1, -1, -1):
        C[i] = C[i + 1]
        if i + 1 < N and A[i] == A[i + 1]:
            C[i] += 1
    for i in range(N):
        if A[i] == 2:
            print(B[i + 1])
        else:
            print(B[i + 1] - C[i + 1])

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0 for _ in range(2 * 10 ** 5 + 1)]
    ans = 0
    for i in range(n):
        b[a[i]] += 1
        if b[a[i]] == 1:
            ans += 1
        else:
            ans -= 1
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.reverse()
    s = [0]*(n+1)
    for i in range(n):
        s[i+1] = s[i] + a[i]
    s.reverse()
    s = s[1:]
    #print(s)
    ans = [0]*n
    for i in range(n):
        ans[i] = s[i]
        for j in range(i+1, n):
            if ans[i] <= a[j]:
                ans[i] = ans[i]
            else:
                ans[i] = ans[i] + a[j]
    ans.reverse()
    for i in range(n):
        print(ans[i])

=======
Suggestion 9

def main():
    N = int(input())
    a = list(map(int, input().split()))
    b = [0]*N
    for i in range(N):
        b[a[i]-1] += 1
    print(sum(b))
    for i in range(N-1):
        b[a[i]-1] -= 1
        b[a[i+1]-1] += 1
        print(sum(b))

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))

    A.sort()
    A.append(0)

    ans = 0
    cnt = 1
    for i in range(N):
        if A[i] == A[i+1]:
            cnt += 1
        else:
            if cnt >= A[i]:
                ans += cnt - A[i]
            else:
                ans += cnt
            cnt = 1

    print(ans)
