Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    S = [input() for _ in range(N)]
    ans = 0
    for i in range(2**N):
        tmp = []
        for j in range(N):
            if (i>>j)&1:
                tmp.append(S[j])
        if len(tmp) != K:
            continue
        cnt = 0
        for k in range(26):
            for l in tmp:
                if chr(ord('a')+k) in l:
                    cnt += 1
                    break
        ans = max(ans, cnt)
    print(ans)

=======
Suggestion 2

def get_max_count(s, k):
    c = {}
    for i in range(len(s)):
        if s[i] in c:
            c[s[i]] += 1
        else:
            c[s[i]] = 1
    count = 0
    for v in c.values():
        if v == k:
            count += 1
    return count

=======
Suggestion 3

def solve():
    N, K = map(int, input().split())
    S = [input() for _ in range(N)]
    #print(N, K, S)

    # 2^15 = 32768
    # 2^15 * 15 = 491520
    # 2^15 * 15 * 15 = 7372800
    # 2^15 * 15 * 15 * 15 = 110592000
    # 2^15 * 15 * 15 * 15 * 15 = 1658880000
    # 2^15 * 15 * 15 * 15 * 15 * 15 = 24883200000

    # 15 * 15 * 15 * 15 * 15 * 15 = 11390625
    # 15 * 15 * 15 * 15 * 15 = 759375
    # 15 * 15 * 15 * 15 = 50625
    # 15 * 15 * 15 = 3375
    # 15 * 15 = 225
    # 15 = 15

    # 2^15 * 15 * 15 * 15 * 15 * 15 = 24883200000
    # 2^15 * 15 * 15 * 15 * 15 = 1658880000
    # 2^15 * 15 * 15 * 15 = 110592000
    # 2^15 * 15 * 15 = 7372800
    # 2^15 * 15 = 491520
    # 2^15 = 32768

    # 2^15 * 15 * 15 * 15 * 15 * 15 = 24883200000
    # 2^15 * 15 * 15 * 15 * 15 = 1658880000
    # 2^15 * 15 * 15 * 15 = 110592000
    # 2^15 * 15 * 15 = 7372800
    # 2^15 * 15 = 491520
    # 2^15 = 32768

    # 2^15 * 15 * 15 * 15 *

=======
Suggestion 4

def main():
    n,k = map(int,input().split())
    s = [input() for _ in range(n)]
    ans = 0
    for i in range(1<<n):
        t = []
        for j in range(n):
            if i & 1<<j:
                t.append(s[j])
        if len(t) == k:
            x = set("".join(t))
            if len(x) > ans:
                ans = len(x)
    print(ans)

=======
Suggestion 5

def main():
    n,k = map(int, input().split())
    s = []
    for _ in range(n):
        s.append(input())
    s.sort()
    #print(s)
    ans = 0
    for i in range(2**n):
        t = []
        for j in range(n):
            if ((i>>j)&1):
                t.append(s[j])
        #print(t)
        if len(t) == 0:
            continue
        if len(t) > k:
            continue
        if len(t) == k:
            #print(t)
            temp = []
            for x in t:
                for y in x:
                    temp.append(y)
            #print(temp)
            temp.sort()
            #print(temp)
            count = 0
            for x in range(len(temp)-1):
                if temp[x] == temp[x+1]:
                    count += 1
            if count == k:
                ans = max(ans, len(set(temp)))
    print(ans)

=======
Suggestion 6

def main():
    n,k = map(int,input().split())
    s = [input() for _ in range(n)]
    ans = 0
    for i in range(2**n):
        t = []
        for j in range(n):
            if i & 1<<j:
                t.append(s[j])
        if len(t) != k:
            continue
        c = [0] * 26
        for j in t:
            for l in j:
                c[ord(l)-97] += 1
        if max(c) == k:
            ans = max(ans,sum(i>>j&1 for j in range(n)))
    print(ans)

=======
Suggestion 7

def main():
    N,K = map(int,input().split())
    S = [input() for _ in range(N)]
    ans = 0
    for i in range(1 << N):
        cnt = 0
        tmp = []
        for j in range(N):
            if i & (1 << j):
                tmp.append(S[j])
        for k in range(26):
            flg = True
            for l in range(len(tmp)):
                if chr(k + ord('a')) not in tmp[l]:
                    flg = False
                    break
            if flg:
                cnt += 1
        if cnt == K:
            ans = max(ans,len(tmp))
    print(ans)

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    S = [input() for _ in range(N)]

    # Sを2進数で表したときのビットが立っているところが登場する文字列として選ばれたものになる
    # 例えばS[0] = "abc"のとき、S[0]を選んだときのビットは00000000000000000000000001となる
    # S[0], S[1], S[2]を選んだときのビットは00000000000000000000000011となる
    # S[0], S[1], S[2], S[3]を選んだときのビットは00000000000000000000000011となる
    # このように、ビットを立てるところを全探索する
    # このとき、ビットが立っているところの文字を集めて、
    # それぞれの文字の出現数を集計して、Kと一致するものを数える
    ans = 0
    for i in range(1 << N):
        tmp = []
        for j in range(N):
            if i & (1 << j):
                tmp.append(S[j])
        if len(tmp) == 0:
            continue
        cnt = [0] * 26
        for s in tmp:
            for c in s:
                cnt[ord(c) - ord('a')] += 1
        if max(cnt) <= K:
            ans = max(ans, sum(cnt))
    print(ans)

=======
Suggestion 9

def main():
    n, k = map(int, input().split())
    s = [input() for i in range(n)]
    ans = 0
    for i in range(1 << n):
        cnt = 0
        tmp = set()
        for j in range(n):
            if i & (1 << j):
                cnt += 1
                for c in s[j]:
                    tmp.add(c)
        if cnt != k:
            continue
        if len(tmp) > ans:
            ans = len(tmp)
    print(ans)

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    S = [input() for _ in range(N)]

    # 各文字列に含まれる文字の種類数を数える
    cnt = [0] * N
    for i in range(N):
        cnt[i] = len(set(S[i]))

    # すべての組み合わせを試す
    ans = 0
    for i in range(1 << N):
        # 選んだ文字列を入れる
        selected = []
        for j in range(N):
            if (i >> j) & 1:
                selected.append(S[j])

        # 選んだ文字列に含まれる文字の種類数を数える
        num = len(set(''.join(selected)))
        if num == K:
            ans = max(ans, sum(cnt) - sum(cnt[j] for j in range(N) if (i >> j) & 1))

    print(ans)
