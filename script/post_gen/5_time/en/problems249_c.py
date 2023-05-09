Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    S = []
    for i in range(N):
        S.append(set(input()))
    ans = 0
    for i in range(1, 2 ** N):
        if bin(i).count("1") == K:
            tmp = set()
            for j in range(N):
                if (i >> j) & 1:
                    tmp |= S[j]
            ans = max(ans, len(tmp))
    print(ans)

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    s = [input() for _ in range(n)]
    ans = 0
    for i in range(1 << n):
        tmp = set()
        for j in range(n):
            if i & (1 << j):
                tmp |= set(s[j])
        if len(tmp) == k:
            ans = max(ans, bin(i).count('1'))
    print(ans)

=======
Suggestion 3

def solve():
    N, K = map(int, input().split())
    S = [input() for _ in range(N)]
    ans = 0
    for i in range(1 << N):
        c = set()
        for j in range(N):
            if (i >> j) & 1:
                c |= set(S[j])
        if len(c) == K:
            ans = max(ans, sum(1 for j in range(N) if (i >> j) & 1))
    print(ans)

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    s = [input() for _ in range(n)]
    ans = 0
    for i in range(1 << n):
        cnt = 0
        alp = [0] * 26
        for j in range(n):
            if i >> j & 1:
                cnt += 1
                for c in s[j]:
                    alp[ord(c) - 97] += 1
        if cnt != k:
            continue
        tmp = 0
        for j in range(26):
            if alp[j] > 0:
                tmp += 1
        ans = max(ans, tmp)
    print(ans)

=======
Suggestion 5

def solve():
    n,k = map(int, input().split())
    s = [input() for _ in range(n)]
    ans = 0
    for i in range(1<<n):
        t = set()
        for j in range(n):
            if i>>j&1:
                t |= set(s[j])
        if len(t) == k:
            ans = max(ans, len(t))
    print(ans)

=======
Suggestion 6

def get_input():
    n, k = map(int, input().split())
    s = [input() for _ in range(n)]
    return n, k, s

=======
Suggestion 7

def main():
  n, k = map(int, input().split())
  s = [input() for _ in range(n)]
  ans = 0
  for i in range(1, 2**n):
    t = []
    for j in range(n):
      if i & (1 << j):
        t.append(s[j])
    if len(t) < k: continue
    x = set()
    for j in range(len(t)):
      for c in t[j]:
        x.add(c)
    if len(x) == k:
      ans = max(ans, len(x))
  print(ans)

=======
Suggestion 8

def get_input():
    n, k = map(int, input().split())
    s = [input() for i in range(n)]
    return n, k, s

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    S = []
    for i in range(N):
        S.append(input())

    alphabet = [0] * 26
    for i in range(N):
        for s in S[i]:
            alphabet[ord(s) - ord('a')] += 1

    ans = 0
    for i in range(1 << N):
        temp = [0] * 26
        for j in range(N):
            if i & (1 << j):
                for s in S[j]:
                    temp[ord(s) - ord('a')] += 1

        count = 0
        for j in range(26):
            if temp[j] > 0 and alphabet[j] == temp[j]:
                count += 1
        if count == K:
            ans = max(ans, sum(temp))
    print(ans)
