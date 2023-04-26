Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    s = [input() for _ in range(n)]
    ans = 0
    for i in range(1 << n):
        t = []
        for j in range(n):
            if i >> j & 1:
                t.append(s[j])
        if len(t) != k:
            continue
        cnt = [0] * 26
        for j in range(k):
            for c in t[j]:
                cnt[ord(c) - ord('a')] += 1
        if max(cnt) <= k:
            ans = max(ans, sum(cnt))
    print(ans)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    S = [input() for _ in range(N)]
    ans = 0
    for i in range(1 << N):
        tmp = []
        for j in range(N):
            if i & (1 << j):
                tmp.append(S[j])
        tmp = "".join(tmp)
        cnt = 0
        for c in "abcdefghijklmnopqrstuvwxyz":
            cnt += tmp.count(c) == K
        ans = max(ans, cnt)
    print(ans)

=======
Suggestion 3

def main():
    n,k = map(int,input().split())
    s = [input() for _ in range(n)]
    ans = 0
    for i in range(1<<n):
        if bin(i).count("1") != k:
            continue
        c = set()
        for j in range(n):
            if i>>j & 1:
                for k in s[j]:
                    c.add(k)
        ans = max(ans,len(c))
    print(ans)

=======
Suggestion 4

def get_input():
    n, k = map(int, input().split())
    s = []
    for i in range(n):
        s.append(input())
    return n, k, s

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    S = [input() for _ in range(N)]
    ans = 0
    for i in range(2 ** N):
        bin_i = bin(i)[2:]
        bin_i = '0' * (N - len(bin_i)) + bin_i
        bin_i = bin_i[::-1]
        tmp = ''
        for j in range(N):
            if bin_i[j] == '1':
                tmp += S[j]
        tmp = sorted(tmp)
        cnt = 0
        for j in range(len(tmp) - 1):
            if tmp[j] == tmp[j + 1]:
                cnt += 1
        if cnt == K:
            ans = max(ans, len(set(tmp)))
    print(ans)

=======
Suggestion 6

def count_char(s):
    char_dict = {}
    for i in s:
        if i in char_dict:
            char_dict[i] += 1
        else:
            char_dict[i] = 1
    return char_dict

=======
Suggestion 7

def main():
    n,k = map(int, input().split())
    s = [input() for _ in range(n)]
    alp = [0 for _ in range(26)]
    for i in range(n):
        for j in range(len(s[i])):
            alp[ord(s[i][j])-97] += 1
    alp.sort()
    ans = 0
    for i in range(26):
        if alp[25-i] >= k:
            ans += 1
    print(ans)

=======
Suggestion 8

def main():
    N,K = map(int,input().split())
    S = [input() for _ in range(N)]
    c = [0]*26
    for s in S:
        for i in range(26):
            if chr(97+i) in s:
                c[i] += 1
    c.sort(reverse=True)
    ans = 0
    for i in range(K):
        ans += c[i]
    print(ans)
main()

=======
Suggestion 9

def solve():
    N,K = map(int,input().split())
    S = []
    for _ in range(N):
        S.append(input())

    #print(S)
    #pr

=======
Suggestion 10

def solve():
    n, k = map(int, input().split())
    s = [input() for _ in range(n)]

    # 2^15 = 32768
    # 32768 * 15 = 491520
    # 491520 * 15 = 7372800
    # 7372800 * 15 = 110592000
    # 110592000 * 15 = 1658880000
    # 1658880000 * 15 = 24883200000
    # 24883200000 * 15 = 373248000000
    # 373248000000 * 15 = 5598720000000
    # 5598720000000 * 15 = 83980800000000
    # 83980800000000 * 15 = 1259712000000000
    # 1259712000000000 * 15 = 18895680000000000
    # 18895680000000000 * 15 = 283435200000000000
    # 283435200000000000 * 15 = 4251528000000000000
    # 4251528000000000000 * 15 = 63772920000000000000
    # 63772920000000000000 * 15 = 956593800000000000000
    # 956593800000000000000 * 15 = 14348907000000000000000
    # 14348907000000000000000 * 15 = 215233605000000000000000
    # 215233605000000000000000 * 15 = 3228504075000000000000000
    # 3228504075000000000000000 * 15 = 48427561125000000000000000
    # 48427561125000000000000000 * 15 = 726413416875000000000000000
    # 726413416875000000000000000 * 15 = 10896201253125000000000000000
    # 10896201253125000000000000000 * 15 = 163443018796875000000000000000
    # 163443018796875000000000000000 * 15 =
