Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    import itertools
    S, K = input().split()
    K = int(K)
    S = sorted(S)
    for i, p in enumerate(itertools.permutations(S)):
        if i == K - 1:
            print(''.join(p))
            break

=======
Suggestion 2

def permute(s):
    if len(s) == 1:
        return [s]
    else:
        res = []
        for i in range(len(s)):
            for j in permute(s[:i] + s[i+1:]):
                res.append(s[i] + j)
        return res

s, k = input().split()
k = int(k)
print(sorted(permute(s))[k-1])

=======
Suggestion 3

def main():
    S, K = input().split()
    K = int(K)
    S = sorted(S)
    ans = ""
    while True:
        if K == 1:
            ans += "".join(S)
            break
        else:
            ans += S.pop(0)
            K -= 1
    print(ans)

=======
Suggestion 4

def main():
    import sys
    sys.setrecursionlimit(100000)
    input = sys.stdin.readline

    S, K = input().split()
    K = int(K)
    S = sorted(S)
    #print(S)
    #print(K)

    def dfs(s, k):
        if s == "":
            return ""
        #print("s", s, "k", k)
        for i, c in enumerate(s):
            #print("i", i, "c", c)
            #print("len(s[:i]+s[i+1:])", len(s[:i]+s[i+1:]))
            #print("fact(len(s[:i]+s[i+1:]))", fact(len(s[:i]+s[i+1:])))
            if fact(len(s[:i]+s[i+1:])) < k:
                k -= fact(len(s[:i]+s[i+1:]))
            else:
                return c + dfs(s[:i]+s[i+1:], k)

    def fact(n):
        if n == 0:
            return 1
        else:
            return n * fact(n-1)

    print(dfs(S, K))

=======
Suggestion 5

def main():
    S, K = input().split()
    K = int(K)
    S = list(S)
    S.sort()
    S = "".join(S)
    print(S)
    print(S[K-1])

=======
Suggestion 6

def main():
    s, k = input().split()
    k = int(k)
    s = list(s)
    s.sort()
    s = ''.join(s)
    print(s)
    count = 0
    while True:
        count += 1
        if count == k:
            break
        s = next_permutation(s)
        print(s)

=======
Suggestion 7

def main():
    S, K = input().split()
    K = int(K)
    S = sorted(list(S))
    ans = []
    while S:
        i = 0
        while i < len(S):
            if i == 0:
                tmp = 1
            else:
                tmp *= i
            if tmp >= K:
                ans.append(S[i])
                S.pop(i)
                K -= (tmp // i)
                break
            i += 1
    print(''.join(ans))

=======
Suggestion 8

def main():
    S,K = input().split()
    K = int(K)
    S = sorted(S)
    ans = ''
    while len(S) > 0:
        #print(S)
        #print(ans)
        #print(K)
        #print('---')
        n = len(S)
        for i in range(n):
            if K <= math.factorial(n-1):
                ans += S[i]
                S.pop(i)
                break
            K -= math.factorial(n-1)
    print(ans)

import math
main()

=======
Suggestion 9

def main():
    S, K = input().split()
    K = int(K)
    #print(S, K)
    S = sorted(S)
    #print(S)
    #print(''.join(S))
    #print(len(S))
    #print(S[0])
    #print(S[1])
    #print(S[2])
    #print(S[3])
    #print(S[4])
    #print(S[5])
    #print(S[6])
    #print(S[7])
    #print(S[8])
    #print(S[9])
    #print(S[10])
    #print(S[11])
    #print(S[12])
    #print(S[13])
    #print(S[14])
    #print(S[15])
    #print(S[16])
    #print(S[17])
    #print(S[18])
    #print(S[19])
    #print(S[20])
    #print(S[21])
    #print(S[22])
    #print(S[23])
    #print(S[24])
    #print(S[25])
    #print(S[26])
    #print(S[27])
    #print(S[28])
    #print(S[29])
    #print(S[30])
    #print(S[31])
    #print(S[32])
    #print(S[33])
    #print(S[34])
    #print(S[35])
    #print(S[36])
    #print(S[37])
    #print(S[38])
    #print(S[39])
    #print(S[40])
    #print(S[41])
    #print(S[42])
    #print(S[43])
    #print(S[44])
    #print(S[45])
    #print(S[46])
    #print(S[47])
    #print(S[48])
    #print(S[49])
    #print(S[50])
    #print(S[51])
    #print(S[52])
    #print(S[53])
    #print(S[54])
    #print(S[55])
    #print(S[56])
    #print(S[57])
    #print(S[58])
    #print(S[59])
    #print(S[60])
    #print(S[61])
    #print(S[62])
    #print(S[63])
    #print

=======
Suggestion 10

def main():
    S, K = input().split()
    K = int(K)
    S = list(S)
    S.sort()
    S = ''.join(S)
    print(S)
    print(K)
    print(S[K-1])
