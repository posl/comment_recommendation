Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N = int(input())
    S = [sorted(input()) for i in range(N)]
    S.sort()
    ans = 0
    cnt = 0
    for i in range(N-1):
        if S[i]==S[i+1]:
            cnt += 1
        else:
            ans += cnt*(cnt+1)//2
            cnt = 0
    ans += cnt*(cnt+1)//2
    print(ans)

=======
Suggestion 2

def solve():
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
    for key in d:
        ans += d[key] * (d[key] - 1) // 2
    print(ans)
solve()

=======
Suggestion 3

def solve():
    n = int(input())
    s = [input() for _ in range(n)]
    d = {}
    for i in range(n):
        k = ''.join(sorted(s[i]))
        if k in d:
            d[k] += 1
        else:
            d[k] = 1
    ans = 0
    for k, v in d.items():
        ans += v * (v - 1) // 2
    print(ans)

=======
Suggestion 4

def solve():
    anagram = {}
    n = int(input())
    for i in range(n):
        s = input()
        s = ''.join(sorted(s))
        if s in anagram:
            anagram[s] += 1
        else:
            anagram[s] = 1
    ans = 0
    for i in anagram.values():
        ans += i*(i-1)//2
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(sorted(input()))
    S.sort()
    cnt = 0
    tmp = 0
    for i in range(N):
        if S[i] == S[i-1]:
            cnt += tmp
            tmp += 1
        else:
            tmp = 1
    print(cnt)
main()

=======
Suggestion 6

def solve():
    N = int(input())
    l = []
    for i in range(N):
        s = input()
        l.append(''.join(sorted(s)))
    l.sort()
    ans = 0
    count = 1
    for i in range(1,N):
        if l[i-1] == l[i]:
            count += 1
        else:
            ans += count * (count-1) // 2
            count = 1
    ans += count * (count-1) // 2
    print(ans)

=======
Suggestion 7

def count_anagrams(s):
    c = [0] * 26
    for i in range(10):
        c[ord(s[i]) - ord('a')] += 1
    return tuple(c)

N = int(input())
S = [input() for _ in range(N)]

from collections import Counter
c = Counter(count_anagrams(s) for s in S)

ans = 0
for v in c.values():
    ans += v * (v - 1) // 2
print(ans)

=======
Suggestion 8

def solve():
    N = int(input())
    S = [input() for _ in range(N)]
    S.sort()
    C = [0]*N
    for i in range(N):
        C[i] = tuple(sorted(S[i]))
    C.sort()
    ans = 0
    cnt = 0
    for i in range(N-1):
        if C[i] == C[i+1]:
            cnt += 1
        else:
            ans += cnt*(cnt+1)//2
            cnt = 0
    ans += cnt*(cnt+1)//2
    print(ans)

=======
Suggestion 9

def anagram(s):
    s = sorted(s)
    return ''.join(s)

n = int(input())
s = []
for i in range(n):
    s.append(anagram(input()))

s = sorted(s)
ans = 0
cnt = 1
for i in range(1, n):
    if s[i-1] == s[i]:
        cnt += 1
    else:
        ans += cnt*(cnt-1)//2
        cnt = 1
ans += cnt*(cnt-1)//2
print(ans)

=======
Suggestion 10

def get_anagram_count(str1, str2):
    return (sorted(str1) == sorted(str2))
