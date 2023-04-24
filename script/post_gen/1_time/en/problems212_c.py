Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    i = 0
    j = 0
    ans = 10 ** 18
    while i < N and j < M:
        ans = min(ans, abs(A[i] - B[j]))
        if A[i] < B[j]:
            i += 1
        else:
            j += 1
    print(ans)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    i = 0
    j = 0
    ans = 10**9
    while i < N and j < M:
        ans = min(ans, abs(A[i] - B[j]))
        if A[i] > B[j]:
            j += 1
        else:
            i += 1
    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    a = 0
    b = 0
    ans = 10**9
    while a < N and b < M:
        ans = min(ans, abs(A[a] - B[b]))
        if A[a] < B[b]:
            a += 1
        else:
            b += 1
    print(ans)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    a = 0
    b = 0
    ans = 10**9
    while a < N and b < M:
        ans = min(ans, abs(A[a] - B[b]))
        if A[a] > B[b]:
            b += 1
        else:
            a += 1
    print(ans)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    diff = 10**9
    i, j = 0, 0
    while i < N and j < M:
        diff = min(diff, abs(A[i]-B[j]))
        if A[i] < B[j]:
            i += 1
        else:
            j += 1
    print(diff)

main()

As you can see, the main idea is to sort the list A and B and then compare the minimum difference of A[i] and B[j] for all i and j. The code is written in Python, but it also works in PyPy.

This problem is from the AtCoder Beginner Contest 212.

=======
Suggestion 6

def main():
    import sys
    from bisect import bisect_left
    input = sys.stdin.readline
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A.sort()
    B.sort()
    ans = 10**9
    for a in A:
        ind = bisect_left(B,a)
        if ind == 0:
            ans = min(ans,abs(a-B[0]))
        elif ind == M:
            ans = min(ans,abs(a-B[-1]))
        else:
            ans = min(ans,abs(a-B[ind]),abs(a-B[ind-1]))
    print(ans)
main()

I'm trying to solve this problem: https://atcoder.jp/contests/abc153/tasks/abc153_f

This is my code:

=======
Suggestion 7

def main():
    import sys
    from bisect import bisect_left
    input = sys.stdin.readline
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A.sort()
    B.sort()
    ans = 10**9
    for i in range(N):
        j = bisect_left(B,A[i])
        if j==0:
            ans = min(ans,abs(A[i]-B[j]))
        elif j==M:
            ans = min(ans,abs(A[i]-B[j-1]))
        else:
            ans = min(ans,abs(A[i]-B[j-1]),abs(A[i]-B[j]))
    print(ans)

=======
Suggestion 8

def calc():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    ans = 10**9
    i = 0
    j = 0
    while i < N and j < M:
        ans = min(ans, abs(A[i] - B[j]))
        if A[i] < B[j]:
            i += 1
        else:
            j += 1
    return ans

print(calc())

=======
Suggestion 9

def main():
    import sys
    from bisect import bisect_left
    readline = sys.stdin.readline
    write = sys.stdout.write
    N, M = map(int, readline().split())
    A = list(map(int, readline().split()))
    B = list(map(int, readline().split()))
    A.sort()
    B.sort()
    ans = 10**9
    for a in A:
        idx = bisect_left(B, a)
        if idx == M:
            ans = min(ans, abs(a-B[idx-1]))
        elif idx == 0:
            ans = min(ans, abs(a-B[idx]))
        else:
            ans = min(ans, abs(a-B[idx-1]), abs(a-B[idx]))
    write(str(ans))
