Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    d = {}
    for i in range(n):
        s, t = input().split()
        if s in d:
            if d[s][0] < int(t):
                d[s] = (int(t), i)
        else:
            d[s] = (int(t), i)
    ans = sorted(d.items(), key=lambda x: (x[1][0], -x[1][1]), reverse=True)
    print(ans[0][1][1] + 1)

=======
Suggestion 2

def problems251_c():
    n=int(input())
    s=[]
    t=[]
    for i in range(n):
        temp=input().split()
        s.append(temp[0])
        t.append(int(temp[1]))
    max=0
    for i in range(n):
        if t[i]>max:
            max=t[i]
    for i in range(n):
        if t[i]==max:
            maxs=s[i]
            break
    for i in range(n):
        if s[i]==maxs and t[i]==max:
            print(i+1)
            break

=======
Suggestion 3

def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        a, b = input().split()
        s.append(a)
        t.append(int(b))
    for i in range(n):
        if s[i] == s[i+1]:
            if t[i] > t[i+1]:
                t[i+1] = t[i]
                s[i+1] = s[i]
            else:
                t[i] = t[i+1]
                s[i] = s[i+1]
    print(s.index(s[n-1])+1)

=======
Suggestion 4

def main():
    n = int(input())
    l = []
    for i in range(n):
        s,t = input().split()
        l.append((s,int(t)))
    l = sorted(l, key=lambda x: x[1], reverse=True)
    d = {}
    for i in range(n):
        if l[i][0] not in d:
            d[l[i][0]] = i+1
    print(d[l[0][0]])

=======
Suggestion 5

def main():
    n = int(input())
    dic = {}
    for i in range(n):
        s, t = input().split()
        if s in dic:
            dic[s] = min(dic[s], int(t))
        else:
            dic[s] = int(t)
    dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    print([i for i, j in enumerate(dic) if j[1] == dic[0][1]][0] + 1)

=======
Suggestion 6

def main():
    # 读取输入
    n = int(input())
    s = []
    t = []
    for i in range(n):
        s_t = input().split()
        s.append(s_t[0])
        t.append(int(s_t[1]))
    # print(s)
    # print(t)
    # 处理输入
    s_t = {}
    for i in range(n):
        if s_t.get(s[i]) == None:
            s_t[s[i]] = t[i]
        else:
            s_t[s[i]] = max(s_t[s[i]], t[i])
    # print(s_t)
    # 处理输出
    max_t = 0
    max_s = ''
    for i in range(n):
        if max_t < s_t[s[i]]:
            max_t = s_t[s[i]]
            max_s = s[i]
    # print(max_t)
    # print(max_s)
    for i in range(n):
        if max_s == s[i] and max_t == t[i]:
            print(i + 1)
            break

main()

=======
Suggestion 7

def solve():
    N = int(input())
    dic = {}
    for i in range(N):
        s, t = input().split()
        dic[s] = int(t)
    dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    print(dic[0][0])

=======
Suggestion 8

def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s,t = input().split()
        S.append(s)
        T.append(int(t))
    for i in range(N):
        if S[i] == S[i+1]:
            T[i+1] = max(T[i],T[i+1])
            T[i] = 0
    print(T.index(max(T))+1)

=======
Suggestion 9

def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        s_i, t_i = input().split()
        s.append(s_i)
        t.append(int(t_i))
    s_t = {}
    for i in range(n):
        if s[i] in s_t:
            s_t[s[i]].append((i, t[i]))
        else:
            s_t[s[i]] = [(i, t[i])]
    for key in s_t:
        s_t[key].sort(key=lambda x: x[1], reverse=True)
    s_t = sorted(s_t.items(), key=lambda x: x[1][0][1], reverse=True)
    print(s_t[0][1][0][0] + 1)

=======
Suggestion 10

def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(int(t))
    min = 1000000000
    min_index = 0
    for i in range(N):
        if S[i] not in S[:i]:
            if T[i] < min:
                min = T[i]
                min_index = i
    print(min_index + 1)
