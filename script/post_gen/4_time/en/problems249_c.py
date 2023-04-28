Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    s = [input() for _ in range(n)]
    ans = 0
    for i in range(1 << 26):
        cnt = 0
        for j in range(n):
            c = 0
            for l in range(26):
                if (i >> l) & 1:
                    if chr(97 + l) in s[j]:
                        c += 1
            if c >= k:
                cnt += 1
        if cnt == n:
            ans = max(ans, bin(i).count('1'))
    print(ans)

=======
Suggestion 2

def main():
    from itertools import combinations
    N, K = map(int, input().split())
    S = [set(input()) for _ in range(N)]
    ans = 0
    for comb in combinations(range(N), K):
        ans = max(ans, len(set().union(*[S[i] for i in comb])))
    print(ans)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    S = [input() for _ in range(N)]
    ans = 0
    for i in range(1 << N):
        if bin(i).count('1') != K:
            continue
        cnt = [0] * 26
        for j in range(N):
            if i >> j & 1:
                for k in S[j]:
                    cnt[ord(k) - ord('a')] += 1
        ans = max(ans, sum(1 for c in cnt if c == K))
    print(ans)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    S = []
    for _ in range(N):
        S.append(input())
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            Sij = S[i] + S[j]
            Sij = set(Sij)
            if len(Sij) < K:
                continue
            for k in range(j+1, N):
                Sijk = S[i] + S[j] + S[k]
                Sijk = set(Sijk)
                if len(Sijk) < K:
                    continue
                for l in range(k+1, N):
                    Sijkl = S[i] + S[j] + S[k] + S[l]
                    Sijkl = set(Sijkl)
                    if len(Sijkl) < K:
                        continue
                    for m in range(l+1, N):
                        Sijklm = S[i] + S[j] + S[k] + S[l] + S[m]
                        Sijklm = set(Sijklm)
                        if len(Sijklm) < K:
                            continue
                        for n in range(m+1, N):
                            Sijklmn = S[i] + S[j] + S[k] + S[l] + S[m] + S[n]
                            Sijklmn = set(Sijklmn)
                            if len(Sijklmn) < K:
                                continue
                            for o in range(n+1, N):
                                Sijklmno = S[i] + S[j] + S[k] + S[l] + S[m] + S[n] + S[o]
                                Sijklmno = set(Sijklmno)
                                if len(Sijklmno) < K:
                                    continue
                                for p in range(o+1, N):
                                    Sijklmnop = S[i] + S[j] + S[k] + S[l] + S[m] + S[n] + S[o] + S[p]
                                    Sijklmnop = set(Sijklmnop)
                                    if len(Sijklmnop) < K:
                                        continue
                                    for q in range(p+1, N):
                                        Sijklmnopq = S[i] + S[j] + S[k] + S[l] + S[m] + S[n] + S[o] + S[p] + S[q]
                                        Sijklmnopq = set

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    s = [list(input()) for _ in range(n)]
    ans = 0
    for i in range(26):
        cnt = 0
        for j in range(26):
            if i == j:
                continue
            for l in range(n):
                if chr(j+97) in s[l]:
                    cnt += 1
        if cnt >= n - k:
            ans += 1
    print(ans)

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    S = [input() for _ in range(N)]
    alpha = [0] * 26
    for s in S:
        for c in s:
            alpha[ord(c) - ord('a')] += 1
    alpha.sort(reverse=True)
    print(sum(alpha[:K]))

=======
Suggestion 7

def main():
    n, k = map(int, input().split())
    s = [input() for _ in range(n)]
    ans = 0
    for i in range(2**n):
        cnt = 0
        for j in range(n):
            if (i >> j) & 1:
                cnt += 1
        if cnt != k:
            continue
        a = []
        for j in range(n):
            if (i >> j) & 1:
                a.append(s[j])
        a = ''.join(a)
        cnt = 0
        for j in range(26):
            if a.count(chr(ord('a')+j)) > 0:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)

=======
Suggestion 8

def main():
    N,K = map(int, input().split())
    S = [input() for _ in range(N)]
    ans = 0
    for i in range(2**26):
        cnt = 0
        for s in S:
            if sum(1 for j in s if (i>>ord(j)-97)&1)>0:
                cnt += 1
        if cnt>=K:
            ans = max(ans, bin(i).count("1"))
    print(ans)

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    S = [input() for _ in range(N)]

    # 2^K通りの組み合わせを全探索
    ans = 0
    for i in range(1 << N):
        t = set()
        for j in range(N):
            if (i >> j) & 1:
                t |= set(S[j])
        if len(t) == K:
            ans += 1

    print(ans)

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    S = [input() for _ in range(N)]

    # 1つの文字列に含まれる文字の種類を求める
    def count(s):
        return len(set(s))

    # 1つの文字列に含まれる文字の種類を求める
    def count2(s):
        return len(set(s))

    # K個の文字列を選んだときに含まれる文字の種類を求める
    def count3(s, k):
        return len(set("".join(s[:k])))

    # K個の文字列を選んだときに含まれる文字の種類を求める
    def count4(s, k):
        return len(set("".join(s[:k])))

    # K個の文字列を選んだときに含まれる文字の種類を求める
    def count5(s, k):
        return len(set("".join(s[:k])))

    # K個の文字列を選んだときに含まれる文字の種類を求める
    def count6(s, k):
        return len(set("".join(s[:k])))

    # K個の文字列を選んだときに含まれる文字の種類を求める
    def count7(s, k):
        return len(set("".join(s[:k])))

    # K個の文字列を選んだときに含まれる文字の種類を求める
    def count8(s, k):
        return len(set("".join(s[:k])))

    # K個の文字列を選んだときに含まれる文字の種類を求める
    def count9(s, k):
        return len(set("".join(s[:k])))

    # K個の文字列を選んだときに含まれる文字の種類を求める
    def count10(s, k):
        return len(set("".join
