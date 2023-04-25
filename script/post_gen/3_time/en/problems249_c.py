Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    S = [input() for _ in range(N)]
    ans = 0
    for i in range(1 << 26):
        cnt = 0
        for s in S:
            mask = 0
            for c in s:
                mask |= 1 << (ord(c) - ord('a'))
            if bin(mask & i).count('1') >= K:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    S = [input() for i in range(N)]
    ans = 0
    for i in range(1 << 26):
        cnt = 0
        for j in range(N):
            cnt += all(i >> ord(s) & 1 for s in S[j])
        if cnt >= K:
            ans = max(ans, bin(i).count("1"))
    print(ans)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    S = [set(input()) for _ in range(N)]
    ans = 0
    for i in range(1 << 26):
        cnt = 0
        for j in range(N):
            if len(S[j] & set(chr(ord('a') + k) for k in range(26) if i >> k & 1)) >= K:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    S = [input() for i in range(N)]
    ans = 0
    for i in range(2 ** 26):
        cnt = 0
        for j in range(N):
            tmp = 0
            for k in S[j]:
                if i >> (ord(k) - ord('a')) & 1:
                    tmp += 1
            if tmp >= K:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    s = [set(input()) for _ in range(n)]
    ans = 0
    for i in range(1 << n):
        if bin(i).count("1") != k:
            continue
        t = set()
        for j in range(n):
            if (i >> j) & 1:
                t |= s[j]
        ans = max(ans, len(t))
    print(ans)

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    s = [input() for i in range(n)]
    ans = 0
    for bit in range(1 << 26):
        cnt = 0
        for i in range(n):
            flag = True
            for j in range(len(s[i])):
                if bit & (1 << (ord(s[i][j]) - ord('a'))) == 0:
                    flag = False
                    break
            if flag:
                cnt += 1
        if cnt >= k:
            ans = max(ans, bin(bit).count('1'))
    print(ans)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    S = [input() for _ in range(N)]
    ans = 0
    for i in range(1 << N):
        if bin(i).count("1") != K:
            continue
        s = set()
        for j in range(N):
            if i >> j & 1:
                s |= set(S[j])
        ans = max(ans, len(s))
    print(ans)

=======
Suggestion 8

def main():
    n, k = map(int, input().split())
    s = [input() for _ in range(n)]
    ans = 0
    for i in range(2 ** n):
        t = []
        for j in range(n):
            if (i >> j) & 1:
                t.append(s[j])
        u = set()
        for x in t:
            for y in x:
                u.add(y)
        c = 0
        for x in u:
            if sum(x in y for y in t) == k:
                c += 1
        ans = max(ans, c)
    print(ans)

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    S = [input() for _ in range(N)]
    S = [set(s) for s in S]
    alpha = set()
    for s in S:
        alpha |= s
    alpha = list(alpha)
    alpha.sort()
    ans = 0
    for i in range(2 ** len(alpha)):
        cnt = 0
        for j in range(N):
            if sum([1 if alpha[k] in S[j] else 0 for k in range(len(alpha)) if i >> k & 1]) >= K:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)

=======
Suggestion 10

def main():
    # Read the input
    N, K = map(int, input().split())
    S = [input() for _ in range(N)]

    # Count the number of times each alphabet occurs in each string
    cnts = [Counter(s) for s in S]

    # The answer is the maximum number of distinct alphabets that satisfy the condition
    ans = 0

    # Try all 26 alphabets
    for i in range(26):
        # The alphabet we are trying
        c = chr(ord('a') + i)

        # How many strings contain the alphabet
        num = 0

        # Count the number of strings that contain the alphabet
        for cnt in cnts:
            if cnt[c] > 0:
                num += 1

        # If the number of strings that contain the alphabet is less than K, we cannot use the alphabet
        if num < K:
            continue

        # If the number of strings that contain the alphabet is greater than or equal to K, we can use the alphabet
        # Try all possible combinations of strings that contain the alphabet
        for comb in combinations(cnts, num):
            # Count the number of times the alphabet occurs in the strings
            cnt = Counter()
            for c in comb:
                cnt += c

            # If the alphabet occurs in exactly K of the strings, update the answer
            if cnt[c] == K:
                ans = max(ans, num)

    # Print the answer
    print(ans)
