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
            for c in s:
                if (1 << (ord(c) - ord('a'))) & i:
                    cnt += 1
                    break
        if cnt >= K:
            ans = max(ans, bin(i).count('1'))
    print(ans)

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    s = [set(input()) for _ in range(n)]
    ans = 0
    for i in range(1 << n):
        if bin(i).count("1") != k:
            continue
        t = set()
        for j in range(n):
            if i >> j & 1:
                t |= s[j]
        ans = max(ans, len(t))
    print(ans)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    S = [input() for _ in range(N)]
    ans = 0
    for i in range(1<<26):
        cnt = 0
        for s in S:
            tmp = 0
            for j in range(26):
                if i>>j & 1:
                    tmp |= 1<<ord(s[j])-97
            if bin(tmp).count("1") == K:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    S = [input() for _ in range(N)]
    ans = 0
    for i in range(1 << N):
        cnt = 0
        for j in range(N):
            if i & (1 << j):
                cnt += 1
        if cnt != K:
            continue
        tmp = 0
        for j in range(26):
            ok = True
            for k in range(N):
                if i & (1 << k) and chr(ord("a") + j) not in S[k]:
                    ok = False
            if ok:
                tmp += 1
        ans = max(ans, tmp)
    print(ans)

=======
Suggestion 5

def main():
    N,K = map(int,input().split())
    S = [input() for _ in range(N)]
    ans = 0
    for i in range(2**26):
        cnt = 0
        for j in range(N):
            tmp = 0
            for k in range(26):
                if (i>>k)&1:
                    if chr(97+k) in S[j]:
                        tmp += 1
            if tmp >= K:
                cnt += 1
        ans = max(ans,cnt)
    print(ans)

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    S = [input() for _ in range(N)]
    ans = 0
    for i in range(2 ** 26):
        bit = bin(i)[2:].zfill(26)
        cnt = 0
        for s in S:
            for j in s:
                if bit[ord(j) - ord("a")] == "0":
                    break
            else:
                cnt += 1
        if cnt >= K:
            ans = max(ans, bit.count("1"))
    print(ans)

=======
Suggestion 7

def solve():
    N, K = map(int, input().split())
    S = [input() for _ in range(N)]
    ans = 0
    for i in range(1 << N):
        cnt = 0
        for j in range(N):
            if i >> j & 1:
                cnt += 1
        if cnt != K:
            continue
        tmp = 0
        for j in range(26):
            ok = True
            for k in range(N):
                if i >> k & 1:
                    if chr(ord('a') + j) not in S[k]:
                        ok = False
            if ok:
                tmp += 1
        ans = max(ans, tmp)
    print(ans)

=======
Suggestion 8

def main():
    #input
    N, K = map(int, input().split())
    S = [input() for _ in range(N)]
    #solve
    #bit全探索
    ans = 0
    for i in range(1<<26):
        cnt = 0
        for s in S:
            flag = True
            for j in s:
                if not(i&(1<<(ord(j)-97))):
                    flag = False
                    break
            if flag:
                cnt += 1
        if cnt >= K:
            ans = max(ans, bin(i).count("1"))
    #output
    print(ans)

=======
Suggestion 9

def solve(N, K, S):
    ans = 0
    for i in range(2 ** 26):
        cnt = 0
        for j in range(N):
            for k in range(26):
                if (((i >> k) & 1) == 1) and (chr(97 + k) in S[j]):
                    cnt += 1
                    break
        if cnt == K:
            ans = max(ans, bin(i).count("1"))
    return ans

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    S = [input() for _ in range(N)]

    # 2^N通りの組み合わせを調べる
    ans = 0
    for i in range(1 << N):
        # iの各ビットが立っているかどうかで、Sのどの文字列を選択するかを決める
        selected = []
        for j in range(N):
            if i & (1 << j):
                selected.append(S[j])

        # 選択した文字列から、K個の文字列に含まれる文字を集める
        used = set()
        for s in selected:
            for c in s:
                used.add(c)

        # 集めた文字列のうち、K個の文字列に含まれる文字の数を数える
        cnt = 0
        for c in used:
            for s in selected:
                if c in s:
                    cnt += 1
                    break

        # K個の文字列に含まれる文字の数がKと等しいとき、答えとして更新する
        if cnt == K:
            ans = max(ans, len(used))

    print(ans)

main()
