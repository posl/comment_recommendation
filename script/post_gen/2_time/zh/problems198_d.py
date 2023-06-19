Synthesizing 10/10 solutions

=======
Suggestion 1

def solve(s1, s2, s3):
    s = set(s1 + s2 + s3)
    if len(s) > 10:
        return False
    chars = tuple(s)
    n = len(chars)
    if n > 10:
        return False
    for perm in permutations(range(10), n):
        d = dict(zip(chars, perm))
        if any(d[s[0]] == 0 for s in (s1, s2, s3)):
            continue
        n1 = int(''.join(str(d[c]) for c in s1))
        n2 = int(''.join(str(d[c]) for c in s2))
        n3 = int(''.join(str(d[c]) for c in s3))
        if n1 + n2 == n3:
            return n1, n2, n3
    return False

from itertools import permutations

s1 = input()
s2 = input()
s3 = input()

ans = solve(s1, s2, s3)

=======
Suggestion 2

def solve():
    s1 = input()
    s2 = input()
    s3 = input()
    s = set(s1+s2+s3)
    if len(s) > 10:
        print('UNSOLVABLE')
        return
    s = list(s)
    s.sort()
    a = [0]*len(s)
    for i in range(len(s)):
        a[i] = i
    while True:
        if a[0] == 0 or a[len(a)-len(s1)] == 0 or a[len(a)-len(s2)] == 0 or a[len(a)-len(s3)] == 0:
            a = next_permutation(a)
            if a is None:
                print('UNSOLVABLE')
                return
            continue
        d = {}
        for i in range(len(s)):
            d[s[i]] = a[i]
        if d[s1[0]] + d[s2[0]] != d[s3[0]]:
            a = next_permutation(a)
            if a is None:
                print('UNSOLVABLE')
                return
            continue
        n1 = 0
        for i in range(len(s1)):
            n1 = n1*10 + d[s1[i]]
        n2 = 0
        for i in range(len(s2)):
            n2 = n2*10 + d[s2[i]]
        n3 = 0
        for i in range(len(s3)):
            n3 = n3*10 + d[s3[i]]
        if n1 + n2 != n3:
            a = next_permutation(a)
            if a is None:
                print('UNSOLVABLE')
                return
            continue
        print(n1)
        print(n2)
        print(n3)
        return

=======
Suggestion 3

def solve(s1,s2,s3):
    #print(s1,s2,s3)
    s1_len = len(s1)
    s2_len = len(s2)
    s3_len = len(s3)
    s1_set = set(s1)
    s2_set = set(s2)
    s3_set = set(s3)
    s_set = s1_set.union(s2_set).union(s3_set)
    #print(s1_set,s2_set,s3_set,s_set)
    if len(s_set) > 10:
        return False
    if s1_len > s3_len or s2_len > s3_len:
        return False
    if s1_len < s3_len and s2_len < s3_len:
        return False
    for i in range(0,10):
        for j in range(0,10):
            for k in range(0,10):
                if i in s_set and j in s_set and k in s_set:
                    if s1_len == s3_len:
                        if s1.count(list(s_set)[i]) != s3.count(list(s_set)[i]):
                            return False
                    if s2_len == s3_len:
                        if s2.count(list(s_set)[j]) != s3.count(list(s_set)[j]):
                            return False
                    if s1_len == s3_len and s2_len == s3_len:
                        if s1.count(list(s_set)[i]) + s2.count(list(s_set)[j]) != s3.count(list(s_set)[k]):
                            return False
                    if s1_len < s3_len:
                        if s3.count(list(s_set)[k]) - s1.count(list(s_set)[i]) != s2.count(list(s_set)[j]):
                            return False
                    if s2_len < s3_len:
                        if s3.count(list(s_set)[k]) - s2.count(list(s_set)[j]) != s1.count(list(s_set)[i]):
                            return False
    return True

=======
Suggestion 4

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    if len(s1) > 10 or len(s2) > 10 or len(s3) > 10:
        print("UNSOLVABLE")
        return
    for i in range(10 ** (len(s1) - 1), 10 ** len(s1)):
        if len(set(str(i))) != len(set(s1)):
            continue
        for j in range(10 ** (len(s2) - 1), 10 ** len(s2)):
            if len(set(str(j))) != len(set(s2)):
                continue
            for k in range(10 ** (len(s3) - 1), 10 ** len(s3)):
                if len(set(str(k))) != len(set(s3)):
                    continue
                if i + j == k:
                    if isMatch(s1, str(i)) and isMatch(s2, str(j)) and isMatch(s3, str(k)):
                        print(i)
                        print(j)
                        print(k)
                        return
    print("UNSOLVABLE")
    return

=======
Suggestion 5

def main():
    s1 = list(input())
    s2 = list(input())
    s3 = list(input())
    chars = set(s1 + s2 + s3)
    if len(chars) > 10:
        print("UNSOLVABLE")
        return
    chars = list(chars)
    for p in permutations(range(10), len(chars)):
        d = {chars[i]: p[i] for i in range(len(chars))}
        if d[s1[0]] == 0 or d[s2[0]] == 0 or d[s3[0]] == 0:
            continue
        n1 = int("".join([str(d[c]) for c in s1]))
        n2 = int("".join([str(d[c]) for c in s2]))
        n3 = int("".join([str(d[c]) for c in s3]))
        if n1 + n2 == n3:
            print(n1)
            print(n2)
            print(n3)
            return
    print("UNSOLVABLE")

=======
Suggestion 6

def solve():
    S1 = input()
    S2 = input()
    S3 = input()

    chars = set(S1 + S2 + S3)
    if len(chars) > 10:
        print("UNSOLVABLE")
        return

    for perm in permutations(range(10), len(chars)):
        table = {ch: d for ch, d in zip(chars, perm)}
        if table[S1[0]] == 0 or table[S2[0]] == 0 or table[S3[0]] == 0:
            continue

        N1 = int("".join([str(table[ch]) for ch in S1]))
        N2 = int("".join([str(table[ch]) for ch in S2]))
        N3 = int("".join([str(table[ch]) for ch in S3]))
        if N1 + N2 == N3:
            print(N1)
            print(N2)
            print(N3)
            return

    print("UNSOLVABLE")

=======
Suggestion 7

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    chars = set(s1 + s2 + s3)
    if len(chars) > 10:
        print('UNSOLVABLE')
        return

    chars = list(chars)
    for perm in permutations(range(10), len(chars)):
        d = {}
        for c, p in zip(chars, perm):
            d[c] = str(p)
        if d[s1[0]] == '0' or d[s2[0]] == '0' or d[s3[0]] == '0':
            continue
        n1 = int(''.join(d[c] for c in s1))
        n2 = int(''.join(d[c] for c in s2))
        n3 = int(''.join(d[c] for c in s3))
        if n1 + n2 == n3:
            print(n1)
            print(n2)
            print(n3)
            return
    print('UNSOLVABLE')

=======
Suggestion 8

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    if len(s1) > 10 or len(s2) > 10 or len(s3) > 10:
        return
    if len(s3) > len(s1) + len(s2):
        return
    s1_set = set(s1)
    s2_set = set(s2)
    s3_set = set(s3)
    if len(s1_set) > 10 or len(s2_set) > 10 or len(s3_set) > 10:
        return
    if len(s1_set) + len(s2_set) > 10:
        return
    s_set = s1_set | s2_set | s3_set
    if len(s_set) > 10:
        return
    s_list = list(s_set)
    s_list.sort()
    s_map = {}
    for i in range(len(s_list)):
        s_map[s_list[i]] = i
    s1_num = 0
    s2_num = 0
    s3_num = 0
    for i in range(len(s1)):
        s1_num = s1_num * 10 + s_map[s1[i]]
    for i in range(len(s2)):
        s2_num = s2_num * 10 + s_map[s2[i]]
    for i in range(len(s3)):
        s3_num = s3_num * 10 + s_map[s3[i]]
    if s1_num + s2_num != s3_num:
        return
    if s1[0] == '0' or s2[0] == '0' or s3[0] == '0':
        return
    print(s1_num)
    print(s2_num)
    print(s3_num)
    return

=======
Suggestion 9

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    s1 = s1[::-1]
    s2 = s2[::-1]
    s3 = s3[::-1]
    s1_list = list(set(s1))
    s2_list = list(set(s2))
    s3_list = list(set(s3))
    if len(s1_list) > len(s3_list) or len(s2_list) > len(s3_list):
        print('UNSOLVABLE')
        return
    if len(s3_list) > 10:
        print('UNSOLVABLE')
        return
    for i in range(10**(len(s3_list)-1), 10**len(s3_list)):
        n1 = str(i)
        if len(n1) < len(s1_list):
            continue
        n1_list = list(n1)
        for j in range(len(s1_list)):
            if s1_list[j] in n1_list:
                n1_list.remove(s1_list[j])
            else:
                break
        else:
            n1 = int(n1)
            for k in range(10**(len(s3_list)-1), 10**len(s3_list)):
                n2 = str(k)
                if len(n2) < len(s2_list):
                    continue
                n2_list = list(n2)
                for l in range(len(s2_list)):
                    if s2_list[l] in n2_list:
                        n2_list.remove(s2_list[l])
                    else:
                        break
                else:
                    n2 = int(n2)
                    n3 = n1 + n2
                    if len(str(n3)) != len(s3_list):
                        continue
                    n3_list = list(str(n3))
                    for m in range(len(s3_list)):
                        if s3_list[m] in n3_list:
                            n3_list.remove(s3_list[m])
                        else:
                            break
                    else:
                        print(n1)
                        print(n2)
                        print(n3)
                        return
    else:
        print('UNSOLVABLE')
        return

=======
Suggestion 10

def solve(s1, s2, s3):
    # 1. 从s1,s2,s3中提取出所有的字符
    chars = set(s1 + s2 + s3)
    if len(chars) > 10:
        return 'UNSOLVABLE'
    chars = list(chars)
    # 2. 枚举所有可能的字符和数字的对应关系
    for perm in permutations(range(10), len(chars)):
        # 3. 利用这种对应关系，将s1,s2,s3转换为数字
        d = {c: p for c, p in zip(chars, perm)}
        if d[s1[0]] == 0 or d[s2[0]] == 0 or d[s3[0]] == 0:
            continue
        n1 = int(''.join(map(str, [d[c] for c in s1])))
        n2 = int(''.join(map(str, [d[c] for c in s2])))
        n3 = int(''.join(map(str, [d[c] for c in s3])))
        # 4. 判断是否满足等式
        if n1 + n2 == n3:
            return '\n'.join([str(n1), str(n2), str(n3)])
    return 'UNSOLVABLE'
