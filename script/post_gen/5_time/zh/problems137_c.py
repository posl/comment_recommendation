Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    words = []
    for i in range(n):
        word = input()
        words.append(word)

    words.sort()
    ans = 0
    cnt = 1
    for i in range(1, n):
        if words[i] == words[i - 1]:
            cnt += 1
        else:
            ans += cnt * (cnt - 1) // 2
            cnt = 1
    ans += cnt * (cnt - 1) // 2
    print(ans)

=======
Suggestion 2

def get_hash(text):
    hash = 0
    for i in range(len(text)):
        hash += ord(text[i]) * (i+1)
    return hash

=======
Suggestion 3

def get_hash(s):
    hash = [0]*26
    for i in range(10):
        hash[ord(s[i])-ord('a')] += 1
    return hash

n = int(input())
s = []
for i in range(n):
    s.append(input())
hash = []
for i in range(n):
    hash.append(get_hash(s[i]))

hash.sort()
ans = 0
cnt = 1
for i in range(n-1):
    if hash[i] == hash[i+1]:
        cnt += 1
    else:
        ans += cnt * (cnt-1) // 2
        cnt = 1

ans += cnt * (cnt-1) // 2
print(ans)

=======
Suggestion 4

def get_word_dict(word):
    word_dict = {}
    for i in range(len(word)):
        if word[i] in word_dict:
            word_dict[word[i]] += 1
        else:
            word_dict[word[i]] = 1
    return word_dict

=======
Suggestion 5

def problem137_c():
    N = int(input())
    s = []
    for i in range(N):
        s.append(input())
    s.sort()
    #print(s)
    count = 0
    i = 0
    while i < N:
        j = i + 1
        while j < N:
            if s[i] == s[j]:
                count += 1
            else:
                break
            j += 1
        i = j
    print(count)

=======
Suggestion 6

def get_n():
    n = int(input())
    return n

=======
Suggestion 7

def main():
    n = int(input())
    d = {}
    for i in range(n):
        s = input()
        s = sorted(s)
        s = ''.join(s)
        if s in d:
            d[s] += 1
        else:
            d[s] = 1
    ans = 0
    for i in d.values():
        ans += i * (i - 1) // 2
    print(ans)

=======
Suggestion 8

def get_char_num(s):
    char_num = [0] * 26
    for char in s:
        char_num[ord(char)-ord('a')] += 1
    return char_num

=======
Suggestion 9

def getHash(s):
    hash = [0] * 26
    for i in range(len(s)):
        hash[ord(s[i]) - ord('a')] += 1
    return hash

=======
Suggestion 10

def solve():
    n = int(input())
    s = [input() for i in range(n)]
    for i in range(n):
        s[i] = ''.join(sorted(s[i]))
    s = sorted(s)
    ans = 0
    cnt = 1
    for i in range(1, n):
        if s[i] == s[i - 1]:
            cnt += 1
        else:
            ans += cnt * (cnt - 1) // 2
            cnt = 1
    ans += cnt * (cnt - 1) // 2
    print(ans)
