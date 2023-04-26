Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    d = {}
    for _ in range(n):
        s = input()
        if s in d:
            d[s] += 1
        else:
            d[s] = 1
    max = 0
    for k, v in d.items():
        if v > max:
            max = v
    l = []
    for k, v in d.items():
        if v == max:
            l.append(k)
    l.sort()
    for i in l:
        print(i)

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

    max_v = max(d.values())
    for k, v in sorted(d.items()):
        if v == max_v:
            print(k)

=======
Suggestion 3

def main():
    N = int(input())
    S = [input() for i in range(N)]
    dic = {}
    for s in S:
        if s in dic:
            dic[s] += 1
        else:
            dic[s] = 1
    max = 0
    for k, v in dic.items():
        if v > max:
            max = v
    for k, v in sorted(dic.items()):
        if v == max:
            print(k)

=======
Suggestion 4

def main():
    n = int(input())
    d = {}
    for _ in range(n):
        s = input()
        d[s] = d.get(s, 0) + 1
    max_count = max(d.values())
    for k, v in sorted(d.items()):
        if v == max_count:
            print(k)

=======
Suggestion 5

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S.sort()
    max = 0
    count = 0
    for i in range(N):
        if S[i] == S[i-1]:
            count += 1
        else:
            if count > max:
                max = count
            count = 1
    if count > max:
        max = count
    count = 0
    for i in range(N):
        if S[i] == S[i-1]:
            count += 1
        else:
            if count == max:
                print(S[i-1])
            count = 1
    if count == max:
        print(S[N-1])

=======
Suggestion 6

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort()
    max = 0
    ans = []
    for i in range(n):
        if s.count(s[i]) > max:
            max = s.count(s[i])
    for i in range(n):
        if s.count(s[i]) == max:
            ans.append(s[i])
    ans = list(set(ans))
    ans.sort()
    for i in range(len(ans)):
        print(ans[i])

=======
Suggestion 7

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    S.sort()
    cnt = 1
    max_cnt = 0
    ans = []
    for i in range(N-1):
        if S[i] == S[i+1]:
            cnt+=1
        else:
            if cnt > max_cnt:
                ans = [S[i]]
                max_cnt = cnt
            elif cnt == max_cnt:
                ans.append(S[i])
            cnt = 1
    if cnt > max_cnt:
        ans = [S[-1]]
    elif cnt == max_cnt:
        ans.append(S[-1])
    for i in range(len(ans)):
        print(ans[i])

=======
Suggestion 8

def main():
    n = int(input())
    s = []
    for _ in range(n):
        s.append(input())
    s.sort()
    s_count = {}
    for i in range(n):
        if s[i] in s_count:
            s_count[s[i]] += 1
        else:
            s_count[s[i]] = 1
    max_key = max(s_count, key=s_count.get)
    for k, v in s_count.items():
        if v == s_count[max_key]:
            print(k)

=======
Suggestion 9

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    S.sort()
    S.append("")
    now = S[0]
    cnt = 1
    for i in range(1, N + 1):
        if now == S[i]:
            cnt += 1
        else:
            if cnt == max_cnt:
                print(now)
            now = S[i]
            cnt = 1
        max_cnt = max(cnt, max_cnt)

=======
Suggestion 10

def solve():
    N = int(input())
    S = [input() for _ in range(N)]
    S.sort()
    max = 0
    maxS = ""
    for i in range(N):
        if S[i] != maxS:
            maxS = S[i]
            max = 1
        else:
            max += 1
        if i == N-1:
            print(S[i])
        elif S[i+1] != maxS:
            print(S[i])
