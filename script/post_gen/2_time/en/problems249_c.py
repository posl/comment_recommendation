Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    s = [input() for _ in range(n)]
    ans = 0
    for i in range(1 << n):
        t = set()
        for j in range(n):
            if i >> j & 1:
                t |= set(s[j])
        if len(t) >= k:
            continue
        cnt = 0
        for j in range(n):
            if i >> j & 1:
                cnt += 1
        if cnt > ans:
            ans = cnt
    print(ans)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    S = [input() for _ in range(N)]
    alphabets = set()
    for s in S:
        alphabets = alphabets | set(s)
    ans = 0
    for i in range(1, 2**N):
        s = set()
        for j in range(N):
            if (i >> j) & 1:
                s = s | set(S[j])
        if len(s) == K:
            ans = max(ans, len(alphabets & s))
    print(ans)

=======
Suggestion 3

def get_input():
    n, k = map(int, input().split())
    s = []
    for i in range(n):
        s.append(input())
    return n, k, s

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    S = [input() for _ in range(N)]
    ans = 0
    for i in range(1<<N):
        l = []
        for j in range(N):
            if i & 1<<j:
                l.append(S[j])
        if len(l) == K:
            ans = max(ans, len(set(''.join(l))))
    print(ans)

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    s = [input() for _ in range(n)]

    ans = 0
    for i in range(1, 2**n):
        tmp = set()
        for j in range(n):
            if i & (1 << j):
                tmp |= set(s[j])
        if len(tmp) == k:
            ans = max(ans, len(tmp))

    print(ans)

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    s = [input() for _ in range(n)]

    ans = 0
    for i in range(1, 2 ** n):
        b = bin(i)[2:].zfill(n)
        tmp = set()
        for j in range(n):
            if b[j] == '1':
                for c in s[j]:
                    tmp.add(c)
        if len(tmp) == k:
            ans = max(ans, len(tmp))
    print(ans)

=======
Suggestion 7

def solve(n, k, s):
    ans = 0
    for i in range(2 ** n):
        t = []
        for j in range(n):
            if ((i >> j) & 1):
                t.append(s[j])
        t = ''.join(t)
        if len(set(t)) == k:
            ans = max(ans, len(t))
    return ans

n, k = map(int, input().split())
s = [input() for _ in range(n)]
print(solve(n, k, s))

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    S = [input() for _ in range(N)]
    ans = 0
    for i in range(2**N):
        num = 0
        tmp = set()
        for j in range(N):
            if (i >> j) & 1:
                num += 1
                for s in S[j]:
                    tmp.add(s)
        if num == K:
            ans = max(ans, len(tmp))
    print(ans)

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    S = []
    for i in range(N):
        S.append(input())
    ans = 0
    for i in range(2**N):
        mask = []
        for j in range(N):
            if i >> j & 1:
                mask.append(1)
            else:
                mask.append(0)
        #print(mask)
        cnt = 0
        for j in range(N):
            if mask[j] == 1:
                cnt += len(S[j])
        if cnt == 0:
            continue
        cnt2 = 0
        for j in range(26):
            cnt3 = 0
            for k in range(N):
                if mask[k] == 1 and chr(j+97) in S[k]:
                    cnt3 += 1
            if cnt3 == K:
                cnt2 += 1
        if cnt2 > ans:
            ans = cnt2
    print(ans)

main()

=======
Suggestion 10

def main():
    import sys
    N, K = map(int, input().split())
    S = [set(input()) for _ in range(N)]

    ans = 0
    for i in range(1 << N):
        cnt = 0
        tmp = set()
        for j in range(N):
            if i & (1 << j):
                cnt += 1
                tmp |= S[j]
        if cnt == K:
            ans = max(ans, len(tmp))
    print(ans)
