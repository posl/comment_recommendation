Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    cnt = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            if A[i] == A[j]:
                continue
            for k in range(j+1, N):
                if A[j] == A[k]:
                    continue
                cnt += 1
    print(cnt)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for i in range(n):
        if a[i] in d:
            d[a[i]] += 1
        else:
            d[a[i]] = 1
    s = 0
    for i in d:
        s += d[i] * (d[i] - 1) * (d[i] - 2) // 6
    for i in range(n):
        s -= (d[a[i]] - 1) * (d[a[i]] - 2) // 2
    print(s)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A.append(0)
    ans = 0
    a = 0
    b = 0
    for i in range(N):
        if A[i] == A[i+1]:
            b += 1
        else:
            ans += b*(b+1)*(b-1)//6
            a += b*(b-1)//2
            b = 0
    for i in range(N):
        if A[i] == A[i+1]:
            b += 1
        else:
            ans -= b*(b+1)*(b-1)//6
            b = 0
    ans += a*(a-1)//2
    print(ans)

=======
Suggestion 4

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
                if a[i] == a[k] or a[j] == a[k]:
                    continue
                ans += 1
    print(ans)

=======
Suggestion 5

def solve():
    n = int(input())
    a = [int(i) for i in input().split()]
    cnt = [0] * (2 * 10**5 + 1)
    for i in range(n):
        cnt[a[i]] += 1
    ans = 0
    for i in range(1, 2 * 10**5 + 1):
        if cnt[i] >= 2:
            ans += cnt[i] * (cnt[i] - 1) * (cnt[i] - 2) // 6
        if cnt[i] >= 1:
            for j in range(i + 1, 2 * 10**5 + 1):
                ans += cnt[i] * cnt[j] * (cnt[j] - 1) // 2
    print(ans)

solve()

=======
Suggestion 6

def main():
    N=int(input())
    A=list(map(int,input().split()))
    A.sort()
    #print(A)
    ans=0
    for i in range(N-2):
        for j in range(i+1,N-1):
            if A[i]==A[j]:
                continue
            for k in range(j+1,N):
                if A[i]==A[k] or A[j]==A[k]:
                    continue
                ans+=1
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] == a[j]:
                continue
            for k in range(j + 1, n):
                if a[j] == a[k]:
                    continue
                ans += 1
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for i in range(n):
        if a[i] in d:
            d[a[i]] += 1
        else:
            d[a[i]] = 1

    # print(d)
    ans = 0
    for i in d:
        ans += d[i] * (d[i] - 1) * (d[i] - 2) // 6

    for i in range(n):
        ans -= (d[a[i]] - 1) * (d[a[i]] - 2) // 2
    print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    ans = 0
    for i in d:
        ans += d[i] * (d[i] - 1) * (d[i] - 2) // 6
    for i in range(n):
        ans += (d[a[i]] - 1) * (d[a[i]] - 2) // 2
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] == a[j]:
                continue
            ans += (d[a[i]] - 1) * (d[a[j]] - 1)
    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if A[i] != A[j] and A[j] != A[k] and A[i] != A[k]:
                    if A[i] + A[j] > A[k] and A[j] + A[k] > A[i] and A[k] + A[i] > A[j]:
                        ans += 1
    print(ans)
