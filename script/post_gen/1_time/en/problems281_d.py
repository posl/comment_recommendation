Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    S = set()
    for i in range(1 << N):
        if bin(i).count("1") == K:
            S.add(sum(A[j] for j in range(N) if (i >> j) & 1))
    ans = -1
    for i in sorted(S, reverse=True):
        if i % D == 0:
            ans = i
            break
    print(ans)

=======
Suggestion 2

def main():
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    S = set()
    for i in range(1 << N):
        if bin(i).count('1') == K:
            s = 0
            for j in range(N):
                if (i >> j) & 1:
                    s += A[j]
            S.add(s)
    S = sorted(list(S))
    if S[-1] < D:
        print(-1)
    else:
        for i in range(len(S)-1, -1, -1):
            if S[i] % D == 0:
                print(S[i])
                break

=======
Suggestion 3

def main():
    n, k, d = map(int, input().split())
    a = list(map(int, input().split()))
    s = set()
    for i in range(n):
        for j in range(i+1, n):
            s.add(a[i] + a[j])
    ans = -1
    for i in s:
        if i % d == 0:
            ans = max(ans, i)
    print(ans)

main()

=======
Suggestion 4

def main():
    import sys
    from itertools import combinations
    input = sys.stdin.readline
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    S = set()
    for comb in combinations(A, K):
        S.add(sum(comb))
    ans = -1
    for s in S:
        if s % D == 0:
            ans = max(ans, s)
    print(ans)

=======
Suggestion 5

def main():
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    S = set()
    for i in range(K):
        S |= {sum(A[j] for j in comb) for comb in combinations(range(N), i+1)}
    S = [s for s in S if s % D == 0]
    print(max(S) if S else -1)

=======
Suggestion 6

def main():
    n,k,d=map(int,input().split())
    a=list(map(int,input().split()))
    s=set()
    for i in range(n):
        for j in range(i+1,n):
            s.add(a[i]+a[j])
    s=sorted(s)
    for i in range(len(s)-1,-1,-1):
        if s[i]%d==0:
            print(s[i])
            return
    print(-1)
    return

=======
Suggestion 7

def solve(n, k, d, a):
    if k == 1:
        for i in range(n):
            if a[i] % d == 0:
                return a[i]
        return -1
    if d == 1:
        return sum(a)
    if k == 2:
        ans = -1
        for i in range(n):
            for j in range(i+1, n):
                if (a[i] + a[j]) % d == 0:
                    ans = max(ans, a[i] + a[j])
        return ans
    if k == 3:
        ans = -1
        for i in range(n):
            for j in range(i+1, n):
                for l in range(j+1, n):
                    if (a[i] + a[j] + a[l]) % d == 0:
                        ans = max(ans, a[i] + a[j] + a[l])
        return ans

=======
Suggestion 8

def main():
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A = [0] + A
    # dp[i][j][k]: i???????????

=======
Suggestion 9

def solve(n,k,d):
    a = list(map(int,input().split()))
    s = set()
    for i in range(n):
        s.add(a[i])
        for j in range(i+1,k+i):
            s.add(a[i]+a[j])
    for i in range(10**9,-1,-1):
        if i*d in s:
            return i*d
    return -1

n,k,d = map(int,input().split())
print(solve(n,k,d))

=======
Suggestion 10

def main():
    # read input
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    # solve problem
    A.sort(reverse=True)
    S = set()
    for i in range(K):
        S.update([sum(A[:i+1])])
    # write output
    for i in range(max(S), -1, -1):
        if i % D == 0:
            print(i)
            return
    print(-1)
