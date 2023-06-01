Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    n=int(input())
    s=[input() for i in range(n)]
    dic={}
    for i in range(n):
        s[i]="".join(sorted(s[i]))
        if s[i] in dic:
            dic[s[i]]+=1
        else:
            dic[s[i]]=1
    ans=0
    for key in dic:
        ans+=dic[key]*(dic[key]-1)//2
    print(ans)

solve()

=======
Suggestion 2

def main():
    N = int(input())
    s = []
    for i in range(N):
        s.append(input())
    s.sort()
    s.append('end')
    cnt = 0
    ans = 0
    for i in range(N):
        if s[i] == s[i+1]:
            cnt += 1
        else:
            ans += (cnt+1)*cnt//2
            cnt = 0
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

n = int(input())
strings = []
for i in range(n):
    strings.append(input())

strings_chars = []
for s in strings:
    strings_chars.append(count_chars(s))

count = 0
for i in range(n):
    for j in range(i+1, n):
        if strings_chars[i] == strings_chars[j]:
            count += 1

print(count)

=======
Suggestion 4

def count_anagrams(arr):
    anagrams = {}
    for s in arr:
        key = ''.join(sorted(s))
        if key in anagrams:
            anagrams[key] += 1
        else:
            anagrams[key] = 1

    count = 0
    for key in anagrams:
        n = anagrams[key]
        count += n * (n-1) / 2

    return count

=======
Suggestion 5

def problem137_c():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())

    s.sort()
    ans = 0
    cnt = 1
    for i in range(1, n):
        if s[i] == s[i-1]:
            cnt += 1
        else:
            ans += cnt * (cnt - 1) // 2
            cnt = 1
    ans += cnt * (cnt - 1) // 2
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort()
    #print(s)
    count = 0
    for i in range(n-1):
        if s[i] == s[i+1]:
            count += 1
    print(count)
main()

=======
Suggestion 7

def get_char_list(str):
    char_list = []
    for i in range(0, 26):
        char_list.append(0)
    for i in range(0, len(str)):
        char_list[ord(str[i]) - ord('a')] += 1
    return char_list

=======
Suggestion 8

def main():
    N = int(input())
    strs = []
    for i in range(N):
        strs.append(input())
    strs.sort()
    cnt = 0
    ans = 0
    for i in range(N):
        if strs[i] == strs[i-1]:
            cnt += 1
        else:
            cnt = 0
        ans += cnt
    print(ans)

=======
Suggestion 9

def get_char_list(str):
    char_list = []
    for i in range(len(str)):
        if str[i] not in char_list:
            char_list.append(str[i])
    return char_list

=======
Suggestion 10

def hash(s):
    h = 0
    for i in range(0, len(s)):
        h = h * 26 + ord(s[i]) - ord('a')
    return h

n = int(input())
d = {}
for i in range(0, n):
    s = input()
    h = hash(s)
    if h in d:
        d[h] += 1
    else:
        d[h] = 1
ans = 0
for k in d:
    v = d[k]
    ans += v * (v - 1) // 2
print(ans)
