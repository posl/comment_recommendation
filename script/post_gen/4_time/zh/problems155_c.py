Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    s_list = []
    for i in range(n):
        s_list.append(input())
    s_list.sort()
    max = 0
    for i in range(n):
        if s_list.count(s_list[i]) > max:
            max = s_list.count(s_list[i])
    for i in range(n):
        if s_list.count(s_list[i]) == max:
            print(s_list[i])

=======
Suggestion 2

def main():
    n = int(input())
    d = {}
    for i in range(n):
        s = input()
        if s in d:
            d[s] += 1
        else:
            d[s] = 1
    #print(d)
    m = max(d.values())
    #print(m)
    for k in sorted(d.keys()):
        if d[k] == m:
            print(k)

=======
Suggestion 3

def main():
    # 读取数据
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    # 统计票数
    d = {}
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    # 找出最多票数
    max = 0
    for i in d:
        if d[i] > max:
            max = d[i]
    # 打印最多票数的字符串
    for i in sorted(d):
        if d[i] == max:
            print(i)

=======
Suggestion 4

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
    for k in d:
        if d[k] > max:
            max = d[k]
    l = []
    for k in d:
        if d[k] == max:
            l.append(k)
    l.sort()
    for i in l:
        print(i)

=======
Suggestion 5

def main():
    n = int(input())
    s = [input() for _ in range(n)]
    s.sort()
    max_count = 0
    for i in range(n):
        if s.count(s[i]) > max_count:
            max_count = s.count(s[i])
    for i in range(n):
        if s.count(s[i]) == max_count:
            print(s[i])

=======
Suggestion 6

def main():
    n = int(input())
    s = [input() for _ in range(n)]
    max_count = 0
    for i in range(n):
        if s.count(s[i]) > max_count:
            max_count = s.count(s[i])
    max_s = []
    for i in range(n):
        if s.count(s[i]) == max_count and s[i] not in max_s:
            max_s.append(s[i])
    max_s.sort()
    for i in max_s:
        print(i)

=======
Suggestion 7

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort()
    cnt = 1
    max = 0
    ans = []
    for i in range(1, n):
        if s[i] == s[i-1]:
            cnt += 1
        else:
            if max < cnt:
                max = cnt
                ans = []
                ans.append(s[i-1])
            elif max == cnt:
                ans.append(s[i-1])
            cnt = 1
    if max < cnt:
        max = cnt
        ans = []
        ans.append(s[n-1])
    elif max == cnt:
        ans.append(s[n-1])
    for i in ans:
        print(i)

=======
Suggestion 8

def main():
    n = int(input())
    s = [input() for _ in range(n)]
    s.sort()
    s_max = 1
    s_max_list = []
    for i in range(n-1):
        if s[i] == s[i+1]:
            s_max += 1
        else:
            if s_max > 1:
                s_max_list.append(s[i])
            s_max = 1
    if s_max > 1:
        s_max_list.append(s[-1])
    for i in s_max_list:
        print(i)

=======
Suggestion 9

def main():
    i = int(input())
    ss = []
    for ii in range(i):
        ss.append(input())
    ss.sort()
    max = 0
    maxs = []
    for s in ss:
        if ss.count(s) > max:
            max = ss.count(s)
            maxs = [s]
        elif ss.count(s) == max and maxs.count(s) == 0:
            maxs.append(s)
    for s in maxs:
        print(s)

=======
Suggestion 10

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
