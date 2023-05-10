Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    s = []
    for i in range(N):
        s.append(input())
    s.sort()
    ans = 0
    tmp = 1
    for i in range(N-1):
        if s[i] == s[i+1]:
            tmp += 1
        else:
            ans += tmp*(tmp-1)//2
            tmp = 1
    ans += tmp*(tmp-1)//2
    print(ans)
main()

=======
Suggestion 2

def solve():
    N = int(input())
    words = [input() for _ in range(N)]
    #print(words)
    d = {}
    for word in words:
        #print(word)
        word = ''.join(sorted(word))
        #print(word)
        d[word] = d.get(word, 0) + 1
        #print(d)
    ans = 0
    for v in d.values():
        ans += v * (v - 1) // 2
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    ans = 0
    dic = {}
    for i in range(N):
        s = input()
        s = ''.join(sorted(s))
        if s in dic:
            ans += dic[s]
            dic[s] += 1
        else:
            dic[s] = 1
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    s = [input() for _ in range(n)]
    d = {}
    for i in range(n):
        key = ''.join(sorted(s[i]))
        if key in d:
            d[key] += 1
        else:
            d[key] = 1
    ans = 0
    for v in d.values():
        ans += v * (v - 1) // 2
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    dic = {}
    for i in range(n):
        s = list(input())
        s.sort()
        s = ''.join(s)
        if s in dic:
            dic[s] += 1
        else:
            dic[s] = 1
    ans = 0
    for key in dic:
        ans += dic[key]*(dic[key]-1)//2
    print(ans)

=======
Suggestion 6

def get_anagram_count(s_list):
    anagram_count = 0
    anagram_dict = {}
    for s in s_list:
        s = ''.join(sorted(s))
        if s in anagram_dict:
            anagram_dict[s] += 1
        else:
            anagram_dict[s] = 1
    for key in anagram_dict.keys():
        if anagram_dict[key] > 1:
            anagram_count += anagram_dict[key] * (anagram_dict[key] - 1) // 2
    return anagram_count

=======
Suggestion 7

def main():
    N = int(input())
    d = {}
    for _ in range(N):
        s = input()
        s = ''.join(sorted(s))
        if s in d:
            d[s] += 1
        else:
            d[s] = 1
    ans = 0
    for v in d.values():
        ans += v * (v - 1) // 2
    print(ans)

=======
Suggestion 8

def solve():
    N = int(input())
    S = [input() for _ in range(N)]
    ans = 0
    dic = {}
    for s in S:
        s = ''.join(sorted(s))
        if s in dic:
            ans += dic[s]
            dic[s] += 1
        else:
            dic[s] = 1
    print(ans)

=======
Suggestion 9

def count_word(word):
    cnt = [0] * 26
    for c in word:
        cnt[ord(c) - ord('a')] += 1
    return tuple(cnt)

n = int(input())
cnt = {}
for _ in range(n):
    word = input()
    c = count_word(word)
    if c in cnt:
        cnt[c] += 1
    else:
        cnt[c] = 1

ans = 0
for v in cnt.values():
    ans += v * (v - 1) // 2
print(ans)

=======
Suggestion 10

def count_anagram(s):
    s = list(s)
    s.sort()
    s = ''.join(s)
    return s
