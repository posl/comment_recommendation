Synthesizing 10/10 solutions

=======
Suggestion 1

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

=======
Suggestion 2

def solve():
    N = int(input())
    dic = {}
    for i in range(N):
        s = input()
        s = ''.join(sorted(s))
        if s in dic:
            dic[s] += 1
        else:
            dic[s] = 1
    ans = 0
    for k in dic:
        ans += dic[k] * (dic[k] - 1) // 2
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    d = {}
    for s in S:
        s = ''.join(sorted(s))
        d[s] = d.get(s, 0) + 1
    ans = 0
    for v in d.values():
        ans += v * (v - 1) // 2
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    S = ["".join(sorted(s)) for s in S]
    from collections import Counter
    S = Counter(S)
    ans = 0
    for s in S.values():
        ans += s * (s - 1) // 2
    print(ans)

=======
Suggestion 5

def count_anagrams(s):
    cnt = {}
    for c in s:
        if c in cnt:
            cnt[c] += 1
        else:
            cnt[c] = 1
    return cnt

n = int(input())
s = []
for i in range(n):
    s.append(input())

cnts = []
for i in range(n):
    cnts.append(count_anagrams(s[i]))

cnt = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        if cnts[i] == cnts[j]:
            cnt += 1

print(cnt)

=======
Suggestion 6

def count_anagrams(s):
    d = {}
    for i in s:
        d[i] = d.get(i, 0) + 1
    return sum([v * (v - 1) // 2 for v in d.values()])

n = int(input())
s = [input() for _ in range(n)]
d = {}
for i in s:
    i = ''.join(sorted(i))
    d[i] = d.get(i, 0) + 1
print(sum([v * (v - 1) // 2 for v in d.values()]))

=======
Suggestion 7

def count_anagram_pairs(strings):
    anagram_count = 0
    anagram_dict = {}

    for string in strings:
        sorted_string = ''.join(sorted(string))
        if sorted_string in anagram_dict:
            anagram_count += anagram_dict[sorted_string]
            anagram_dict[sorted_string] += 1
        else:
            anagram_dict[sorted_string] = 1

    return anagram_count

=======
Suggestion 8

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

=======
Suggestion 9

def get_anagram_count(s):
    anagram_count = 0
    anagram_dict = {}
    for i in range(len(s)):
        s_sorted = ''.join(sorted(s[i]))
        if s_sorted in anagram_dict:
            anagram_count += anagram_dict[s_sorted]
            anagram_dict[s_sorted] += 1
        else:
            anagram_dict[s_sorted] = 1
    return anagram_count

=======
Suggestion 10

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort()
    s.append('end')
    count = 0
    ans = 0
    for i in range(n):
        if s[i] == s[i+1]:
            count += 1
        else:
            ans += int(count*(count+1)/2)
            count = 0
    print(ans)
