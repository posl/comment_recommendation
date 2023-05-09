Synthesizing 9/10 solutions

=======
Suggestion 1

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
        d = dict(zip(chars, perm))
        if d[s1[0]] == 0 or d[s2[0]] == 0 or d[s3[0]] == 0:
            continue
        n1 = int(''.join(str(d[c]) for c in s1))
        n2 = int(''.join(str(d[c]) for c in s2))
        n3 = int(''.join(str(d[c]) for c in s3))
        if n1 + n2 == n3:
            print(n1)
            print(n2)
            print(n3)
            return
    print('UNSOLVABLE')

main()

=======
Suggestion 2

def solve():
    s1 = input()
    s2 = input()
    s3 = input()
    chars = set(s1+s2+s3)
    if len(chars) > 10:
        print("UNSOLVABLE")
        return

    chars = list(chars)
    for p in permutations(range(10), len(chars)):
        d = {}
        for i in range(len(chars)):
            d[chars[i]] = p[i]
        if d[s1[0]] == 0 or d[s2[0]] == 0 or d[s3[0]] == 0:
            continue
        n1 = 0
        n2 = 0
        n3 = 0
        for i in range(len(s1)):
            n1 *= 10
            n1 += d[s1[i]]
        for i in range(len(s2)):
            n2 *= 10
            n2 += d[s2[i]]
        for i in range(len(s3)):
            n3 *= 10
            n3 += d[s3[i]]
        if n1 + n2 == n3:
            print(n1)
            print(n2)
            print(n3)
            return
    print("UNSOLVABLE")
    return


from itertools import permutations
solve()

=======
Suggestion 3

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    s1 = list(s1)
    s2 = list(s2)
    s3 = list(s3)
    s1.reverse()
    s2.reverse()
    s3.reverse()
    s1_dict = {}
    s2_dict = {}
    s3_dict = {}
    for i in s1:
        s1_dict[i] = 0
    for i in s2:
        s2_dict[i] = 0
    for i in s3:
        s3_dict[i] = 0
    if len(s1_dict) > 10 or len(s2_dict) > 10 or len(s3_dict) > 10:
        print('UNSOLVABLE')
        return
    for i in range(10):
        if i in s1_dict.values():
            continue
        for j in range(10):
            if j in s2_dict.values():
                continue
            for k in range(10):
                if k in s3_dict.values():
                    continue
                if i == 0 and (s1[0] in s1_dict.keys() or s2[0] in s2_dict.keys() or s3[0] in s3_dict.keys()):
                    continue
                s1_dict[s1[0]] = i
                s2_dict[s2[0]] = j
                s3_dict[s3[0]] = k
                s1_num = 0
                s2_num = 0
                s3_num = 0
                for l in range(len(s1)):
                    s1_num += s1_dict[s1[l]] * (10 ** l)
                for l in range(len(s2)):
                    s2_num += s2_dict[s2[l]] * (10 ** l)
                for l in range(len(s3)):
                    s3_num += s3_dict[s3[l]] * (10 ** l)
                if s1_num + s2_num == s3_num:
                    print(s1_num)
                    print(s2_num)
                    print(s3_num)
                    return
                s1_dict[s1[0]] = 0
                s2_dict[s2[0]] = 0
                s3_dict[s3[0]] = 0
    print('UNSOLVABLE')

=======
Suggestion 4

def solve():
    from itertools import permutations
    s1 = input()
    s2 = input()
    s3 = input()
    chars = set(s1+s2+s3)
    if len(chars) > 10:
        print('UNSOLVABLE')
        return
    for perm in permutations(range(10), len(chars)):
        if perm[0] == 0:
            continue
        d = {c: n for c, n in zip(chars, perm)}
        if d[s1[0]] + d[s2[0]] > 9 or d[s3[0]] + d[s3[1]] > 9:
            continue
        n1 = int(''.join(str(d[c]) for c in s1))
        n2 = int(''.join(str(d[c]) for c in s2))
        n3 = int(''.join(str(d[c]) for c in s3))
        if n1 + n2 == n3:
            print(n1)
            print(n2)
            print(n3)
            return
    print('UNSOLVABLE')

=======
Suggestion 5

def solve(S1, S2, S3):
    for i in range(10):
        for j in range(10):
            for k in range(10):
                S1 = S1.replace('A', str(i))
                S1 = S1.replace('B', str(j))
                S1 = S1.replace('C', str(k))
                S2 = S2.replace('A', str(i))
                S2 = S2.replace('B', str(j))
                S2 = S2.replace('C', str(k))
                S3 = S3.replace('A', str(i))
                S3 = S3.replace('B', str(j))
                S3 = S3.replace('C', str(k))
                if int(S1)+int(S2) == int(S3):
                    return i,j,k
    return -1,-1,-1

S1 = input()
S2 = input()
S3 = input()
a,b,c = solve(S1, S2, S3)

=======
Suggestion 6

def get_number(s, d):
    ret = 0
    for c in s:
        ret = ret * 10 + d[c]
    return ret

=======
Suggestion 7

def is_valid(S1, S2, S3, N1, N2, N3):
    # print("is_valid", S1, S2, S3, N1, N2, N3)
    if len(S1) != len(N1) or len(S2) != len(N2) or len(S3) != len(N3):
        return False
    if N1[0] == '0' or N2[0] == '0' or N3[0] == '0':
        return False
    for i in range(len(S1)):
        if S1[i] == S2[i] and N1[i] != N2[i]:
            return False
        if S1[i] == S3[i] and N1[i] != N3[i]:
            return False
        if S2[i] == S3[i] and N2[i] != N3[i]:
            return False
    return True

=======
Suggestion 8

def get_number(s, c, n):
    x = 0
    for i in range(len(s)):
        if s[i] == c:
            x += (10 ** (len(s) - i - 1)) * n
    return x

s1 = input()
s2 = input()
s3 = input()

s = set(s1 + s2 + s3)

=======
Suggestion 9

def convert(s, d):
    t = ''
    for c in s:
        t += str(d[c])
    return t
