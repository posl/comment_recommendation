Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

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
Suggestion 2

def solve(n, a):
    ans = 0
    for i in range(n):
        for j in range(i, n):
            x = min(a[i:j+1])
            ans = max(ans, x*(j-i+1))
    return ans

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    # l, r, xを全探索する
    for l in range(N):
        for r in range(l, N):
            for x in range(1, 1001):
                # 条件を満たすかどうか
                ok = True
                for i in range(l, r+1):
                    if A[i] < x:
                        ok = False
                # 条件を満たした場合、ansを更新する
                if ok:
                    ans = max(ans, x*(r-l+1))
    print(ans)

=======
Suggestion 4

def max_orange(n, a):
    ans = 0
    for l in range(n):
        min_orange = a[l]
        for r in range(l, n):
            min_orange = min(min_orange, a[r])
            ans = max(ans, min_orange * (r - l + 1))
    return ans

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        l = i
        r = i
        x = A[i]
        while l > 0 and A[l-1] >= x:
            l -= 1
        while r < N-1 and A[r+1] >= x:
            r += 1
        ans = max(ans, x*(r-l+1))
    print(ans)

=======
Suggestion 6

def solve():
    N = int(input())
    A = list(map(int,input().split()))
    ans = 0
    for i in range(N):
        for j in range(i,N):
            x = min(A[i:j+1])
            ans = max(ans,x*(j-i+1))
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for l in range(n):
        x = a[l]
        for r in range(l, n):
            x = min(x, a[r])
            ans = max(ans, x * (r - l + 1))
    print(ans)

=======
Suggestion 8

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
Suggestion 9

def main():
    n = int(input())
    a = list(map(int,input().split()))
    ans = 0
    for i in range(n):
        for j in range(i,n):
            tmp = min(a[i:j+1])
            ans = max(ans, tmp*(j-i+1))
    print(ans)
