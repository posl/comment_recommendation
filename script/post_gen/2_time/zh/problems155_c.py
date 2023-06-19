Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    dic = {}
    for i in range(n):
        word = input()
        dic[word] = dic.get(word, 0) + 1
    max = 0
    for key in dic:
        if max < dic[key]:
            max = dic[key]
    for key in sorted(dic):
        if dic[key] == max:
            print(key)

main()

=======
Suggestion 2

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort()
    max = 0
    for i in range(n):
        if s.count(s[i]) > max:
            max = s.count(s[i])
    for i in range(n):
        if s.count(s[i]) == max:
            print(s[i])

=======
Suggestion 3

def main():
    n = int(input())
    s = dict()
    for i in range(n):
        tmp = input()
        if tmp not in s:
            s[tmp] = 1
        else:
            s[tmp] += 1
    max = 0
    for key in s.keys():
        if s[key] > max:
            max = s[key]
    for key in s.keys():
        if s[key] == max:
            print(key)

=======
Suggestion 4

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S.sort()
    max = 0
    for i in range(N):
        if S[i] != S[i-1]:
            count = S.count(S[i])
            if max < count:
                max = count
    for i in range(N):
        if S[i] != S[i-1]:
            count = S.count(S[i])
            if max == count:
                print(S[i])

=======
Suggestion 5

def main():
    n = int(input())
    l = []
    for i in range(n):
        l.append(input())
    l.sort()
    max = 1
    for i in range(n-1):
        if l[i] == l[i+1]:
            max += 1
        else:
            max = 1
        if max > (n//2):
            print(l[i])
            break

main()

=======
Suggestion 6

def problems155_c():
    pass

=======
Suggestion 7

def main():
    n = int(input())
    s = [input() for i in range(n)]
    s.sort()
    max = 0
    count = 1
    for i in range(1,n):
        if s[i] == s[i-1]:
            count += 1
        else:
            if max < count:
                max = count
            count = 1
    if max < count:
        max = count
    count = 1
    for i in range(1,n):
        if s[i] == s[i-1]:
            count += 1
        else:
            if max == count:
                print(s[i-1])
            count = 1
    if max == count:
        print(s[n-1])

=======
Suggestion 8

def main():
    n = int(input())
    dic = {}
    for i in range(n):
        s = input()
        if s in dic:
            dic[s] += 1
        else:
            dic[s] = 1
    max = 0
    for key in dic:
        if dic[key] > max:
            max = dic[key]
    ans = []
    for key in dic:
        if dic[key] == max:
            ans.append(key)
    ans.sort()
    for s in ans:
        print(s)

=======
Suggestion 9

def main():
    n = int(input())
    d = {}
    for i in range(n):
        s = input()
        if s in d:
            d[s] += 1
        else:
            d[s] = 1
    max_vote = max(d.values())
    for k in sorted(d.keys()):
        if d[k] == max_vote:
            print(k)
