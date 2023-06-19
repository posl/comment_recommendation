Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    # 读入数据
    N, K = map(int, input().split())
    S = [input() for _ in range(N)]

    # 求解
    ans = 0
    for bit in range(1 << N):
        # 选择的字符串
        T = [i for i in range(N) if bit & (1 << i)]
        # 选择的字符串的字母集合
        U = set()
        for t in T:
            U |= set(S[t])
        # 选择的字符串的字母集合的大小
        if len(U) == K:
            ans = max(ans, len(T))

    # 输出结果
    print(ans)

=======
Suggestion 2

def main():
    N,K = map(int,input().split())
    S = []
    for i in range(N):
        S.append(input())
    print(S)

=======
Suggestion 3

def main():
    N,K = map(int,input().split())
    S = []
    for i in range(N):
        S.append(input())
    ans = 0
    for i in range(2**N):
        cnt = 0
        tmp = []
        for j in range(N):
            if i&(1<<j):
                tmp.append(S[j])
                cnt += 1
        if cnt != K:
            continue
        ans = max(ans,len(set("".join(tmp))))
    print(ans)

=======
Suggestion 4

def getStrList():
    N, K = map(int, input().split())
    strList = []
    for i in range(N):
        strList.append(input())
    return strList

=======
Suggestion 5

def get_all_subsets(input_set):
    return get_all_subsets_rec(input_set,0)

=======
Suggestion 6

def get_input():
    n,k = map(int,input().split())
    s = []
    for i in range(n):
        s.append(input())
    return n,k,s

=======
Suggestion 7

def is_included(Si, Sj):
    for c in Si:
        if c in Sj:
            return True
    return False

=======
Suggestion 8

def main():
    n,k = map(int, input().split())
    s = []
    for i in range(n):
        s.append(input())

    ans = 0
    for i in range(1<<n):
        t = set()
        for j in range(n):
            if i&(1<<j):
                t |= set(s[j])

        if len(t) == k:
            ans = max(ans, bin(i).count("1"))

    print(ans)

=======
Suggestion 9

def f(s):
    return set(s)

n, k = map(int, input().split())
s = [input() for _ in range(n)]
ans = 0
for i in range(1 << n):
    if bin(i).count('1') != k:
        continue
    t = set()
    for j in range(n):
        if i >> j & 1:
            t |= f(s[j])
    if len(t) == k:
        ans = max(ans, bin(i).count('1'))
print(ans)

=======
Suggestion 10

def main():
    # 读入数据
    n, k = map(int, input().split())
    s = []
    for i in range(n):
        s.append(input())
    # 递归求解
    print(solve(s, k))
