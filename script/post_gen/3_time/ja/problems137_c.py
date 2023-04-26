Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            if sorted(S[i]) == sorted(S[j]):
                ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    S.sort()
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            if len(S[i]) != len(S[j]):
                break
            if sorted(S[i]) == sorted(S[j]):
                ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S.sort()
    ans = 0
    for i in range(N-1):
        for j in range(i+1, N):
            if S[i] == S[j]:
                continue
            if len(S[i]) != len(S[j]):
                break
            if isAnagram(S[i], S[j]):
                ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    s = [input() for _ in range(N)]
    s.sort()
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            if s[i] == s[j]:
                continue
            if len(s[i]) != len(s[j]):
                continue
            if sorted(s[i]) == sorted(s[j]):
                ans += 1
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    s = [input() for _ in range(N)]
    s.sort()
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            if s[i] == s[j]:
                continue
            if sorted(s[i]) == sorted(s[j]):
                ans += 1
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    D = {}
    for s in S:
        d = {}
        for c in s:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
        if str(d) in D:
            D[str(d)] += 1
        else:
            D[str(d)] = 1
    ans = 0
    for v in D.values():
        ans += v * (v - 1) // 2
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    from collections import Counter
    C = [Counter(s) for s in S]
    from collections import defaultdict
    D = defaultdict(int)
    for c in C:
        D[tuple(c.items())] += 1
    ans = 0
    for n in D.values():
        ans += n*(n-1)//2
    print(ans)

=======
Suggestion 8

def main():
    #入力
    N = int(input())
    S = [input() for _ in range(N)]

    #アナグラムの数を数える
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if sorted(S[i]) == sorted(S[j]):
                ans += 1

    #出力
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    s = [input() for _ in range(N)]

    # アナグラムの数を数える
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if sorted(s[i]) == sorted(s[j]):
                count += 1

    print(count)

=======
Suggestion 10

def main():
    N = int(input())
    S = [input() for _ in range(N)]

    # ソートして辞書のキーとして利用する
    # これでアナグラムは同じキーになる
    S = [''.join(sorted(s)) for s in S]

    # 辞書を作成
    # キーがアナグラムの文字列、値がその文字列の数
    D = {}
    for s in S:
        if s in D:
            D[s] += 1
        else:
            D[s] = 1

    # 辞書の値が 2 以上のものの個数をカウント
    cnt = 0
    for v in D.values():
        if v >= 2:
            cnt += v * (v - 1) // 2

    print(cnt)
