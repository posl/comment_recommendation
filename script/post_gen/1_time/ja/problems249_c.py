Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    S = [input() for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            cnt = 0
            for c in S[i]:
                if c in S[j]:
                    cnt += 1
            if cnt >= K:
                ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    S = [input() for _ in range(N)]
    cnt = [0] * 26
    for i in range(N):
        for j in range(len(S[i])):
            cnt[ord(S[i][j]) - ord('a')] += 1
    cnt.sort(reverse=True)
    print(sum(cnt[:K]))

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    S = [input() for _ in range(N)]
    ans = 0
    for i in range(2 ** N):
        bit = bin(i)[2:].zfill(N)
        if bit.count("1") != K:
            continue
        s = set()
        for j, b in enumerate(bit):
            if b == "1":
                s |= set(S[j])
        ans = max(ans, len(s))
    print(ans)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    S = [input() for i in range(N)]
    print(solve(N, K, S))

=======
Suggestion 5

def main():
    import sys
    from itertools import combinations
    from collections import Counter
    input = sys.stdin.readline
    N, K = map(int, input().split())
    S = [input().rstrip() for _ in range(N)]
    L = []
    for s in S:
        L += list(s)
    C = Counter(L)
    L = [x for x in C if C[x] >= K]
    ans = 0
    for i in range(K, len(L)+1):
        for c in combinations(L, i):
            cnt = 0
            for s in S:
                for x in c:
                    if x in s:
                        cnt += 1
                        break
            if cnt == K:
                ans = i
    print(ans)

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    S = [set(input()) for _ in range(N)]
    print(dfs(0, S, K, set()))

=======
Suggestion 7

def main():
    n,k = map(int,input().split())
    s = [input() for i in range(n)]
    print(solve(n,k,s))

=======
Suggestion 8

def solve():
    N, K = map(int, input().split())
    S = [input() for _ in range(N)]

    # すべての文字列の集合を作る
    all_str = set()
    for s in S:
        for c in s:
            all_str.add(c)

    # 選ぶ文字列の集合を作る
    choose_str = set()
    for s in S:
        if len(s) < K:
            continue
        for c in s:
            choose_str.add(c)

    # 選ぶ文字列の集合からすべての文字列の集合を引く
    diff = all_str - choose_str

    # 選ばない文字列の集合からすべての文字列の集合を引く
    diff2 = all_str - diff

    # 選ぶ文字列の集合から選ばない文字列の集合を引く
    diff3 = choose_str - diff2

    # 選ぶ文字列の集合から選ばない文字列の集合を引く
    diff4 = choose_str - diff3

    # 選ぶ文字列の集合から選ばない文字列の集合を引く
    diff5 = choose_str - diff4

    # 選ぶ文字列の集合から選ばない文字列の集合を引く
    diff6 = choose_str - diff5

    # 選ぶ文字列の集合から選

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    S = [input() for _ in range(N)]
    #各文字列に含まれる文字を集合として保持
    S = [set(s) for s in S]
    #全ての文字列を結合した集合
    allS = set()
    for s in S:
        allS |= s
    #全ての文字列を結合した集合の要素数
    allSlen = len(allS)
    #全ての文字列を結合した集合の各要素の出現回数
    allScount = [0]*allSlen
    #各文字列を結合した集合の各要素の出現回数をカウント
    for s in S:
        for i, v in enumerate(allS):
            if v in s:
                allScount[i] += 1
    #出現回数がKと同じ要素数をカウント
    count = 0
    for c in allScount:
        if c == K:
            count += 1
    print(count)

=======
Suggestion 10

def main():
    import sys
    import re
    from collections import Counter
    from itertools import combinations

    N, K = map(int, input().split())
    S = [input() for _ in range(N)]
    # 重複を除いた文字列を作成
    S2 = []
    for s in S:
        S2.append("".join(set(s)))
    # 重複しない文字列の組み合わせを作成
    comb = combinations(S2, K)
    # 重複しない文字列の組み合わせの文字数をカウント
    count = []
    for c in comb:
        count.append(len("".join(c)))
    # 最大値を出力
    print(max(count))
