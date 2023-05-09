Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]
    i = 0
    while A[i] < N:
        i += 1
    print(i+1)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    i = 0
    while N > 0:
        N = N - A[i]
        i = i + 1
    print(i)

main()

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0] * (n+1)
    for i in a:
        b[i] = 1
    for i in range(n):
        b[i+1] += b[i]
    ans = 0
    for i in range(k):
        ans += b[n] - b[a[i]]
        n -= a[i]
    print(ans)
    return

=======
Suggestion 4

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(k):
        if i == 0:
            ans += a[i]
        else:
            ans += a[i] - a[i-1]
    print(ans + n - a[-1])

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    count = 0
    for i in range(k):
        if n >= a[i]:
            n -= a[i]
            count += 1
        else:
            break
    print(count)

=======
Suggestion 6

def problem():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    ans = 0
    for i in range(K-1,-1,-1):
        if N >= A[i]:
            ans += (N//A[i])*A[i]
            N = N%A[i]
    return ans

print(problem())

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.append(N+1)
    ans = 0
    for i in range(K):
        ans += A[i]
    print(ans)

=======
Suggestion 8

def main():
    n,k = map(int, input().split())
    a = [int(i) for i in input().split()]
    cnt = 0
    while n > 0:
        if n >= a[-1]:
            n -= a[-1]
            cnt += 1
        else:
            a.pop()
    print(cnt)

=======
Suggestion 9

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.append(a[-1]+1)
    b = [0] * (n+1)
    for i in range(1, n+1):
        for j in a:
            if i - j < 0:
                break
            b[i] = max(b[i], 1 - b[i-j])
    print('First' if b[n] == 1 else 'Second')

=======
Suggestion 10

def solve():
    # Implement solution here
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    print(sum(A[0:A.index(N)]) + (N - A[A.index(N) - 1]))
