Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                if A[i] != A[j] and A[j] != A[k]:
                    ans += 1
                elif A[i] == A[j] and A[j] != A[k]:
                    ans += 1
                elif A[i] != A[j] and A[j] == A[k]:
                    ans += 1
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            if a[i] == a[j]:
                continue
            for k in range(j+1, n):
                if a[j] == a[k]:
                    continue
                if a[i] == a[k]:
                    continue
                if a[i] + a[j] > a[k]:
                    ans += 1
                else:
                    break
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if a[i] != a[j] and a[j] != a[k] and a[i] != a[k]:
                    if a[i] + a[j] > a[k]:
                        ans += 1
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if a[i] != a[j] and a[j] != a[k] and a[k] != a[i]:
                    if a[i] + a[j] > a[k]:
                        ans += 1
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    cnt = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if a[i] != a[j] and a[j] != a[k]:
                    if a[i] + a[j] > a[k]:
                        cnt += 1
    print(cnt)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    cnt = [0] * (10 ** 6 + 1)
    for j in range(n):
        cnt[a[j]] += 1
    for i in range(1, 10 ** 6 + 1):
        ans += cnt[i] * (cnt[i] - 1) * (cnt[i] - 2) // 6
    for i in range(1, 10 ** 6 + 1):
        ans += cnt[i] * (cnt[i] - 1) // 2 * (n - cnt[i])
    for i in range(1, 10 ** 6 + 1):
        ans += cnt[i] * (cnt[i] - 1) // 2 * (cnt[i] - 2) // 3
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    sum = 0
    for i in range(n):
        for j in range(i+1, n):
            sum += (a[i] * a[j]) % 1000000007
    print(sum % 1000000007)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    B = [0] * (2*10**5+1)
    for i in range(N):
        B[A[i]] += 1
    ans = 0
    for i in range(2*10**5+1):
        if B[i] >= 3:
            ans += B[i]*(B[i]-1)*(B[i]-2)//6
        if B[i] >= 2:
            for j in range(i+1, 2*10**5+1):
                if B[j] >= 2:
                    ans += B[i]*B[j]*(B[j]-1)//2
        if B[i] >= 1:
            for j in range(i+1, 2*10**5+1):
                if B[j] >= 1:
                    ans += B[i]*B[j]*B[j]
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A = [0] + A
    cnt = [0] * (2 * 10 ** 5 + 1)
    for i in range(1, N + 1):
        cnt[A[i]] += 1
    for i in range(1, 2 * 10 ** 5 + 1):
        cnt[i] += cnt[i - 1]
    ans = 0
    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            if 2 * A[j] - A[i] > 2 * 10 ** 5:
                break
            ans += cnt[2 * A[j] - A[i]] - cnt[A[j]]
    print(ans)

=======
Suggestion 10

def nC2(n):
    return n*(n-1)//2

N = int(input())
A = list(map(int,input().split()))
A.sort()
