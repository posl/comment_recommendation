Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    S = input()
    ans = 0
    count = 0
    for i in range(N-1):
        if S[i] == S[i+1]:
            count += 1
        else:
            ans += 1
    ans += min(count, K) * 2
    if K >= count:
        ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N, K = map(int, input().split(

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    S = input()
    count = 0
    if S[0] == '0':
        count += 1
    for i in range(1, N):
        if S[i] == '1' and S[i - 1] == '0':
            count += 1
    print(min(N, count + 2 * K))

=======
Suggestion 4

def main():
    n,k = map(int,input().split())
    s = input()
    l = 0
    r = 0
    ans = 0
    while r < n:
        while r < n and s[r] == '1':
            r += 1
        ans = max(ans,r-l)
        r += 1
        while r < n and s[r] == '0':
            r += 1
        while k > 0 and l < r:
            k -= 1
            l += 1
            while l < r and s[l] == '1':
                l += 1
    print(ans)

=======
Suggestion 5

def solve():
    n, k = map(int, input().split())
    s = input()
    s = list(s)
    s = list(map(int, s))
    cnt = 0
    for i in range(n-1):
        if s[i] == s[i+1]:
            cnt += 1
    ans = min(cnt + 2 * k, n - 1)
    print(ans)

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    s = input()
    #print(n, k, s)
    #print(s[0])
    #print(s[1])
    #print(s[2])
    #print(s[3])
    #print(s[4])

    #print(s[0:3])
    #print(s[1:4])
    #print(s[2:5])
    #print(s[3:6])
    #print(s[4:7])

    #print(s[0:4])
    #print(s[1:5])
    #print(s[2:6])
    #print(s[3:7])
    #print(s[4:8])

    #print(s[0:5])
    #print(s[1:6])
    #print(s[2:7])
    #print(s[3:8])
    #print(s[4:9])

    #print(s[0:6])
    #print(s[1:7])
    #print(s[2:8])
    #print(s[3:9])
    #print(s[4:10])

    #print(s[0:7])
    #print(s[1:8])
    #print(s[2:9])
    #print(s[3:10])
    #print(s[4:11])

    #print(s[0:8])
    #print(s[1:9])
    #print(s[2:10])
    #print(s[3:11])
    #print(s[4:12])

    #print(s[0:9])
    #print(s[1:10])
    #print(s[2:11])
    #print(s[3:12])
    #print(s[4:13])

    #print(s[0:10])
    #print(s[1:11])
    #print(s[2:12])
    #print(s[3:13])
    #print(s[4:14])

    #print(s[0:11])
    #print(s[1:12])
    #print(s[2:13])
    #print(s[3:14])

    #print(s[0:12])
    #print(s[1:13])
    #print(s[2:14])

    #print(s[0:13])
    #print(s[

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    S = input()
    S = S + '0'
    cnt = 0
    start = 0
    if S[0] == '0':
        cnt = 1
    for i in range(1, N+1):
        if S[i-1] != S[i]:
            cnt += 1
        else:
            if cnt > 0:
                start += 1
            cnt = 0
    if cnt > 0:
        start += 1
    if start <= K:
        print(N)
    else:
        ans = 0
        cnt = 0
        tmp = 0
        for i in range(1, N+1):
            if S[i-1] != S[i]:
                cnt += 1
            else:
                if cnt > 0:
                    tmp += 1
                else:
                    ans += 1
                cnt = 0
            if tmp == K:
                break
        ans += cnt
        print(ans)

=======
Suggestion 8

def main():
    # input
    n,k = map(int,input().split())
    s = input()
    # solve
    s = list(s)
    s = list(map(int,s))
    s = [0] + s + [0]
    count = 0
    for i in range(n):
        if s[i] == 1 and s[i+1] == 0:
            count += 1
    count = min(count,k)
    ans = 0
    for i in range(n):
        if s[i] == 0:
            count += 1
        if s[i] == 1:
            count -= 1
        if s[i+count] == 0:
            count -= 1
        if s[i+count] == 1:
            count += 1
        ans = max(ans,count)
    # output
    print(ans)

=======
Suggestion 9

def main():
    N,K = map(int,input().

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    S = input()
    S = list(S)
    S = S + S
    S = list(map(int, S))
    #print(S)
    cnt = 0
    ans = 0
    for i in range(2 * N - 1):
        if S[i] == S[i+1]:
            cnt += 1
        else:
            cnt = 0
        ans = max(ans, cnt)
    #print(ans)
    ans = min(ans + 2 * K, N)
    print(ans)
