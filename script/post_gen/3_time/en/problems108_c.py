Synthesizing 9/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n,k = map(int, input().split())
    ans = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            for l in range(1,n+1):
                if (i+j)%k == 0 and (j+l)%k == 0 and (l+i)%k == 0:
                    ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    cnt = 0
    for a in range(1, N+1):
        for b in range(1, N+1):
            if (a+b)%K == 0:
                for c in range(1, N+1):
                    if (b+c)%K == 0 and (c+a)%K == 0:
                        cnt += 1
    print(cnt)

=======
Suggestion 3

def count_triples(n, k):
    count = 0
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            for c in range(1, n + 1):
                if (a + b) % k == 0 and (b + c) % k == 0 and (c + a) % k == 0:
                    count += 1
    return count

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    ans = 0
    for a in range(1, N + 1):
        ans += (N // a) * max(0, (a - K + 1))
        if a >= K:
            ans += max(0, (N % a) - K + 1)
    print(ans)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    print(N//K * N//K * N//K + (N//K+1)**3 if K%2 == 0 else N//K * N//K * N//K)

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    print((N//K)**3 + ((N+K//2)//K)**3)

=======
Suggestion 7

def get_ints():
    return map(int, input().split())

N, K = get_ints()
ans = 0
for i in range(1, N + 1):
    if i % K == 0:
        ans += 1
print(ans**3)

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    print(((N//K)**3)+((N//K)**2)*((N-N//K)**2)*2+((N//K)**2)*((N//K)**2)*2+((N-N//K)**2)*((N-N//K)**2)*2)
