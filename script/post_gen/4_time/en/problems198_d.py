Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    chars = set(s1+s2+s3)
    if len(chars) > 10:
        print("UNSOLVABLE")
        return
    chars = list(chars)
    chars.sort()
    for perm in permutations(range(10), len(chars)):
        d = {chars[i]:perm[i] for i in range(len(chars))}
        if d[s1[0]] == 0 or d[s2[0]] == 0 or d[s3[0]] == 0:
            continue
        n1 = int(''.join([str(d[c]) for c in s1]))
        n2 = int(''.join([str(d[c]) for c in s2]))
        n3 = int(''.join([str(d[c]) for c in s3]))
        if n1+n2 == n3:
            print(n1)
            print(n2)
            print(n3)
            return
    print("UNSOLVABLE")

=======
Suggestion 2

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    chars = set(s1) | set(s2) | set(s3)
    if len(chars) > 10:
        print('UNSOLVABLE')
        return
    chars = list(chars)
    for perm in permutations(range(10), len(chars)):
        s1_ = s1
        s2_ = s2
        s3_ = s3
        for i in range(len(chars)):
            s1_ = s1_.replace(chars[i], str(perm[i]))
            s2_ = s2_.replace(chars[i], str(perm[i]))
            s3_ = s3_.replace(chars[i], str(perm[i]))
        if s1_[0] == '0' or s2_[0] == '0' or s3_[0] == '0':
            continue
        if int(s1_) + int(s2_) == int(s3_):
            print(s1_)
            print(s2_)
            print(s3_)
            return
    print('UNSOLVABLE')


from itertools import permutations

=======
Suggestion 3

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    s1 = s1[::-1]
    s2 = s2[::-1]
    s3 = s3[::-1]
    s1 = s1.replace('x', '0')
    s2 = s2.replace('x', '0')
    s3 = s3.replace('x', '0')
    s1 = s1.replace('y', '0')
    s2 = s2.replace('y', '0')
    s3 = s3.replace('y', '0')
    s1 = s1.replace('z', '0')
    s2 = s2.replace('z', '0')
    s3 = s3.replace('z', '0')
    if int(s1) + int(s2) == int(s3):
        print(s1[::-1])
        print(s2[::-1])
        print(s3[::-1])
    else:
        print('UNSOLVABLE')

=======
Suggestion 4

def main():
    from itertools import permutations
    s1 = input()
    s2 = input()
    s3 = input()
    chars = set(s1 + s2 + s3)
    if len(chars) > 10:
        print("UNSOLVABLE")
        return
    chars = list(chars)
    for p in permutations(range(10), len(chars)):
        d = {c: p[i] for i, c in enumerate(chars)}
        n1 = int("".join([str(d[c]) for c in s1]))
        n2 = int("".join([str(d[c]) for c in s2]))
        n3 = int("".join([str(d[c]) for c in s3]))
        if n1 + n2 == n3:
            print(n1)
            print(n2)
            print(n3)
            return
    print("UNSOLVABLE")

main()

=======
Suggestion 5

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    if len(s1) > len(s2):
        if len(s1) > len(s3):
            max_len = len(s1)
        else:
            max_len = len(s3)
    else:
        if len(s2) > len(s3):
            max_len = len(s2)
        else:
            max_len = len(s3)
    for i in range(10 ** (max_len - 1), 10 ** max_len):
        n1 = str(i)
        n2 = str(i)
        n3 = str(i)
        for j in range(len(n1), max_len):
            n1 = "0" + n1
        for j in range(len(n2), max_len):
            n2 = "0" + n2
        for j in range(len(n3), max_len):
            n3 = "0" + n3
        for j in range(max_len):
            if s1[j] == s2[j] and s1[j] != s3[j]:
                break
            if s1[j] == s3[j] and s1[j] != s2[j]:
                break
            if s2[j] == s3[j] and s1[j] != s2[j]:
                break
            if s1[j] == s2[j] and s1[j] == s3[j]:
                if n1[j] != n2[j]:
                    break
                elif n1[j] != n3[j]:
                    break
                elif n2[j] != n3[j]:
                    break
            if s1[j] != s2[j] and s1[j] != s3[j] and s2[j] != s3[j]:
                if n1[j] == n2[j] or n1[j] == n3[j] or n2[j] == n3[j]:
                    break
        else:
            if int(n1) + int(n2) == int(n3):
                print(n1)
                print(n2)
                print(n3)
                exit()
    print("UNSOLVABLE")

=======
Suggestion 6

def solve(s1, s2, s3):
    chars = set(s1 + s2 + s3)
    if len(chars) > 10:
        return 'UNSOLVABLE'

    chars = list(chars)
    for perm in permutations(range(10), len(chars)):
        table = {c: str(perm[i]) for i, c in enumerate(chars)}
        if table[s1[0]] == '0' or table[s2[0]] == '0' or table[s3[0]] == '0':
            continue

        n1 = int(''.join([table[c] for c in s1]))
        n2 = int(''.join([table[c] for c in s2]))
        n3 = int(''.join([table[c] for c in s3]))
        if n1 + n2 == n3:
            return '\n'.join([str(n1), str(n2), str(n3)])

    return 'UNSOLVABLE'

=======
Suggestion 7

def solve(s1, s2, s3):
    s1 = s1[::-1]
    s2 = s2[::-1]
    s3 = s3[::-1]
    d = {}
    for s in s1 + s2 + s3:
        d[s] = -1
    if len(d) > 10:
        return 'UNSOLVABLE'
    for i in range(10):
        if i in d.values():
            continue
        d[s1[0]] = i
        for j in range(10):
            if j in d.values():
                continue
            d[s2[0]] = j
            for k in range(10):
                if k in d.values():
                    continue
                d[s3[0]] = k
                if d[s1[0]] + d[s2[0]] == d[s3[0]]:
                    if len(s1) == 1 and len(s2) == 1 and len(s3) == 1:
                        return '%d\n%d\n%d' % (d[s1[0]], d[s2[0]], d[s3[0]])
                    elif len(s1) == 1 or len(s2) == 1 or len(s3) == 1:
                        continue
                    else:
                        n1 = 0
                        n2 = 0
                        n3 = 0
                        for s in s1:
                            n1 = n1 * 10 + d[s]
                        for s in s2:
                            n2 = n2 * 10 + d[s]
                        for s in s3:
                            n3 = n3 * 10 + d[s]
                        if n1 + n2 == n3:
                            return '%d\n%d\n%d' % (n1, n2, n3)
                d[s3[0]] = -1
            d[s2[0]] = -1
        d[s1[0]] = -1
    return 'UNSOLVABLE'

s1 = input()
s2 = input()
s3 = input()
print(solve(s1, s2, s3))

=======
Suggestion 8

def solve(s1, s2, s3):
    chars = list(set(s1 + s2 + s3))
    if len(chars) > 10:
        return None
    chars.sort()
    for p in permutations(range(10), len(chars)):
        if p[0] == 0:
            continue
        d = dict(zip(chars, p))
        n1 = int(''.join(map(str, [d[c] for c in s1])))
        n2 = int(''.join(map(str, [d[c] for c in s2])))
        n3 = int(''.join(map(str, [d[c] for c in s3])))
        if n1 + n2 == n3:
            return n1, n2, n3
    return None

from itertools import permutations
s1 = input()
s2 = input()
s3 = input()
ans = solve(s1, s2, s3)

=======
Suggestion 9

def get_int(s, d):
    num = 0
    for c in s:
        num = num * 10 + d[c]
    return num

=======
Suggestion 10

def getNum(s, chars):
    num = 0
    for c in s:
        num = num * 10 + chars[c]
    return num
