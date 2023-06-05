Synthesizing 10/10 solutions

=======
Suggestion 1

def convert_to_int(string):
    return [ord(c) - ord('a') for c in string]

=======
Suggestion 2

def main():
    n = int(input())
    s = [input() for _ in range(n)]
    d = {}
    for i in range(n):
        s[i] = ''.join(sorted(s[i]))
        if s[i] in d:
            d[s[i]] += 1
        else:
            d[s[i]] = 1
    ans = 0
    for i in d:
        ans += d[i] * (d[i] - 1) // 2
    print(ans)

=======
Suggestion 3

def solve():
    N = int(input())
    s = []
    for i in range(N):
        s.append(input())
    s.sort()
    s.append('')
    ans = 0
    cnt = 1
    for i in range(N):
        if s[i] == s[i + 1]:
            cnt += 1
        else:
            ans += cnt * (cnt - 1) // 2
            cnt = 1
    print(ans)

=======
Suggestion 4

def get_key(s):
    a = [0 for i in range(26)]
    for i in s:
        a[ord(i) - ord('a')] += 1
    return tuple(a)

=======
Suggestion 5

def count(s):
    result = 0
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if s[i] == s[j]:
                result += 1
    return result

=======
Suggestion 6

def get_hash(s):
    hash = [0]*26
    for c in s:
        hash[ord(c)-ord('a')] += 1
    return hash

=======
Suggestion 7

def solve():
    N = int(input())
    s = []
    for i in range(N):
        s.append(input())
    s.sort()
    ans = 0
    cnt = 1
    for i in range(1, N):
        if s[i] == s[i-1]:
            cnt += 1
        else:
            ans += cnt * (cnt - 1) // 2
            cnt = 1
    ans += cnt * (cnt - 1) // 2
    print(ans)

=======
Suggestion 8

def solve():
    n = int(input())
    s = [input() for i in range(n)]
    d = {}
    for i in s:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    ans = 0
    for i in d:
        ans += d[i] * (d[i] - 1) // 2
    print(ans)

solve()

=======
Suggestion 9

def count_chars(s):
    chars = {}
    for c in s:
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return chars

=======
Suggestion 10

def getCharNumber(c):
    a = ord('a')
    z = ord('z')
    val = ord(c)
    if a <= val and val <= z:
        return val - a
    return -1
