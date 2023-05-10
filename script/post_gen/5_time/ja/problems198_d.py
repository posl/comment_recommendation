Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    s1 = input()
    s2 = input()
    s3 = input()

    if len(s1) > 10 or len(s2) > 10 or len(s3) > 10:
        print("UNSOLVABLE")
        return

    if len(s1) == 1 and len(s2) == 1 and len(s3) == 1:
        print("0\n0\n0")
        return

    alp = set(s1) | set(s2) | set(s3)
    if len(alp) > 10:
        print("UNSOLVABLE")
        return

    alp = list(alp)
    alp.sort()

    for p in permutations(range(10), len(alp)):
        d = dict(zip(alp, p))
        if d[s1[0]] == 0 or d[s2[0]] == 0 or d[s3[0]] == 0:
            continue
        n1 = 0
        for i in range(len(s1)):
            n1 = n1 * 10 + d[s1[i]]
        n2 = 0
        for i in range(len(s2)):
            n2 = n2 * 10 + d[s2[i]]
        n3 = 0
        for i in range(len(s3)):
            n3 = n3 * 10 + d[s3[i]]
        if n1 + n2 == n3:
            print(n1)
            print(n2)
            print(n3)
            return
    print("UNSOLVABLE")
    return

=======
Suggestion 2

def main():
    import sys
    input = sys.stdin.readline
    import itertools
    from collections import deque
    import bisect
    import heapq
    import math
    import copy
    import collections
    from collections import deque
    from collections import defaultdict
    from collections import Counter
    from functools import reduce

    S1 = input()[:-1]
    S2 = input()[:-1]
    S3 = input()[:-1]
    S = set(S1+S2+S3)
    if len(S)>10:
        print("UNSOLVABLE")
        exit()
    S = list(S)
    if len(S)>10:
        print("UNSOLVABLE")
        exit()
    if len(S)==10:
        for i in range(10):
            S[i] = str(i)
    else:
        for i in range(len(S)):
            S[i] = str(i)
    S = "".join(S)
    for i in range(10**(len(S1)-1),10**len(S1)):
        N1 = str(i)
        if len(set(N1))!=len(N1):
            continue
        for j in range(10**(len(S2)-1),10**len(S2)):
            N2 = str(j)
            if len(set(N2))!=len(N2):
                continue
            for k in range(10**(len(S3)-1),10**len(S3)):
                N3 = str(k)
                if len(set(N3))!=len(N3):
                    continue
                if int(N1)+int(N2)==int(N3):
                    dic = {}
                    for l in range(len(S1)):
                        dic[S1[l]] = N1[l]
                    for l in range(len(S2)):
                        dic[S2[l]] = N2[l]
                    for l in range(len(S3)):
                        dic[S3[l]] = N3[l]
                    if dic[S1[0]]=="0" or dic[S2[0]]=="0" or dic[S3[0]]=="0":
                        continue
                    for l in range(len(S1)):
                        S1 = S1.replace(S1[l],dic[S1[l]])
                    for l in range(len(S2)):
                        S2 = S2.replace(S2[l],dic[S2[l]])
                    for l in range(len(S3)):
                        S3 = S3

=======
Suggestion 3

def solve():
    from itertools import permutations
    s1 = input()
    s2 = input()
    s3 = input()
    chars = set(s1+s2+s3)
    if len(chars) > 10:
        print("UNSOLVABLE")
        return
    chars = list(chars)
    for perm in permutations(range(10), len(chars)):
        d = {c: str(d) for c, d in zip(chars, perm)}
        if d[s1[0]] == "0" or d[s2[0]] == "0" or d[s3[0]] == "0":
            continue
        n1 = int("".join(d[c] for c in s1))
        n2 = int("".join(d[c] for c in s2))
        n3 = int("".join(d[c] for c in s3))
        if n1 + n2 == n3:
            print(n1)
            print(n2)
            print(n3)
            return
    print("UNSOLVABLE")

=======
Suggestion 4

def solve():
    s1 = input()
    s2 = input()
    s3 = input()
    s1_len = len(s1)
    s2_len = len(s2)
    s3_len = len(s3)
    if s1_len > 10 or s2_len > 10 or s3_len > 10:
        print("UNSOLVABLE")
        return
    s1_set = set(s1)
    s2_set = set(s2)
    s3_set = set(s3)
    if len(s1_set) > 10 or len(s2_set) > 10 or len(s3_set) > 10:
        print("UNSOLVABLE")
        return
    s_set = s1_set | s2_set | s3_set
    if len(s_set) > 10:
        print("UNSOLVABLE")
        return
    s_list = list(s_set)
    if len(s_list) == 1:
        if s1_len == 1 and s2_len == 1 and s3_len == 1:
            print(0)
            print(0)
            print(0)
            return
        else:
            print("UNSOLVABLE")
            return
    s_list.sort()
    s1_list = list(s1)
    s2_list = list(s2)
    s3_list = list(s3)
    s1_num = 0
    s2_num = 0
    s3_num = 0
    s1_num_list = []
    s2_num_list = []
    s3_num_list = []
    for i in range(s1_len):
        s1_num_list.append(0)
    for i in range(s2_len):
        s2_num_list.append(0)
    for i in range(s3_len):
        s3_num_list.append(0)
    for i in range(s1_len):
        for j in range(len(s_list)):
            if s1_list[i] == s_list[j]:
                s1_num_list[i] = j
                break
    for i in range(s2_len):
        for j in range(len(s_list)):
            if s2_list[i] == s_list[j]:
                s2_num_list[i] = j
                break
    for i in range(s3_len):
        for j in range(len(s_list)):
            if s3_list[i]

=======
Suggestion 5

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    s1 = s1[::-1]
    s2 = s2[::-1]
    s3 = s3[::-1]
    if len(s1) > len(s3) or len(s2) > len(s3):
        print('UNSOLVABLE')
        return
    for i in range(10 ** (len(s1) - 1), 10 ** len(s1)):
        for j in range(10 ** (len(s2) - 1), 10 ** len(s2)):
            if i + j > 10 ** len(s3):
                continue
            if len(str(i)) != len(s1) or len(str(j)) != len(s2):
                continue
            s1_flag = True
            s2_flag = True
            s3_flag = True
            for k in range(len(s1)):
                if s1[k] == s2[k] and str(i)[k] != str(j)[k]:
                    s1_flag = False
                    s2_flag = False
                if s1[k] == s3[k] and str(i)[k] != str(i + j)[k]:
                    s1_flag = False
                    s3_flag = False
                if s2[k] == s3[k] and str(j)[k] != str(i + j)[k]:
                    s2_flag = False
                    s3_flag = False
            if s1_flag and s2_flag and s3_flag:
                print(i)
                print(j)
                print(i + j)
                return
    print('UNSOLVABLE')

=======
Suggestion 6

def solve(s1, s2, s3):
    # 重複文字を除いた文字リストを作成
    chars = list(set(s1 + s2 + s3))
    # 重複文字の数が10を超える場合は不正解
    if len(chars) > 10:
        return None

    # リストの先頭が0の場合は不正解
    if s1[0] in chars[0] or s2[0] in chars[0] or s3[0] in chars[0]:
        return None

    # 重複文字の数が10以下の場合は全探索
    for v in itertools.permutations(range(10), len(chars)):
        # マッピングテーブルを作成
        table = dict(zip(chars, v))
        # 先頭文字が0の場合は不正解
        if table[s1[0]] == 0 or table[s2[0]] == 0 or table[s3[0]] == 0:
            continue
        # 数値に変換
        n1 = int(''.join([str(table[s]) for s in s1]))
        n2 = int(''.join([str(table[s]) for s in s2]))
        n3 = int(''.join([str(table[s]) for s in s3]))
        # 覆面算の結果が正しい場合は正解
        if n1 + n2 == n3:
            return (n1, n2, n3)
    return None

=======
Suggestion 7

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    if len(s1) > 10 or len(s1) < 1:
        return
    if len(s2) > 10 or len(s2) < 1:
        return
    if len(s3) > 10 or len(s3) < 1:
        return
    if not s1.islower():
        return
    if not s2.islower():
        return
    if not s3.islower():
        return

    # 文字列の重複を削除して、文字列の長さが10を超えるならFalse
    if len(set(s1)) > 10:
        return
    if len(set(s2)) > 10:
        return
    if len(set(s3)) > 10:
        return

    # 文字列の長さが10を超えるならFalse
    if len(s1) > 10:
        return
    if len(s2) > 10:
        return
    if len(s3) > 10:
        return

    # 文字列の長さが1の場合
    if len(s1) == 1:
        if len(s2) == 1:
            if len(s3) == 1:
                if s1 == s2 and s1 == s3:
                    print('1')
                    print('1')
                    print('2')
                    return
                else:
                    print('UNSOLVABLE')
                    return
            else:
                print('UNSOLVABLE')
                return
        else:
            print('UNSOLVABLE')
            return
    else:
        # 文字列の長さが2以上の場合
        # 文字列の先頭が0の場合
        if s1[0] == '0' or s2[0] == '0' or s3[0] == '0':
            print('UNSOLVABLE')
            return
        else:
            # 文字列の長さが3以上の場合
            # 文字列の長さが3の場合
            if len(s1) == 3:
                if len(s2) == 3:
                    if len

=======
Suggestion 8

def solve():
    s1 = input()
    s2 = input()
    s3 = input()
    if len(s1) > 10 or len(s2) > 10 or len(s3) > 10:
        print("UNSOLVABLE")
        return

    letters = set(s1 + s2 + s3)
    if len(letters) > 10:
        print("UNSOLVABLE")
        return

    letters = list(letters)
    for perm in permutations(range(10), len(letters)):
        d = {c: str(i) for c, i in zip(letters, perm)}
        if all(d[s] != '0' for s in (s1[0], s2[0], s3[0])):
            n1 = int(''.join(d[s] for s in s1))
            n2 = int(''.join(d[s] for s in s2))
            n3 = int(''.join(d[s] for s in s3))
            if n1 + n2 == n3:
                print(n1)
                print(n2)
                print(n3)
                return
    print("UNSOLVABLE")

=======
Suggestion 9

def check(s1,s2,s3):
    num = set(s1 + s2 + s3)
    if len(num) > 10:
        return False
    num = list(num)
    for i in range(10):
        s1 = s1.replace(num[i],str(i))
        s2 = s2.replace(num[i],str(i))
        s3 = s3.replace(num[i],str(i))
    if int(s1) + int(s2) == int(s3):
        return True
    else:
        return False

s1 = input()
s2 = input()
s3 = input()
