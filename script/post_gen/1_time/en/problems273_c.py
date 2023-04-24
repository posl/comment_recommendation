Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = [0] * N
    ans[0] = 1
    for i in range(1, N):
        ans[i] = ans[i-1]
        if A[i] != A[i-1]:
            ans[i] += 1
    ans = ans[::-1]
    for i in range(N):
        print(ans[i])

=======
Suggestion 2

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = [0] * N
    for i in range(N):
        if i > 0 and A[i] == A[i - 1]:
            ans[i] = ans[i - 1]
        else:
            ans[i] = N - i - 1
    for i in ans:
        print(i)
    return 0

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a.append(-1)
    ans = [0] * n
    cnt = 1
    for i in range(n):
        if a[i] != a[i+1]:
            ans[cnt-1] += 1
            cnt = 1
        else:
            cnt += 1
    for i in ans:
        print(i)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a.append(0)
    ans = [0] * n
    cnt = 1
    for i in range(n):
        if a[i] != a[i+1]:
            ans[cnt-1] += 1
            cnt = 1
        else:
            cnt += 1
    print(*ans, sep='\n')

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a.append(-1)
    cnt = 0
    ans = [0] * n
    for i in range(n):
        cnt += 1
        if a[i] != a[i+1]:
            ans[cnt-1] += 1
            cnt = 0
    for i in range(n):
        print(ans[i])

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    c = [0] * (n+1)
    for i in range(n):
        c[a[i]] += 1
    s = [0] * (n+1)
    for i in range(1, n+1):
        s[i] = s[i-1] + c[i]
    for i in range(n):
        print(s[a[i]] - 1)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A.append(0)
    K = 0
    ans = [0] * N
    for i in range(N):
        if A[i] != A[i+1]:
            ans[K] += 1
            K = 0
        else:
            K += 1
    print(*ans, sep='\n')

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a.append(0)
    ans = [0] * n
    x = 0
    for i in range(n):
        if a[i] != a[i+1]:
            ans[x] = i + 1
            x = 0
        else:
            x += 1
    for i in range(n):
        print(ans[i])

=======
Suggestion 9

def solve():
    import sys
    N = int(input())
    A = list(map(int, input().split()))
    if N == 1:
        print(1)
        sys.exit()
    A.sort()
    ans = [0 for _ in range(N)]
    ans[0] = 1
    for i in range(1, N):
        if A[i] != A[i-1]:
            ans[i] = ans[i-1] + 1
        else:
            ans[i] = ans[i-1]
    for i in range(N):
        print(ans[i])

=======
Suggestion 10

def problems273_c():
    N = int(raw_input())
    A = map(int, raw_input().split())
    A.sort()
    A.append(A[-1]+1)
    ans = [0]*N
    cnt = 1
    for i in range(N):
        if A[i]!=A[i+1]:
            ans[cnt-1]+=1
            cnt = 1
        else:
            cnt+=1
    print '\n'.join(map(str,ans))
