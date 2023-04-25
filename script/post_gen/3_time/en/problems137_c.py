Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N = int(input())
    d = {}
    for i in range(N):
        s = input()
        s = ''.join(sorted(s))
        if s in d:
            d[s] += 1
        else:
            d[s] = 1
    ans = 0
    for k in d:
        ans += d[k] * (d[k] - 1) // 2
    print(ans)
solve()

=======
Suggestion 2

def string_to_dict(s):
    d = {}
    for c in s:
        if c in d:
            d[c] = d[c] + 1
        else:
            d[c] = 1
    return d

=======
Suggestion 3

def anagram(s):
    d = {}
    for c in s:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    return d

n = int(input())
s = [input() for _ in range(n)]

d = {}
for i in range(n):
    a = anagram(s[i])
    if a in d:
        d[a] += 1
    else:
        d[a] = 1

ans = 0
for k in d:
    ans += d[k] * (d[k] - 1) // 2
print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    s = []
    for i in range(N):
        s.append(''.join(sorted(input())))
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
Suggestion 5

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S.sort()
    ans = 0
    count = 1
    for i in range(N-1):
        if S[i] == S[i+1]:
            count += 1
        else:
            ans += int(count * (count-1) / 2)
            count = 1
    ans += int(count * (count-1) / 2)
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    d = {}
    for i in s:
        i = ''.join(sorted(i))
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    ans = 0
    for i in d:
        ans += d[i] * (d[i] - 1) // 2
    print(ans)

=======
Suggestion 7

def get_anagram_count(s):
    s = sorted(s)
    count = 0
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            count += 1
    return count

=======
Suggestion 8

def solve():
    N = int(input())
    s = [input() for _ in range(N)]
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
Suggestion 9

def main():
    N = int(input())
    s = []
    for i in range(N):
        s.append(input())
    s.sort()
    count = 0
    tmp = 0
    for i in range(N):
        if i == 0:
            tmp = 1
        elif s[i] == s[i-1]:
            tmp += 1
        else:
            count += tmp * (tmp - 1) // 2
            tmp = 1
    count += tmp * (tmp - 1) // 2
    print(count)

=======
Suggestion 10

def getAnagramCount(s):
    anagramCount = 0
    anagramDict = dict()

    for i in range(len(s)):
        sortedString = ''.join(sorted(s[i]))
        if sortedString not in anagramDict:
            anagramDict[sortedString] = 1
        else:
            anagramDict[sortedString] += 1
            anagramCount += anagramDict[sortedString]

    return anagramCount
