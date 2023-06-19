Synthesizing 8/10 solutions

=======
Suggestion 1

def main():
    n,k = map(int,input().split())
    s = input()
    s_list = list(s)

=======
Suggestion 2

def solve():
    n, k = map(int, input().split())
    s = input()
    cnt = 0
    for i in range(n-1):
        if s[i] == s[i+1]:
            cnt += 1
    print(min(cnt + 2*k, n-1))
solve()

=======
Suggestion 3

def solve():
    n,k = map(int,input().split())
    s = input()
    s = s.replace("LR","L R")
    s = s.replace("RL","R L")
    #print(s)
    s = s.split()
    #print(s)
    ans = 0
    for i in range(len(s)):
        if s[i][0] == "L":
            ans += 1
        if s[i][-1] == "R":
            ans += 1
    ans = min(ans+2*k,n)
    print(ans)

=======
Suggestion 4

def solve():
    n, k = map(int, input().split())
    s = input()
    ans = 0
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            ans += 1
    ans += min(2 * k, n - 1)
    print(ans)

solve()

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    S = input()
    cnt = 0
    for i in range(N-1):
        if S[i] == S[i+1]:
            cnt += 1
    cnt += 2 * K
    if cnt > N-1:
        cnt = N-1
    print(cnt)

=======
Suggestion 6

def solve(n, k, s):
    # 从左边开始计算
    l = 0
    happy = 0
    for i in range(n):
        if s[i] == 'R':
            happy += 1
        else:
            happy -= 1
        if happy > 0:
            l = i+1
            break
    # 从右边开始计算
    r = n-1
    happy = 0
    for i in range(n-1, -1, -1):
        if s[i] == 'L':
            happy += 1
        else:
            happy -= 1
        if happy > 0:
            r = i-1
            break
    # 从左边开始计算
    happy = 0
    for i in range(l, r+1):
        if s[i] == 'R':
            happy += 1
        else:
            happy -= 1
    # 从右边开始计算
    happy = 0
    for i in range(r, l-1, -1):
        if s[i] == 'L':
            happy += 1
        else:
            happy -= 1
    return happy + min(k, r-l+1)

=======
Suggestion 7

def main():
    n, k = map(int, input().split())
    s = input()

    # 左端点为l，右端点为r
    l = 0
    r = 0

    # 从左向右扫描，找到第一个L
    while l < n and s[l] == 'R':
        l += 1
    # 从右向左扫描，找到第一个R
    while r < n and s[n-r-1] == 'L':
        r += 1

    # 从左向右扫描，找到所有的R的左端点
    rr = []
    i = l
    while i < n:
        while i < n and s[i] == 'L':
            i += 1
        if i == n:
            break
        j = i
        while j < n and s[j] == 'R':
            j += 1
        rr.append((i, j))
        i = j

    # 从右向左扫描，找到所有的L的右端点
    ll = []
    i = n-r-1
    while i >= 0:
        while i >= 0 and s[i] == 'R':
            i -= 1
        if i < 0:
            break
        j = i
        while j >= 0 and s[j] == 'L':
            j -= 1
        ll.append((j+1, i+1))
        i = j

    # print(l, r)
    # print(rr)
    # print(ll)

    # 求出左右两边的人数
    ans = r + l

    # 求出中间的人数
    for i in range(len(rr)):
        ans += rr[i][1] - rr[i][0]
        if i > 0:
            ans += rr[i][0] - rr[i-1][1] - 1
    for i in range(len(ll)):
        ans += ll[i][1] - ll[i][0]
        if i > 0:
            ans += ll[i][0] - ll[i-1][1] - 1

    # print(ans)

    # 从左向右

=======
Suggestion 8

def solve(n, k, s):
    #print(n, k, s)
    if k >= n:
        return n
    else:
        l = 0
        r = 0
        cnt = 0
        for i in range(n):
            if s[i] == 'L':
                l += 1
            else:
                r += 1
            if i > 0 and s[i] != s[i-1]:
                cnt += 1
        #print(l, r, cnt)
        if cnt <= k:
            return n
        else:
            if s[0] == 'L':
                s = 'R' + s
            else:
                s = 'L' + s
            if s[-1] == 'L':
                s = s + 'R'
            else:
                s = s + 'L'
            #print(s)
            s = list(s)
            for i in range(n+1):
                if s[i] == 'L':
                    l -= 1
                else:
                    r -= 1
                if s[i+1] == 'L':
                    l += 1
                else:
                    r += 1
                if l == r:
                    #print(l, r, i)
                    if i+1 <= k:
                        return n
                    else:
                        return n - 1
            return n
