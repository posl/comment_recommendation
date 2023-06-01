Synthesizing 10/10 solutions

=======
Suggestion 1

def problems233_d():
    pass

=======
Suggestion 2

def main():
    print("233_d")
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    s = [0]
    for i in range(n):
        s.append(s[i]+a[i])
    #print(s)
    ans = 0
    r = 0
    for l in range(n):
        while r <= n and s[r] - s[l] < k:
            r += 1
        if s[r] - s[l] == k:
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    ans = 0
    right = 1
    for left in range(n):
        while right <= n and s[right] - s[left] < k:
            right += 1
        if s[right] - s[left] == k:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.insert(0, 0)
    for i in range(1, n+1):
        a[i] += a[i-1]
    ans = 0
    from collections import defaultdict
    d = defaultdict(int)
    for i in range(n+1):
        ans += d[a[i]]
        d[a[i]+k] += 1
    print(ans)

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    # print(n, k)
    # print(a)
    # print(len(a))
    # print(a[0])
    # print(a[1])
    # print(a[n-1])
    # print(a[n])
    # print(a[n-2])
    # print(a[n-1])
    # print(a[n])
    # print(a[n+1])
    # print(a[n+2])
    # print(a[n+3])
    # print(a[n+4])
    # print(a[n+5])
    # print(a[n+6])
    # print(a[n+7])
    # print(a[n+8])
    # print(a[n+9])
    # print(a[n+10])
    # print(a[n+11])
    # print(a[n+12])
    # print(a[n+13])
    # print(a[n+14])
    # print(a[n+15])
    # print(a[n+16])
    # print(a[n+17])
    # print(a[n+18])
    # print(a[n+19])
    # print(a[n+20])
    # print(a[n+21])
    # print(a[n+22])
    # print(a[n+23])
    # print(a[n+24])
    # print(a[n+25])
    # print(a[n+26])
    # print(a[n+27])
    # print(a[n+28])
    # print(a[n+29])
    # print(a[n+30])
    # print(a[n+31])
    # print(a[n+32])
    # print(a[n+33])
    # print(a[n+34])
    # print(a[n+35])
    # print(a[n+36])
    # print(a[n+37])
    # print(a[n+38])
    # print(a[n+39])
    # print(a[n+40])
    # print(a[n+41])
    # print(a[n+42])
    # print(a[n+43])
    # print(a[n+44])
    # print(a[n+45])
    # print(a[n+46])
    # print(a[n+47])
    # print(a[n+48])
    # print(a[n+49])
    # print(a[n+50])
    # print(a[n+51

=======
Suggestion 6

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    r = 0
    sum = 0
    for l in range(N):
        while r < N and sum < K:
            sum += A[r]
            r += 1
        if sum == K:
            ans += 1
        if r == l:
            r += 1
        else:
            sum -= A[l]
    print(ans)

=======
Suggestion 7

def main():
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
Suggestion 8

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]
    from collections import defaultdict
    d = defaultdict(int)
    ans = 0
    for i in range(N + 1):
        ans += d[S[i]]
        d[S[i] + K] += 1
    print(ans)

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    r = 0
    s = 0
    for l in range(N):
        while r < N and s + A[r] < K:
            s += A[r]
            r += 1
        ans += r - l
        if r == l:
            r += 1
        else:
            s -= A[l]
    print(ans)

=======
Suggestion 10

def subarray_sum(arr, k):
    count = 0
    for i in range(len(arr)):
        sum = 0
        for j in range(i, len(arr)):
            sum += arr[j]
            if sum == k:
                count += 1
    return count
