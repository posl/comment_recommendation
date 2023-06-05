Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S1 = input()
    S2 = input()
    S3 = input()
    S = set(S1 + S2 + S3)
    if len(S) > 10:
        print("UNSOLVABLE")
        return
    for S in permutations(S):
        if S[0] == '0' or S[3] == '0' or S[6] == '0':
            continue
        D = dict(zip(S, range(10)))
        N1 = sum(D[c] * 10 ** i for i, c in enumerate(S1[::-1]))
        N2 = sum(D[c] * 10 ** i for i, c in enumerate(S2[::-1]))
        N3 = sum(D[c] * 10 ** i for i, c in enumerate(S3[::-1]))
        if N1 + N2 == N3:
            print(N1)
            print(N2)
            print(N3)
            return
    print("UNSOLVABLE")

=======
Suggestion 2

def solve():
    s1 = input()
    s2 = input()
    s3 = input()
    s = set(s1 + s2 + s3)
    if len(s) > 10:
        print("UNSOLVABLE")
        return
    s = list(s)
    n = len(s)
    if n > 10:
        print("UNSOLVABLE")
        return
    for i in range(10 ** n):
        t = str(i).zfill(n)
        if len(set(t)) != n:
            continue
        d = {}
        for j in range(n):
            d[s[j]] = t[j]
        if d[s1[0]] == '0' or d[s2[0]] == '0' or d[s3[0]] == '0':
            continue
        n1 = int("".join([d[c] for c in s1]))
        n2 = int("".join([d[c] for c in s2]))
        n3 = int("".join([d[c] for c in s3]))
        if n1 + n2 == n3:
            print(n1)
            print(n2)
            print(n3)
            return
    print("UNSOLVABLE")


solve()

=======
Suggestion 3

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    s = set(s1+s2+s3)
    if len(s) > 10:
        print('UNSOLVABLE')
        exit()
    s = list(s)
    if len(s) < 10:
        for i in range(10-len(s)):
            s.append('0')
    for i in range(10):
        s[i] = ord(s[i])-ord('a')
    for i in range(1000,10000):
        if len(set(str(i))) != 4:
            continue
        n1 = i
        n2 = i*2
        n3 = i*3
        if len(str(n2)) != len(str(n1)):
            continue
        if len(str(n3)) != len(str(n1)):
            continue
        for j in range(4):
            if s1[j] == chr(n1//(10**(3-j))%10 + ord('a')):
                continue
            else:
                break
        else:
            for j in range(4):
                if s2[j] == chr(n2//(10**(3-j))%10 + ord('a')):
                    continue
                else:
                    break
            else:
                for j in range(4):
                    if s3[j] == chr(n3//(10**(3-j))%10 + ord('a')):
                        continue
                    else:
                        break
                else:
                    print(n1)
                    print(n2)
                    print(n3)
                    exit()
    print('UNSOLVABLE')
    exit()

=======
Suggestion 4

def judge():
    s1 = input()
    s2 = input()
    s3 = input()
    if len(s1) > len(s2):
        s1, s2 = s2, s1
    if len(s1) > len(s3):
        s1, s3 = s3, s1
    if len(s2) > len(s3):
        s2, s3 = s3, s2
    if len(s3) > 10:
        return False
    if len(s1) + len(s2) != len(s3):
        return False
    s = set()
    for i in range(len(s1)):
        s.add(s1[i])
        s.add(s2[i])
        s.add(s3[i])
    if len(s) > 10:
        return False
    s = list(s)
    for i in range(10):
        for j in range(10):
            for k in range(10):
                if i == 0 and (j == 0 or k == 0):
                    continue
                dic = {}
                for l in range(len(s)):
                    dic[s[l]] = [i, j, k][l]
                n1 = n2 = n3 = 0
                for l in range(len(s1)):
                    n1 = n1 * 10 + dic[s1[l]]
                    n2 = n2 * 10 + dic[s2[l]]
                    n3 = n3 * 10 + dic[s3[l]]
                if n1 + n2 == n3:
                    print(n1)
                    print(n2)
                    print(n3)
                    return True
    return False

=======
Suggestion 5

def solve(S1, S2, S3):
    for i in range(10):
        for j in range(10):
            for k in range(10):
                N1 = S1.replace('a', str(i)).replace('b', str(j)).replace('c', str(k))
                N2 = S2.replace('a', str(i)).replace('b', str(j)).replace('c', str(k))
                N3 = S3.replace('a', str(i)).replace('b', str(j)).replace('c', str(k))
                if N1[0] == '0' or N2[0] == '0' or N3[0] == '0':
                    continue
                if int(N1) + int(N2) == int(N3):
                    return N1, N2, N3
    return None, None, None

=======
Suggestion 6

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    if len(s1) > len(s3) or len(s2) > len(s3):
        print("UNSOLVABLE")
        return
    li = list(set(s1 + s2 + s3))
    if len(li) > 10:
        print("UNSOLVABLE")
        return
    for i in range(10 ** len(s1) - 1, 10 ** (len(s1) - 1) - 1, -1):
        for j in range(10 ** len(s2) - 1, 10 ** (len(s2) - 1) - 1, -1):
            if i + j > 10 ** len(s3):
                continue
            s = str(i) + str(j) + str(i + j)
            if len(s) > 10:
                break
            if len(s) < 10:
                s = "0" * (10 - len(s)) + s
            d = {}
            for k in range(len(li)):
                d[li[k]] = s[k]
            if len(set(d.values())) == len(d.values()):
                for k in range(3):
                    for l in range(len(s1)):
                        s1 = s1[:l] + d[s1[l]] + s1[l + 1:]
                    for l in range(len(s2)):
                        s2 = s2[:l] + d[s2[l]] + s2[l + 1:]
                    for l in range(len(s3)):
                        s3 = s3[:l] + d[s3[l]] + s3[l + 1:]
                print(i)
                print(j)
                print(i + j)
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
        print("UNSOLVABLE")
        return
    chars = list(chars)
    from itertools import permutations
    for perm in permutations(range(10), len(chars)):
        d = dict(zip(chars, perm))
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
Suggestion 8

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    if len(s1) > len(s2):
        s1, s2 = s2, s1
    if len(s1) > len(s3):
        s1, s3 = s3, s1
    if len(s2) > len(s3):
        s2, s3 = s3, s2
    # print(s1, s2, s3)
    if len(s3) > 10:
        print("UNSOLVABLE")
        return
    s1 = s1[::-1]
    s2 = s2[::-1]
    s3 = s3[::-1]
    # print(s1, s2, s3)
    d = {}
    for i in s1:
        d[i] = -1
    for i in s2:
        d[i] = -1
    for i in s3:
        d[i] = -1
    # print(d)
    if len(d) > 10:
        print("UNSOLVABLE")
        return
    if len(d) == 10:
        for i in range(10):
            d[chr(ord('0')+i)] = i
        if d[s1[0]] == 0 or d[s2[0]] == 0 or d[s3[0]] == 0:
            print("UNSOLVABLE")
            return
        n1 = 0
        n2 = 0
        n3 = 0
        for i in range(len(s1)):
            n1 = n1*10 + d[s1[i]]
        for i in range(len(s2)):
            n2 = n2*10 + d[s2[i]]
        for i in range(len(s3)):
            n3 = n3*10 + d[s3[i]]
        if n1 + n2 == n3:
            print(n1)
            print(n2)
            print(n3)
        else:
            print("UNSOLVABLE")
        return
    else:
        for i in range(10):
            d[chr(ord('0')+i)] = i
        if d[s1[0]] == 0 or d[s2[0]] == 0 or d[s3[0]] == 0:
            print("

=======
Suggestion 9

def get_num(s):
    num = 0
    for i in s:
        num = num * 10 + ord(i) - ord('a')
    return num

=======
Suggestion 10

def solve():
    s1 = input()
    s2 = input()
    s3 = input()
    if len(s1) > len(s2):
        s1, s2 = s2, s1
    if len(s2) > len(s3):
        s2, s3 = s3, s2
    if len(s1) > len(s2):
        s1, s2 = s2, s1
    if len(s1) == len(s2) == len(s3) == 1:
        if s3 == chr(ord(s1) + ord(s2) - ord('a')):
            print(1)
            print(1)
            print(2)
        else:
            print("UNSOLVABLE")
        return
    if len(s1) == len(s2) == 1:
        if s1 == s2 and s2 != s3:
            print("UNSOLVABLE")
            return
        if s3 == chr(ord(s1) + ord(s2) - ord('a')):
            print(1)
            print(1)
            print(2)
        else:
            print("UNSOLVABLE")
        return
    if len(s1) == 1 and len(s2) == 2:
        if s3[0] == chr(ord(s1) + ord(s2[0]) - ord('a')):
            print(1)
            print(1)
            print(2)
        else:
            print("UNSOLVABLE")
        return
    if len(s1) == 1 and len(s2) == 3:
        if s3[0] == chr(ord(s1) + ord(s2[0]) - ord('a')):
            print(1)
            print(1)
            print(2)
        else:
            print("UNSOLVABLE")
        return
    if len(s1) == 2 and len(s2) == 2:
        if s1[0] == s2[0] and s3[0] != s3[1]:
            print("UNSOLVABLE")
            return
        if s1[0] == s2[0] and s3[0] == s3[1]:
            print(1)
            print(1)
            print(2)
            return
        if s1[0] == s
