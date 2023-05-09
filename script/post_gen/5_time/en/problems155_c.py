Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    d = {}
    for i in range(n):
        s = input()
        if s not in d:
            d[s] = 1
        else:
            d[s] += 1
    max_num = max(d.values())
    for s in sorted(d):
        if d[s] == max_num:
            print(s)

=======
Suggestion 2

def main():
    N = int(input())
    S = [input() for i in range(N)]
    S.sort()
    S_dict = {}
    for s in S:
        if s in S_dict:
            S_dict[s] += 1
        else:
            S_dict[s] = 1
    max_S = max(S_dict.values())
    for s in S:
        if S_dict[s] == max_S:
            print(s)
            S_dict[s] = 0

=======
Suggestion 3

def main():
    n = int(input())
    s = [input() for i in range(n)]
    s.sort()
    d = {}
    for i in s:
        d.setdefault(i, 0)
        d[i] += 1
    m = max(d.values())
    for i in d:
        if d[i] == m:
            print(i)

=======
Suggestion 4

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    S.sort()
    S_count = {}
    for s in S:
        if s not in S_count:
            S_count[s] = 1
        else:
            S_count[s] += 1
    max_count = max(S_count.values())
    for k, v in S_count.items():
        if v == max_count:
            print(k)

=======
Suggestion 5

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    S.sort()
    max_vote = 0
    vote_dict = {}
    for s in S:
        if s in vote_dict:
            vote_dict[s] += 1
        else:
            vote_dict[s] = 1
        max_vote = max(max_vote, vote_dict[s])
    for s in S:
        if vote_dict[s] == max_vote:
            print(s)

=======
Suggestion 6

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort()
    s_set = set(s)
    d = {}
    for i in s_set:
        d[i] = 0
    for i in s:
        d[i] += 1
    max = 0
    for i in s_set:
        if d[i] > max:
            max = d[i]
    for i in s_set:
        if d[i] == max:
            print(i)

=======
Suggestion 7

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    S.sort()
    max_count = 0
    max_str = ''
    count = 0
    for i in range(N):
        if i == 0:
            count = 1
        else:
            if S[i] == S[i-1]:
                count += 1
            else:
                count = 1
        if count > max_count:
            max_count = count
            max_str = S[i]
    print(max_str)

=======
Suggestion 8

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort()
    s.append("")
    max = 0
    count = 0
    for i in range(n):
        if s[i] == s[i+1]:
            count += 1
        else:
            if count > max:
                max = count
                ans = s[i]
            count = 0
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    print(S)
    from collections import Counter
    c = Counter(S)
    print(c)
    m = max(c.values())
    print(m)
    for k in sorted(k for k, v in c.items() if v == m):
        print(k)

=======
Suggestion 10

def main():
    N = int(input())
    S = [input() for i in range(N)]
    S.sort()
    max_count = 0
    max_str = ''
    cur_count = 0
    for i in range(N):
        if S[i] == max_str:
            cur_count += 1
        else:
            if cur_count > max_count:
                max_count = cur_count
            max_str = S[i]
            cur_count = 1
    if cur_count > max_count:
        max_count = cur_count
    cur_count = 0
    for i in range(N):
        if S[i] == max_str:
            cur_count += 1
        else:
            if cur_count == max_count:
                print(S[i-1])
            cur_count = 0
            max_str = S[i]
    if cur_count == max_count:
        print(S[i-1])
