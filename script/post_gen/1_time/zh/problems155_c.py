Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    n = int(input())
    d = {}
    for _ in range(n):
        s = input()
        if s not in d:
            d[s] = 1
        else:
            d[s] += 1
    
    max_v = max(d.values())
    for k, v in d.items():
        if v == max_v:
            print(k)

=======
Suggestion 2

def main():
    n = int(input())
    list = []
    for i in range(n):
        list.append(input())
    list.sort()
    d = {}
    for i in list:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    max = 0
    for i in d:
        if d[i] > max:
            max = d[i]
    for i in d:
        if d[i] == max:
            print(i)

=======
Suggestion 3

def solve():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S.sort()
    max_count = 0
    max_word = ''
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
            max_word = S[i]
    print(max_word)

=======
Suggestion 4

def get_input():
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(input())
    return arr

=======
Suggestion 5

def main():
    n = int(input())
    s = [input() for _ in range(n)]
    s.sort()
    res = []
    max_cnt = 0
    cnt = 0
    for i in range(n):
        if s[i] != s[i-1]:
            if cnt > max_cnt:
                max_cnt = cnt
                res = [s[i-1]]
            elif cnt == max_cnt:
                res.append(s[i-1])
            cnt = 1
        else:
            cnt += 1
    if cnt > max_cnt:
        res = [s[-1]]
    elif cnt == max_cnt:
        res.append(s[-1])
    for r in res:
        print(r)

=======
Suggestion 6

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort()
    count = 1
    max = 0
    for i in range(n-1):
        if s[i] == s[i+1]:
            count += 1
        else:
            if count > max:
                max = count
            count = 1
    if count > max:
        max = count
    count = 1
    for i in range(n-1):
        if s[i] == s[i+1]:
            count += 1
        else:
            if count == max:
                print(s[i])
            count = 1
    if count == max:
        print(s[n-1])

=======
Suggestion 7

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
    for key in sorted(dic):
        if dic[key] == max:
            print(key)

=======
Suggestion 8

def main():
    N = int(input())
    S = [input() for i in range(N)]
    S.sort()
    max_count = 0
    count = 0
    for i in range(1, N):
        if S[i] == S[i - 1]:
            count += 1
        else:
            if count > max_count:
                max_count = count
            count = 0
    if count > max_count:
        max_count = count
    count = 0
    for i in range(1, N):
        if S[i] == S[i - 1]:
            count += 1
        else:
            if count == max_count:
                print(S[i - 1])
            count = 0
    if count == max_count:
        print(S[i - 1])

=======
Suggestion 9

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
            count = 1
        if count > max:
            max = count
    count = 0
    for i in range(N):
        if S[i] == S[i-1]:
            count += 1
        else:
            count = 1
        if count == max:
            print(S[i])

=======
Suggestion 10

def main():
    n = int(input())
    d = {}
    for i in range(n):
        s = input()
        if s in d:
            d[s] += 1
        else:
            d[s] = 1
    max = 0
    for s in d:
        if d[s] > max:
            max = d[s]
    for s in sorted(d):
        if d[s] == max:
            print(s)
