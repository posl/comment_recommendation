Synthesizing 10/10 solutions

=======
Suggestion 1

def getStr(s):
    return set(s)

=======
Suggestion 2

def count(s):
    t = [0]*26
    for c in s:
        t[ord(c)-ord('a')] = 1
    return t.count(1)

=======
Suggestion 3

def check(s1,s2):
    for i in range(len(s1)):
        if s1[i] in s2:
            return False
    return True

=======
Suggestion 4

def getStr(str):
    str = str.replace("\n", "")
    str = str.replace(" ", "")
    return str

=======
Suggestion 5

def get_input():
    input_list = []
    while True:
        try:
            input_list.append(input())
        except:
            break
    return input_list

=======
Suggestion 6

def func():
    pass

=======
Suggestion 7

def main():
    # 读入
    n, k = map(int, input().split())
    s = [input() for _ in range(n)]

    # 位运算
    ans = 0
    for i in range(1 << n):
        t = set()
        for j in range(n):
            if (i >> j) & 1:
                t |= set(s[j])
        if len(t) == k:
            ans = max(ans, bin(i).count("1"))

    # 输出
    print(ans)

=======
Suggestion 8

def main():
    N,K = map(int,input().split())
    S = [input() for _ in range(N)]
    S.sort(key = lambda x: len(x))
    ans = 0
    for i in range(1<<N):
        if bin(i).count('1') != K:
            continue
        else:
            tmp = []
            for j in range(N):
                if i & (1<<j):
                    tmp.append(S[j])
            tmp = ''.join(tmp)
            if len(set(tmp)) == K:
                ans = max(ans,len(tmp))
    print(ans)

=======
Suggestion 9

def get_input():
    n, k = input().split()
    n, k = int(n), int(k)
    s = []
    for i in range(n):
        s.append(input())
    return n, k, s

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    S = [input() for _ in range(N)]
    ans = 0
    for i in range(1 << N):
        T = []
        for j in range(N):
            if i >> j & 1:
                T.append(S[j])
        if len(T) != K:
            continue
        cnt = 0
        for c in range(26):
            for t in T:
                if chr(c + 97) in t:
                    cnt += 1
                    break
        if cnt == K:
            ans = max(ans, len(T))
    print(ans)
