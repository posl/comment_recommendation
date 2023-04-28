Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    d = {}
    for i in range(n):
        s = input()
        if s in d:
            d[s] += 1
        else:
            d[s] = 1
    mx = max(d.values())
    for k in sorted(d.keys()):
        if d[k] == mx:
            print(k)

=======
Suggestion 2

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    d = {}
    for s in S:
        if s in d:
            d[s] += 1
        else:
            d[s] = 1
    max_value = max(d.values())
    for k, v in sorted(d.items(), key=lambda x:x[0]):
        if v == max_value:
            print(k)

=======
Suggestion 3

def main():
    n = int(input())
    s = [input() for _ in range(n)]
    d = {}
    for i in range(n):
        if s[i] in d:
            d[s[i]] += 1
        else:
            d[s[i]] = 1
    max = 0
    for i in d:
        if max < d[i]:
            max = d[i]
    for i in sorted(d):
        if d[i] == max:
            print(i)

=======
Suggestion 4

def main():
    n = int(input())
    s = [input() for _ in range(n)]

    d = {}
    for i in range(n):
        if s[i] in d:
            d[s[i]] += 1
        else:
            d[s[i]] = 1

    m = max(d.values())
    for k, v in sorted(d.items()):
        if v == m:
            print(k)

=======
Suggestion 5

def countVotes(votes):
    votesCount = {}
    for vote in votes:
        if vote in votesCount:
            votesCount[vote] += 1
        else:
            votesCount[vote] = 1
    return votesCount

=======
Suggestion 6

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort()
    dic = {}
    for i in range(n):
        if s[i] in dic:
            dic[s[i]] += 1
        else:
            dic[s[i]] = 1
    max = 0
    for i in dic:
        if dic[i] > max:
            max = dic[i]
    for i in dic:
        if dic[i] == max:
            print(i)

=======
Suggestion 7

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort()
    max = 0
    for i in range(n):
        if max < s.count(s[i]):
            max = s.count(s[i])
    for i in range(n):
        if max == s.count(s[i]):
            print(s[i])

=======
Suggestion 8

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S.sort()
    max_count = 0
    count = 0
    for i in range(N):
        if i == 0:
            count += 1
        elif S[i] == S[i-1]:
            count += 1
        else:
            if count > max_count:
                max_count = count
            count = 1
    if count > max_count:
        max_count = count
    count = 0
    for i in range(N):
        if i == 0:
            count += 1
        elif S[i] == S[i-1]:
            count += 1
        else:
            if count == max_count:
                print(S[i-1])
            count = 1
    if count == max_count:
        print(S[i-1])

=======
Suggestion 9

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    S.sort()
    from collections import Counter
    c = Counter(S)
    max_count = max(c.values())
    for k, v in c.items():
        if v == max_count:
            print(k)

=======
Suggestion 10

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort()
    count = 1
    max_count = 0
    max_string = ''
    for i in range(n-1):
        if s[i] == s[i+1]:
            count += 1
        else:
            if count > max_count:
                max_count = count
                max_string = s[i]
            count = 1
    if count > max_count:
        max_string = s[n-1]
    print(max_string)
