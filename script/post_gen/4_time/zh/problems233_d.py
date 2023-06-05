Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    sum = 0
    for i in range(N):
        for j in range(i, N):
            sum += A[j]
            if sum == K:
                print(i, j)
    print(sum)

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    #print(n, k)
    #print(a)
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    #print(s)
    ans = 0
    right = 0
    for left in range(n):
        while right < n and s[right + 1] - s[left] < k:
            right += 1
        if s[right + 1] - s[left] == k:
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    #print(a)
    sum = 0
    ans = 0
    right = 0
    for left in range(n):
        while right < n and sum + a[right] < k:
            sum += a[right]
            right += 1
        ans += right - left
        if left == right:
            right += 1
        else:
            sum -= a[left]
    print(ans)

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    from collections import Counter
    c = Counter(s)
    ans = 0
    for i in range(n + 1):
        ans += c[s[i] - k]
        c[s[i]] -= 1
    print(ans)


main()

=======
Suggestion 5

def solve():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    s = [0]*(n+1)
    for i in range(n):
        s[i+1] = s[i] + a[i]
    from collections import defaultdict
    d = defaultdict(int)
    ans = 0
    for i in range(n+1):
        ans += d[s[i]]
        d[s[i]+k] += 1
    print(ans)

=======
Suggestion 6

def solve(n, k, a):
    s = [0]
    for i in range(n):
        s.append(s[-1] + a[i])
    ans = 0
    from collections import Counter
    c = Counter(s)
    for i in range(n + 1):
        ans += c[s[i] + k]
        if s[i] == s[i + 1]:
            c[s[i]] -= 1
    return ans

n, k = map(int, input().split())
a = list(map(int, input().split()))
print(solve(n, k, a))

=======
Suggestion 7

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.insert(0, 0)
    for i in range(1, n+1):
        a[i] += a[i-1]
    a.insert(0, 0)
    from collections import defaultdict
    d = defaultdict(int)
    ans = 0
    for i in range(1, n+2):
        ans += d[a[i]-k]
        d[a[i]] += 1
    print(ans)

=======
Suggestion 8

def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    count = 0
    for i in range(N):
        if A[i] == K:
            count += 1
        for j in range(i+1,N):
            A[j] += A[j-1]
            if A[j] == K:
                count += 1
    print(count)

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]
    from collections import defaultdict
    cnt = defaultdict(int)
    ans = 0
    for i in range(N + 1):
        ans += cnt[S[i]]
        cnt[S[i] + K] += 1
    print(ans)

=======
Suggestion 10

def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    ans = 0
    s = 0
    t = 0
    while True:
        if s == N:
            break
        while True:
            if t == N:
                break
            if s == t:
                if A[s] == K:
                    ans += 1
                    t += 1
                    break
                else:
                    t += 1
            else:
                if sum(A[s:t+1]) == K:
                    ans += 1
                    t += 1
                    break
                elif sum(A[s:t+1]) < K:
                    t += 1
                else:
                    break
        s += 1
    print(ans)
