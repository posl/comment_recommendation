Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    cnt = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if A[i] != A[j] and A[j] != A[k] and A[k] != A[i]:
                    if A[i] + A[j] > A[k]:
                        cnt += 1
    print(cnt)

=======
Suggestion 2

def solve():
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()
    A.append(0)
    ans = 0
    cnt = 1
    for i in range(N):
        if A[i] == A[i+1]:
            cnt += 1
        else:
            ans += cnt*(cnt-1)*(cnt-2)//6
            cnt = 1
    print(ans)

=======
Suggestion 3

def solve():
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()
    res = 0
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                if A[i] != A[j] and A[j] != A[k] and A[k] != A[i]:
                    res += 1
    print(res)
    return 0

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                if A[i] != A[j] and A[j] != A[k] and A[i] != A[k]:
                    if A[i] + A[j] > A[k]:
                        ans += 1
                    else:
                        break
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = [0] * (10 ** 5 + 1)
    for i in range(n):
        cnt[a[i]] += 1
    ans = 0
    for i in range(1, 10 ** 5 + 1):
        ans += cnt[i] * (cnt[i] - 1) * (cnt[i] - 2) // 6
    for i in range(1, 10 ** 5 + 1):
        ans += cnt[i] * (cnt[i] - 1) // 2 * (n - cnt[i])
    for i in range(1, 10 ** 5 + 1):
        ans += cnt[i] * (cnt[i] - 1) // 2 * (cnt[i] - 2) // 3
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            if a[i] == a[j]:
                continue
            for k in range(j+1, n):
                if a[j] == a[k]:
                    continue
                if a[k] > a[i] + a[j]:
                    break
                ans += 1
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a = list(set(a))
    n = len(a)
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            ans += n - j - 1
    print(ans)
main()

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    C = [0] * (10**5+1)
    for a in A:
        C[a] += 1
    ans = 0
    for i in range(1, 10**5):
        if C[i] == 0:
            continue
        for j in range(i+1, 10**5+1):
            if C[j] == 0:
                continue
            for k in range(j+1, 10**5+1):
                if C[k] == 0:
                    continue
                ans += C[i] * C[j] * C[k]
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            if A[i] == A[j]:
                continue
            for k in range(j+1, N):
                if A[j] == A[k]:
                    continue
                if A[i] == A[k]:
                    continue
                if A[i] + A[j] > A[k]:
                    ans += 1
    print(ans)

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a.append(0)
    ans = 0
    num = 1
    for i in range(n):
        if a[i] == a[i+1]:
            num += 1
        else:
            ans += (n-i-1)*(n-i-2)//2*num
            num = 1
    print(ans)
