Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    d = {}
    for i in range(N):
        s = input()
        l = list(s)
        l.sort()
        s = "".join(l)
        if s in d:
            d[s] += 1
        else:
            d[s] = 1
    ans = 0
    for v in d.values():
        ans += v * (v - 1) // 2
    print(ans)

=======
Suggestion 2

def count(s):
    c = [0] * 26
    for i in range(len(s)):
        c[ord(s[i]) - ord('a')] += 1
    return tuple(c)

n = int(input())
s = [input() for _ in range(n)]
d = {}
for i in range(n):
    c = count(s[i])
    if c in d:
        d[c] += 1
    else:
        d[c] = 1
ans = 0
for v in d.values():
    ans += v * (v - 1) // 2
print(ans)

=======
Suggestion 3

def count_chars(s):
    chars = {}
    for c in s:
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return chars

N = int(input())
S = [input() for _ in range(N)]
S = list(map(count_chars, S))
S = list(map(lambda x: tuple(sorted(x.items())), S))
S = list(map(lambda x: hash(x), S))
S = list(map(lambda x: (x, S.count(x)), S))
print(sum(map(lambda x: x[1] * (x[1] - 1) // 2, S)))

=======
Suggestion 4

def count(s):
    d = {}
    for c in s:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    return d

N = int(input())
s = [input() for _ in range(N)]
d = [count(s[i]) for i in range(N)]
print(d)
ans = 0
for i in range(N-1):
    for j in range(i+1, N):
        if d[i] == d[j]:
            ans += 1
print(ans)

=======
Suggestion 5

def count(s):
    d = {}
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1

    return d

n = int(input())
s = []
for i in range(n):
    s.append(input())

d = {}
for i in range(n):
    d[i] = count(s[i])

from itertools import combinations

ans = 0
for c in combinations(range(n), 2):
    if d[c[0]] == d[c[1]]:
        ans += 1

print(ans)

=======
Suggestion 6

def getAnagramCount(s):
    count = {}
    for c in s:
        if c in count:
            count[c] += 1
        else:
            count[c] = 1
    return count

=======
Suggestion 7

def anagram(s):
    return ''.join(sorted(s))

n = int(input())
d = {}
for _ in range(n):
    s = input()
    anagram_s = anagram(s)
    if anagram_s not in d:
        d[anagram_s] = 0
    d[anagram_s] += 1
print(sum(v * (v - 1) // 2 for v in d.values()))

=======
Suggestion 8

def get_count(s):
    count_list = [0] * 26
    for c in s:
        count_list[ord(c) - ord('a')] += 1
    return tuple(count_list)

N = int(input())
count_dict = {}
for _ in range(N):
    s = input()
    count = get_count(s)
    if count not in count_dict:
        count_dict[count] = 0
    count_dict[count] += 1

ans = 0
for count in count_dict.values():
    ans += count * (count - 1) // 2
print(ans)

=======
Suggestion 9

def count(s):
    res = 0
    for i in range(26):
        res += s[i]*(s[i]-1)//2
    return res

n = int(input())
ans = 0
s = [0]*26
for _ in range(n):
    t = input()
    s[ord(t[0])-ord('a')] += 1
    ans += count(s)
print(ans)

=======
Suggestion 10

def getAnagramCount(word):
    wordSet = set(word)
    wordList = list(wordSet)
    wordList.sort()
    wordList.sort(key=len)
    wordList.reverse()
    return wordList
