Synthesizing 9/10 solutions

=======
Suggestion 1

def solve(n,s,w):
    w.sort()
    ans = 0
    for i in range(n):
        if s[i]=='0':
            ans+=1
    minw = 10**9+1
    for i in range(n):
        if s[i]=='0':
            if w[i]<minw:
                minw = w[i]
    if minw==10**9+1:
        minw = 0
    maxw = -1
    for i in range(n):
        if s[i]=='1':
            if w[i]>maxw:
                maxw = w[i]
    if maxw==-1:
        maxw = 0
    if ans==0:
        return 0
    return min(ans,2*n-ans)

=======
Suggestion 2

def isChild(W, S, X):
    if W < X and S == '0':
        return True
    elif W >= X and S == '1':
        return True
    else:
        return False

=======
Suggestion 3

def main():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    ans = 0
    for x in range(0, 200):
        #print(x)
        cnt = 0
        for i in range(N):
            if S[i] == '0' and W[i] <= x:
                cnt += 1
            if S[i] == '1' and W[i] > x:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)

=======
Suggestion 4

def f(x, s, w):
    n = len(s)
    count = 0
    for i in range(n):
        if s[i] == '1':
            if w[i] >= x:
                count += 1
        else:
            if w[i] < x:
                count += 1
    return count

=======
Suggestion 5

def get_max_f(x, n, s, w):
    f = 0
    for i in range(n):
        if s[i] == '0' and w[i] < x:
            f += 1
        elif s[i] == '1' and w[i] >= x:
            f += 1
    return f

=======
Suggestion 6

def f(x, s, w):
    count = 0
    for i in range(len(s)):
        if s[i] == '0' and w[i] < x:
            count += 1
        elif s[i] == '1' and w[i] >= x:
            count += 1
    return count

n = int(input())
s = input()
w = [int(i) for i in input().split()]
max_w = max(w)
min_w = min(w)
max_x = max_w
min_x = min_w
max_f = f(max_x, s, w)
min_f = f(min_x, s, w)

while min_x < max_x:
    mid_x = (min_x + max_x) // 2
    mid_f = f(mid_x, s, w)
    if mid_f == max_f:
        min_x = mid_x
    elif mid_f == min_f:
        max_x = mid_x
    else:
        min_x = mid_x
        max_x = mid_x

print(max_f)

=======
Suggestion 7

def main():
    n = int(input())
    s = input()
    w = list(map(int, input().split()))
    if s.count('0') == 0 or s.count('1') == 0:
        print(n)
        return
    if s.count('0') == n or s.count('1') == n:
        print(0)
        return
    w.sort()
    for i in range(n):
        if s[i] == '1':
            w[i] = -1
    for i in range(n-1):
        if w[i] == -1:
            continue
        if w[i] < w[i+1]:
            w[i] = -1
    print(w.count(-1))

=======
Suggestion 8

def f(x, n, s, w):
    c = 0
    for i in range(n):
        if s[i] == '0':
            if x > w[i]:
                c += 1
        else:
            if x <= w[i]:
                c += 1
    return c

=======
Suggestion 9

def f(x, N, S, W):
    count = 0
    for i in range(N):
        if S[i] == '0':
            if W[i] < x:
                count += 1
        else:
            if W[i] >= x:
                count += 1
    return count
