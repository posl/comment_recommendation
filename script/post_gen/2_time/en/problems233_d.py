Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]
    S = [s - K for s in S]
    S.sort()
    ans = 0
    cnt = 1
    for i in range(N):
        if S[i] == S[i + 1]:
            cnt += 1
        else:
            ans += cnt * (cnt - 1) // 2
            cnt = 1
    print(ans)

=======
Suggestion 2

def main():
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    s=[0]*(n+1)
    for i in range(n):
        s[i+1]=s[i]+a[i]
    d={}
    for i in range(n+1):
        m=s[i]%k
        d[m]=d.get(m,0)+1
    ans=0
    for i in d.values():
        ans+=i*(i-1)//2
    print(ans)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A = [0] + A
    for i in range(N):
        A[i + 1] += A[i]
    counter = {}
    for a in A:
        if a in counter:
            counter[a] += 1
        else:
            counter[a] = 1
    ans = 0
    for a in A:
        if a + K in counter:
            ans += counter[a + K]
    print(ans)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        tmp = 0
        for j in range(i, N):
            tmp += A[j]
            if tmp == K:
                ans += 1
    print(ans)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    cumsum = [0]
    for i in range(N):
        cumsum.append(cumsum[i] + A[i])
    dic = {}
    for i in range(N+1):
        if cumsum[i] - K in dic:
            ans += dic[cumsum[i]-K]
        if cumsum[i] in dic:
            dic[cumsum[i]] += 1
        else:
            dic[cumsum[i]] = 1
    print(ans)

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    #A = [8, -3, 5, 7, 0, -4]
    #N = 6
    #K = 5
    #A = [1000000000, -1000000000]
    #N = 2
    #K = -1000000000000000
    #A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    #N = 10
    #K = 15
    #A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    #N = 11
    #K = 15
    #A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    #N = 11
    #K = 20
    #A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    #N = 11
    #K = 21
    #A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    #N = 11
    #K = 22
    #A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    #N = 11
    #K = 23
    #A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    #N = 11
    #K = 24
    #A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    #N = 11
    #K = 25

=======
Suggestion 7

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    cnt = 0
    for i in range(n):
        sum_a = 0
        for j in range(i, n):
            sum_a += a[j]
            if sum_a == k:
                cnt += 1
    print(cnt)

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A = [0] + A

    #累積和
    for i in range(1, N + 1):
        A[i] += A[i - 1]

    #累積和の差がKとなる組み合わせの個数を求める
    from collections import Counter
    cnt = Counter(A)
    ans = 0
    for i in range(N + 1):
        ans += cnt[A[i] - K]
    print(ans)

=======
Suggestion 9

def solve(N,K,A):
    # write your code in Python 3.6
    sum = 0
    count = 0
    dic = {}
    dic[0] = 1
    for i in range(N):
        sum += A[i]
        if sum - K in dic:
            count += dic[sum - K]
        if sum in dic:
            dic[sum] += 1
        else:
            dic[sum] = 1
    return count
