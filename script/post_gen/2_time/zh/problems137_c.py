Synthesizing 10/10 solutions

=======
Suggestion 1

def get_num(string):
    return sum([ord(i) for i in string])

=======
Suggestion 2

def count(s):
    #print(s)
    s = list(s)
    s.sort()
    #print(s)
    count = 0
    c = 0
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            c += 1
        else:
            count += c*(c+1)/2
            c = 0
    count += c*(c+1)/2
    return count

n = int(input())
s = []
for i in range(n):
    s.append(input())
s.sort()
#print(s)
count = 0
c = 0
for i in range(n-1):
    if s[i] == s[i+1]:
        c += 1
    else:
        count += c*(c+1)/2
        c = 0
count += c*(c+1)/2
print(int(count))

=======
Suggestion 3

def main():
    N = int(input())
    s = []
    for i in range(N):
        s.append(input())
    s.sort()
    s.append("")

    count = 0
    ans = 0
    for i in range(N):
        if s[i] == s[i + 1]:
            count += 1
        else:
            ans += count * (count + 1) // 2
            count = 0
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort()
    count = 0
    i = 0
    while i < n-1:
        j = i + 1
        while j < n and s[i] == s[j]:
            count += 1
            j += 1
        i = j
    print(count)

=======
Suggestion 5

def count_anagram(s):
    count = {}
    for c in s:
        count[c] = count.get(c, 0) + 1
    return count

=======
Suggestion 6

def problems137_c():
    pass

=======
Suggestion 7

def get_key(s):
    s_list = list(s)
    s_list.sort()
    return ''.join(s_list)

N = int(input())
s_list = []
for i in range(N):
    s_list.append(input())
s_list.sort()
s_list.append('')

count = 0
key = ''
for i in range(N):
    if key == s_list[i]:
        count += 1
    else:
        key = get_key(s_list[i])
print(count)

=======
Suggestion 8

def count(s):
    # s is a string
    # return a dictionary
    d = {}
    for c in s:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1

    return d

=======
Suggestion 9

def solve():
    n = int(input())
    s = [input() for i in range(n)]
    s.sort()
    ans = 0
    cnt = 0
    for i in range(1,n):
        if s[i] == s[i-1]:
            cnt += 1
        else:
            ans += cnt*(cnt+1)//2
            cnt = 0
    ans += cnt*(cnt+1)//2
    print(ans)

=======
Suggestion 10

def getStrHash(str):
    hash = 0
    for i in range(len(str)):
        hash += ord(str[i]) * pow(2, i)
    return hash
