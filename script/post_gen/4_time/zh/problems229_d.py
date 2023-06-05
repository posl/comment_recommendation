Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    K = int(input())
    count = 0
    max_count = 0
    for i in range(len(S)):
        if S[i] == 'X':
            count += 1
        else:
            if count > max_count:
                max_count = count
            count = 0
    if count > max_count:
        max_count = count
    if max_count + K > len(S):
        print(len(S))
    else:
        print(max_count + K)

=======
Suggestion 2

def main():
    s = input()
    k = int(input())
    cnt = 0
    max_cnt = 0
    for i in range(len(s)):
        if s[i] == 'X':
            cnt += 1
        else:
            max_cnt = max(max_cnt, cnt)
            cnt = 0
    max_cnt = max(max_cnt, cnt)
    if k == 0:
        print(max_cnt)
        return
    cnt = 0
    for i in range(len(s)):
        if s[i] == 'X':
            cnt += 1
        else:
            if i > 0 and s[i - 1] == 'X':
                cnt += 1
            if i < len(s) - 1 and s[i + 1] == 'X':
                cnt += 1
            max_cnt = max(max_cnt, cnt)
            cnt = 0
    max_cnt = max(max_cnt, cnt)
    print(max_cnt)
    return

=======
Suggestion 3

def main():
    s = input()
    k = int(input())
    n = len(s)
    l = []
    cnt = 0
    for i in range(n):
        if s[i] == "X":
            cnt += 1
        else:
            l.append(cnt)
            cnt = 0
    l.append(cnt)
    m = len(l)
    ans = 0
    if m <= 2 * k + 1:
        ans = n
    else:
        for i in range(m - 2 * k):
            tmp = sum(l[i:i + 2 * k + 1]) + k
            ans = max(ans, tmp)
    print(ans)

=======
Suggestion 4

def main():
    s = input()
    k = int(input())
    s_len = len(s)
    count = 0
    for i in range(s_len):
        if s[i] == "X":
            count += 1
    if count == s_len:
        print(s_len)
        return
    if k == 0:
        count = 0
        max_count = 0
        for i in range(s_len):
            if s[i] == ".":
                max_count = max(max_count, count)
                count = 0
            else:
                count += 1
        max_count = max(max_count, count)
        print(max_count)
        return
    count = 0
    max_count = 0
    for i in range(s_len):
        if s[i] == ".":
            max_count = max(max_count, count)
            count = 0
        else:
            count += 1
    max_count = max(max_count, count)
    print(max_count + k)

=======
Suggestion 5

def main():
    s = input()
    k = int(input())
    l = len(s)
    i = 0
    j = 0
    ans = 0
    while i < l:
        if s[i] == 'X':
            j += 1
            i += 1
        else:
            if k > 0:
                ans = max(ans, j + 1)
                k -= 1
                i += 1
                j += 1
            else:
                ans = max(ans, j)
                j = 0
                i += 1
    ans = max(ans, j)
    print(ans)

=======
Suggestion 6

def solve():
    s = input()
    k = int(input())
    n = len(s)
    a = [0] * n
    for i in range(n):
        if s[i] == 'X':
            a[i] = 1
    b = [0] * n
    b[0] = a[0]
    for i in range(1, n):
        b[i] = b[i - 1] + a[i]
    ans = 0
    for i in range(n):
        if s[i] == 'X':
            ans += 1
            continue
        if i == 0:
            ans = max(ans, b[min(i + k, n - 1)])
        else:
            ans = max(ans, b[min(i + k, n - 1)] - b[i - 1])
    print(ans)

solve()

=======
Suggestion 7

def main():
    s = input()
    k = int(input())
    n = len(s)
    l = []
    i = 0
    while i < n:
        if s[i] == "X":
            count = 0
            while i < n and s[i] == "X":
                count += 1
                i += 1
            l.append(count)
        else:
            i += 1
    ans = 0
    for i in range(len(l)):
        ans = max(ans, l[i])
    for i in range(len(l)):
        if k == 0:
            break
        if l[i] == 1:
            if i == 0:
                if i+1 < len(l):
                    if l[i+1] > 1:
                        if k >= 2:
                            ans = max(ans, l[i]+l[i+1]+1)
                            k -= 2
                    else:
                        if k >= 1:
                            ans = max(ans, l[i]+l[i+1]+1)
                            k -= 1
                else:
                    if k >= 1:
                        ans = max(ans, l[i]+l[i+1]+1)
                        k -= 1
            elif i == len(l)-1:
                if i-1 >= 0:
                    if l[i-1] > 1:
                        if k >= 2:
                            ans = max(ans, l[i]+l[i-1]+1)
                            k -= 2
                    else:
                        if k >= 1:
                            ans = max(ans, l[i]+l[i-1]+1)
                            k -= 1
                else:
                    if k >= 1:
                        ans = max(ans, l[i]+l[i-1]+1)
                        k -= 1
            else:
                if l[i-1] > 1 and l[i+1] > 1:
                    if k >= 3:
                        ans = max(ans, l[i-1]+l[i]+l[i+1]+2)
                        k -= 3
                elif l[i-1] > 1 and l[i+1] <= 1:
                    if k >= 2:
                        ans = max(ans, l[i-1]+l[i]+l[i+1]+1)
                        k -= 2
                elif l[i-1] <=

=======
Suggestion 8

def solve():
    S = input()
    K = int(input())
    S = S.replace('.', ' ')
    S = S.split()
    ans = 0
    for s in S:
        ans += len(s) - K + 1 if len(s) - K + 1 > 0 else 0
    print(ans)

=======
Suggestion 9

def solve(S,K):
    # S = list(S)
    S = S.replace('.','0')
    S = S.replace('X','1')
    S = list(S)
    # print(S)
    if K == 0:
        ans = 0
        cnt = 0
        for i in range(len(S)):
            if S[i] == '1':
                cnt += 1
            else:
                ans = max(ans,cnt)
                cnt = 0
        ans = max(ans,cnt)
        return ans
    else:
        ans = 0
        cnt = 0
        for i in range(len(S)):
            if S[i] == '1':
                cnt += 1
            else:
                if K > 0:
                    K -= 1
                    cnt += 1
                else:
                    ans = max(ans,cnt)
                    cnt = 0
        ans = max(ans,cnt)
        return ans

=======
Suggestion 10

def main():
    S = input()
    K = int(input())
    n = len(S)
    l = 0
    r = 0
    ans = 0
    while l < n:
        while r < n and S[r] == 'X':
            r += 1
        ans = max(ans, r - l)
        if K > 0:
            K -= 1
            r += 1
        l += 1
    print(ans)
