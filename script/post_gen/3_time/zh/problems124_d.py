Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, k = map(int, input().spli

=======
Suggestion 2

def main():
    n,k=map(int,input().split())
    s=input()
    ans=0
    for i in range(n):
        if s[i]=='0':
            ans+=1
    if ans==n:
        print(n)
        return
    tmp=0
    for i in range(k):
        if s[i]=='0':
            tmp+=1
    ans=max(ans,tmp)
    for i in range(k,n):
        if s[i-k]=='0':
            tmp-=1
        if s[i]=='0':
            tmp+=1
        ans=max(ans,tmp)
    print(ans)
    return

=======
Suggestion 3

def solve():
    N, K = map(int, input().split())
    S = input()
    ans = 0
    cnt = 0
    for i in range(N):
        if S[i] == '0':
            cnt += 1
        else:
            if K > 0:
                K -= 1
                cnt += 1
            else:
                ans = max(ans, cnt)
                cnt = 0
    ans = max(ans, cnt)
    print(ans)
solve()

=======
Suggestion 4

def main():
    n,k = map(int,input().split())
    s = list(map(int,input()))
    ans = 0
    for i in range(n):
        if s[i] == 0:
            ans += 1
    tmp = ans
    for i in range(k):
        if s[i] == 0:
            tmp += 1
        else:
            tmp -= 1
        ans = max(ans,tmp)
    print(ans)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    S = input()
    ans = 0
    for i in range(N):
        if S[i] == '0':
            ans += 1
    print(min(ans + K * 2, N - 1))

=======
Suggestion 6

def main():
    n,k = map(int, input().split())
    s = input()
    #print(n,k,s)
    #print(s)
    a = []
    for i in range(n-1):
        if s[i] != s[i+1]:
            a.append(i)
    #print(a)
    l = len(a)
    if l <= 2*k:
        print(n)
    else:
        #print(a)
        #print(l)
        #print(k)
        b = [0]*(l-2*k+1)
        for i in range(l-2*k+1):
            b[i] = a[i+2*k-1]-a[i]+1
        #print(b)
        print(max(b))

=======
Suggestion 7

def solve():
    N, K = map(int, input().split())
    S = input()
    ans = 0
    for i in range(N):
        if S[i] == '0':
            if i == 0 or S[i-1] == '1':
                ans += 1
        else:
            if i == 0 or S[i-1] == '0':
                ans += 1
    ans += 2 * K
    print(min(ans, N-1))

=======
Suggestion 8

def main():
    n,k = map(int,input().split())
    s = input()
    s = [int(x) for x in s]
    if n==1:
        print(1)
        return
    if s[0]==0:
        s.insert(0,1)
    if s[-1]==0:
        s.append(1)
    if n==2:
        print(2)
        return
    s.insert(0,1)
    s.append(1)
    #print(s)
    l = 0
    r = 0
    max = 0
    while r<len(s)-1:
        if s[r+1]==0:
            if k>0:
                k -= 1
                r += 1
            else:
                if s[l]==0:
                    l += 1
                else:
                    l += 2
                    r += 1
        else:
            r += 1
        if r-l>max:
            max = r-l
    print(max)
    return

=======
Suggestion 9

def solve():
    N,K = map(int,input().split())
    S = input()
    l = 0
    r = 0
    ans = 0
    count = 0
    while l < N:
        while r < N and (r == l or (r < N and S[r] == S[r-1])):
            r += 1
        if S[l] == '0':
            count += r - l
        ans = max(ans,r - l)
        l += 1
    if K > 0:
        ans = min(ans,N)
    else:
        ans = min(ans,count)
    print(ans)

=======
Suggestion 10

def main():
    n, k = map(int, input().split())
    s = input()
    cnt = 0
    for i in range(n - 1):
        if s[i] != s[i + 1]:
            cnt += 1
    print(min(cnt + 2 * k, n - 1))
