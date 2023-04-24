Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))

    ans = 0
    for l in range(N):
        x = A[l]
        for r in range(l, N):
            x = min(x, A[r])
            ans = max(ans, x * (r - l + 1))
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(i, N):
            x = min(A[i:j+1])
            ans = max(ans, x*(j-i+1))
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for x in range(1, 10 ** 5 + 1):
        l = 0
        r = 0
        cnt = 0
        while r < N:
            if A[r] >= x:
                r += 1
                cnt += 1
            else:
                ans = max(ans, x * cnt)
                while l < r:
                    if A[l] >= x:
                        l += 1
                        cnt -= 1
                    else:
                        l += 1
                        break
    print(max(ans, x * cnt))

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))

    ans = 0
    for x in range(1, 10**5+1):
        l = 0
        r = 0
        cnt = 0
        while l <= r and r < N:
            if A[l] >= x:
                cnt += 1
                l += 1
            elif A[r] >= x:
                cnt += 1
                r += 1
            else:
                l += 1
                r += 1
            ans = max(ans, cnt*x)
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))

    ans = 0
    for x in range(1, 10**5+1):
        l = 0
        r = 0
        tmp = 0
        while r < N:
            if A[r] < x:
                if r == l:
                    r += 1
                    l += 1
                else:
                    tmp -= A[l]
                    l += 1
            else:
                tmp += A[r]
                r += 1
            if tmp >= x:
                ans += 1
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(i, N):
            for k in range(1, 10**5+1):
                if all([A[l] >= k for l in range(i, j+1)]):
                    ans = max(ans, k*(j-i+1))
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        l = a[i]
        for j in range(i, n):
            l = min(l, a[j])
            ans = max(ans, l * (j - i + 1))
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for l in range(n):
        x = 10**5
        for r in range(l,n):
            x = min(x,a[r])
            ans = max(ans,x*(r-l+1))
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        m = 10**5
        for j in range(i, N):
            m = min(m, A[j])
            ans = max(ans, m * (j - i + 1))
    print(ans)
