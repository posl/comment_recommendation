Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s, k = input().split()
    k = int(k)
    s = sorted(s)
    # print(s)
    # print(k)
    # print(list(set(s)))
    # print(len(list(set(s))))
    # print(len(list(set(s)))**len(s))
    # print(40320/6)
    # print(40320/2)
    # print(40320/1)

    # for i in range(len(s)):
    #     print(i)
    #     for j in range(len(s)):
    #         print(j)
    #         for k in range(len(s)):
    #             print(k)
    #             for l in range(len(s)):
    #                 print(l)
    #                 for m in range(len(s)):
    #                     print(m)
    #                     for n in range(len(s)):
    #                         print(n)
    #                         for o in range(len(s)):
    #                             print(o)
    #                             for p in range(len(s)):
    #                                 print(p)
    #                                 for q in range(len(s)):
    #                                     print(q)
    #                                     print(s[i]+s[j]+s[k]+s[l]+s[m]+s[n]+s[o]+s[p]+s[q])
    #                                     if s[i]+s[j]+s[k]+s[l]+s[m]+s[n]+s[o]+s[p]+s[q] == 'zyxwdcba':
    #                                         print('zyxwdcba')
    #

=======
Suggestion 2

def main():
    import sys
    input = sys.stdin.readline
    from itertools import permutations

    S, K = input().rstrip().split()
    K = int(K)
    S = sorted(S)
    S = ''.join(S)
    S = list(set(permutations(S)))
    S.sort()
    S = [''.join(s) for s in S]
    print(S[K-1])
main()

=======
Suggestion 3

def permutation(s):
    if len(s) == 1:
        return [s]
    else:
        p = []
        for i in range(len(s)):
            p += [s[i] + x for x in permutation(s[:i] + s[i+1:])]
        return p

s, k = input().split()
k = int(k)
p = permutation(s)
p.sort()
print(p[k-1])

=======
Suggestion 4

def permutations(arr, n):
    # 順列を出力する
    # arr: 対象配列
    # n: 順列の長さ
    # 戻り値: 順列のリスト
    if n == 0:
        return [[]]
    l = []
    for i in range(len(arr)):
        m = arr[i]
        rest = arr[:i] + arr[i+1:]
        for p in permutations(rest, n - 1):
            l.append([m] + p)
    return l

=======
Suggestion 5

def main():
    s, k = input().split()
    k = int(k)
    s = sorted(s)
    print(s)
    ans = []
    ans.append(s[0])
    for i in range(1, len(s)):
        ans.append(s[i])
        ans.append(s[i - 1] + s[i])
    ans = sorted(list(set(ans)))
    print(ans)
    print(ans[k - 1])

=======
Suggestion 6

def main():
    s, k = input().split()
    k = int(k)
    s = list(s)
    s.sort()
    ans = []
    for i in range(len(s)):
        ans.append(s[i])
        ans += sorted(s[i+1:])
        if len(ans) >= k:
            break
    print("".join(ans[:k]))

=======
Suggestion 7

def getPermutation(s, k):
    if len(s) == 1:
        return s
    n = len(s)
    fact = 1
    for i in range(2, n):
        fact *= i
    q, r = divmod(k, fact)
    return s[q] + getPermutation(s[:q] + s[q+1:], r)

s, k = input().split()
k = int(k)
s = sorted(s)
print(getPermutation(s, k-1))

=======
Suggestion 8

def main():
    S,K = input().split()
    K = int(K)
    S = sorted(S)
    #print(S)
    #print(K)
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
    #print(S[64])
    #print(S[65])
    #print(S[66

=======
Suggestion 9

def main():
    # 入力
    s, k = input().split()
    k = int(k)
    s = list(s)
    s.sort()
    # 文字列の長さ
    n = len(s)
    # 重複文字の数
    duplicate_count = 0
    # 重複文字の数をカウント
    for i in range(n-1):
        if s[i] == s[i+1]:
            duplicate_count += 1
    # 重複文字の数を排除
    s = list(set(s))
    # 文字列の長さ
    n = len(s)
    # 重複文字の数をカウント
    for i in range(n-1):
        if s[i] == s[i+1]:
            duplicate_count += 1
    # 重複文字の数を排除
    s = list(set(s))
    # 文字列の長さ
    n = len(s)
    # 重複文字の数をカウント
    for i in range(n-1):
        if s[i] == s[i+1]:
            duplicate_count += 1
    # 重複文字の数を排除
    s = list(set(s))
    # 文字列の長さ
    n = len(s)
    # 重複文字の数をカウント
    for i in range(n-1):
        if s[i] == s[i+1]:
            duplicate_count += 1
    # 重複文字の数を排除
    s = list(set(s))
    # 文字列の長さ
    n = len(s)
    # 重複文字の数をカウント
    for i in range(n-1):
        if s[i] == s[i+1]:
            duplicate_count += 1
    # 重複文字の数を排除
    s = list(set(s))
    # 文字列の長さ
    n = len(s)
    # 重複文字の数をカウント
    for i in range(n-1):
        if s[i] == s[i+1]:
            duplicate_count

=======
Suggestion 10

def get_permutation(string, k):
    if len(string) == 1:
        return string
    num = 1
    for i in range(1, len(string)):
        num *= i
    idx = k // num
    return string[idx] + get_permutation(string[:idx] + string[idx + 1:], k % num)

s, k = input().split()
k = int(k)
print(get_permutation(sorted(s), k - 1))
