Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    k = int(input())
    n = len(s)
    ans = 0
    cur = 0
    for i in range(n):
        if s[i] == 'X':
            cur += 1
        else:
            if k > 0:
                k -= 1
                cur += 1
            else:
                ans = max(ans, cur)
                cur = 0
    ans = max(ans, cur)
    print(ans)

=======
Suggestion 2

def main():
    S = input()
    K = int(input())
    S = S.replace('X','X.')
    S = S.split('.')
    S = [len(i) for i in S]
    S = [i for i in S if i > 0]
    if len(S) <= K:
        print(sum(S)+K-len(S))
    else:
        print(sum(S[:K])+K)

=======
Suggestion 3

def main():
    s = input()
    k = int(input())
    n = len(s)
    x = [0] * (n + 1)
    for i in range(n):
        x[i + 1] = x[i] + (s[i] == 'X')
    ans = 0
    for i in range(n + 1):
        l = i
        r = n + 1
        while r - l > 1:
            m = (r + l) // 2
            if x[m] - x[i] > k:
                r = m
            else:
                l = m
        ans = max(ans, l - i)
    print(ans)

=======
Suggestion 4

def main():
    S = input()
    K = int(input())
    count = 0
    max_count = 0
    for i in range(len(S)):
        if S[i] == 'X':
            count += 1
        else:
            if max_count < count:
                max_count = count
            count = 0
    if max_count < count:
        max_count = count
    if max_count < K:
        max_count = K
    print(max_count)
main()

=======
Suggestion 5

def main():
    s = input()
    k = int(input())
    n = len(s)
    l = []
    c = 0
    for i in range(n):
        if s[i] == 'X':
            c += 1
        else:
            l.append(c)
            c = 0
    l.append(c)
    ans = 0
    for i in range(len(l)):
        if i % 2 == 0:
            ans += l[i]
    if k == 0:
        print(ans)
        return
    if len(l) % 2 == 0:
        l.append(0)
    for i in range(0, len(l), 2):
        if k == 0:
            break
        if i == 0:
            ans += l[i] + l[i + 1]
            continue
        if l[i] <= l[i - 1] + l[i + 1]:
            ans += l[i]
            continue
        ans += l[i - 1] + l[i + 1]
        ans += 1
        k -= 1
    print(ans)

=======
Suggestion 6

def solve(s,k):
    n = len(s)
    if n == 1:
        return 1
    if n == 2:
        if k == 0:
            return 0
        else:
            return 2
    if n == 3:
        if k == 0:
            return 1
        else:
            return 3
    if n == 4:
        if k == 0:
            return 2
        else:
            return 4
    if k == 0:
        return 1
    if s[0] == '.':
        if s[1] == '.':
            if s[2] == '.':
                if s[3] == '.':
                    return 4
                else:
                    return 3
            else:
                return 2
        else:
            return 1
    if s[1] == '.':
        if s[2] == '.':
            if s[3] == '.':
                return 3
            else:
                return 2
        else:
            return 1
    if s[2] == '.':
        if s[3] == '.':
            return 2
        else:
            return 1
    if s[3] == '.':
        return 1
    return 0

s = input()
k = int(input())
print(solve(s,k))

=======
Suggestion 7

def main():
    s = input()
    k = int(input())
    n = len(s)
    a = [0] * n
    for i in range(n):
        if s[i] == 'X':
            a[i] = 1
    b = [0] * (n + 1)
    for i in range(n):
        b[i + 1] = b[i] + a[i]
    ans = 0
    for i in range(n):
        if s[i] == 'X':
            ans += 1
    for i in range(n):
        if s[i] == '.':
            ans = max(ans, b[min(i + k + 1, n)] - b[max(i - k, 0)])
    print(ans)

=======
Suggestion 8

def main():
    s = input()
    k = int(input())
    s = s.replace('.',' ')
    s = s.split()
    s = [len(i) for i in s]
    if len(s) == 1:
        print(s[0] + k)
        exit()
    ans = 0
    for i in range(len(s)):
        if i == 0 or i == len(s) - 1:
            ans = max(ans, s[i] + k)
        else:
            ans = max(ans, s[i] + k + 1)
    print(ans)

=======
Suggestion 9

def main():
    s = input()
    k = int(input())
    ans = 0
    l = len(s)
    for i in range(l):
        if s[i] == 'X':
            if i == 0:
                ans += 1
            elif s[i-1] == 'X':
                ans += 1
    for i in range(k):
        if ans == l:
            break
        if ans == 0:
            ans += 1
        elif ans == 1:
            if s[0] == '.' and s[1] == '.':
                s = s[:0] + 'X' + s[1:]
                ans += 1
            elif s[0] == '.' and s[1] == 'X':
                s = s[:1] + 'X' + s[2:]
                ans += 1
            elif s[0] == 'X' and s[1] == '.':
                s = s[:0] + 'X' + s[1:]
                ans += 1
            elif s[0] == 'X' and s[1] == 'X':
                s = s[:1] + 'X' + s[2:]
                ans += 1
        elif ans == l-1:
            if s[l-2] == '.' and s[l-1] == '.':
                s = s[:l-1] + 'X'
                ans += 1
            elif s[l-2] == '.' and s[l-1] == 'X':
                s = s[:l-2] + 'X'
                ans += 1
            elif s[l-2] == 'X' and s[l-1] == '.':
                s = s[:l-1] + 'X'
                ans += 1
            elif s[l-2] == 'X' and s[l-1] == 'X':
                s = s[:l-2] + 'X'
                ans += 1
        else:
            if s[ans] == '.':
                if s[ans-1] == '.' and s[ans+1] == '.':
                    s = s[:ans] + 'X' + s[ans+1:]
                    ans += 1
                elif s[ans-1] == '.' and s[ans+1]

=======
Suggestion 10

def solve(s, k):
    n = len(s)
    ans = 0
    for i in range(n):
        if s[i] == 'X':
            ans += 1
    for i in range(n - 1):
        if s[i] == 'X' and s[i + 1] == 'X':
            ans -= 1
    for i in range(n):
        if s[i] == '.':
            if i > 0 and s[i - 1] == 'X':
                ans += 1
            if i < n - 1 and s[i + 1] == 'X':
                ans += 1
    ans = min(ans + k * 2, n)
    return ans
