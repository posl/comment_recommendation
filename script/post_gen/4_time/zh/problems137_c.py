Synthesizing 10/10 solutions

=======
Suggestion 1

def make_dict(string):
    dict = {}
    for i in string:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict

=======
Suggestion 2

def problem137_c():
    N = int(input())
    s = []
    for i in range(N):
        s.append(input())

    s.sort()

    count = 0
    for i in range(N):
        for j in range(i+1,N):
            if s[i] == s[j]:
                count += 1
    print(count)

=======
Suggestion 3

def count_anagrams(words):
    counts = {}
    for word in words:
        sorted_word = ''.join(sorted(word))
        counts[sorted_word] = counts.get(sorted_word, 0) + 1
    return sum(count * (count - 1) / 2 for count in counts.values())

=======
Suggestion 4

def main():
    N = int(input())
    s = [input() for i in range(N)]
    d = {}
    for i in range(N):
        s[i] = ''.join(sorted(s[i]))
        if s[i] in d.keys():
            d[s[i]] += 1
        else:
            d[s[i]] = 1
    ans = 0
    for v in d.values():
        ans += v * (v - 1) // 2
    print(ans)

=======
Suggestion 5

def solve():
    n = int(input())
    d = {}
    for i in range(n):
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

=======
Suggestion 6

def main():
    N = int(input())
    s = []
    for i in range(N):
        s.append(input())

    s.sort()
    ans = 0
    cnt = 0
    for i in range(N):
        if s[i] == s[i-1]:
            cnt += 1
        else:
            ans += cnt*(cnt-1)//2
            cnt = 1
    ans += cnt*(cnt-1)//2
    print(ans)

=======
Suggestion 7

def count(s):
    s = list(s)
    s.sort()
    s = ''.join(s)
    return s

=======
Suggestion 8

def count(s):
    dic={}
    for i in s:
        dic[i]=dic.get(i,0)+1
    return dic

=======
Suggestion 9

def get_hash(s):
    hash = 0
    for i in range(0, len(s)):
        hash += ord(s[i]) * pow(10, i)
    return hash

=======
Suggestion 10

def solve():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort()
    ans = 0
    cnt = 0
    for i in range(n):
        if i > 0 and s[i] == s[i-1]:
            cnt += 1
        else:
            ans += cnt * (cnt + 1) // 2
            cnt = 0
    ans += cnt * (cnt + 1) // 2
    print(ans)
