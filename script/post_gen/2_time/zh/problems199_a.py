Synthesizing 10/10 solutions

=======
Suggestion 1

def getint(str):
    x = 0
    for i in range(len(str)):
        x += (ord(str[i]) - ord('a') + 1) * (10 ** (len(str) - i - 1))
    return x

S1 = input()
S2 = input()
S3 = input()

S1_int = getint(S1)
S2_int = getint(S2)
S3_int = getint(S3)

for i in range(10 ** (len(S1) - 1), 10 ** len(S1)):
    for j in range(10 ** (len(S2) - 1), 10 ** len(S2)):
        for k in range(10 ** (len(S3) - 1), 10 ** len(S3)):
            if i + j == k:
                if getint(S1) == i and getint(S2) == j and getint(S3) == k:
                    print(i)
                    print(j)
                    print(k)
                    exit()
print("UNSOLVABLE")

=======
Suggestion 2

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    if len(s1) > 10 or len(s2) > 10 or len(s3) > 10:
        print("UNSOLVABLE")
        return
    s = set()
    for c in s1:
        s.add(c)
    for c in s2:
        s.add(c)
    for c in s3:
        s.add(c)
    if len(s) > 10:
        print("UNSOLVABLE")
        return
    l = list(s)
    l.sort()
    if len(l) == 1:
        print(0)
        print(0)
        print(0)
        return
    n = len(l)
    for i in range(0, 10):
        for j in range(0, 10):
            for k in range(0, 10):
                if i == j or i == k or j == k:
                    continue
                d = {}
                for m in range(0, n):
                    d[l[m]] = -1
                d[s1[0]] = i
                d[s2[0]] = j
                d[s3[0]] = k
                if d[s1[0]] == 0 and len(s1) > 1:
                    continue
                if d[s2[0]] == 0 and len(s2) > 1:
                    continue
                if d[s3[0]] == 0 and len(s3) > 1:
                    continue
                if d[s1[0]] == -1 or d[s2[0]] == -1 or d[s3[0]] == -1:
                    continue
                n1 = 0
                n2 = 0
                n3 = 0
                for m in range(0, len(s1)):
                    n1 = n1 * 10 + d[s1[m]]
                for m in range(0, len(s2)):
                    n2 = n2 * 10 + d[s2[m]]
                for m in range(0, len(s3)):
                    n3 = n3 * 10 + d[s3[m]]
                if n1 + n2 == n3:
                    print(n1)
                    print(n2)
                    print(n3)
                    return

=======
Suggestion 3

def solve(s1, s2, s3):
    if len(s1) > len(s2):
        s1, s2 = s2, s1
    if len(s2) > len(s3):
        s2, s3 = s3, s2
    if len(s1) > len(s2):
        s1, s2 = s2, s1
    if len(s1) + len(s2) != len(s3):
        return False
    s1 = s1[::-1]
    s2 = s2[::-1]
    s3 = s3[::-1]
    for i in range(10 ** (len(s1) - 1), 10 ** len(s1)):
        for j in range(10 ** (len(s2) - 1), 10 ** len(s2)):
            if i + j == int(s3):
                if check(s1, i) and check(s2, j) and check(s3, i + j):
                    return [i, j, i + j]
    return False

=======
Suggestion 4

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    if len(s1) > len(s2):
        s1, s2 = s2, s1
    if len(s2) > len(s3):
        s2, s3 = s3, s2
    if len(s1) > len(s2):
        s1, s2 = s2, s1
    if len(s1) + len(s2) != len(s3):
        print("UNSOLVABLE")
        return
    s1 = s1[::-1]
    s2 = s2[::-1]
    s3 = s3[::-1]
    for i in range(10 ** (len(s1) - 1), 10 ** len(s1)):
        n1 = str(i)
        if len(n1) != len(s1):
            continue
        for j in range(10 ** (len(s2) - 1), 10 ** len(s2)):
            n2 = str(j)
            if len(n2) != len(s2):
                continue
            n3 = str(i + j)
            if len(n3) != len(s3):
                continue
            d = {}
            for k in range(len(s1)):
                if s1[k] not in d:
                    d[s1[k]] = n1[k]
                elif d[s1[k]] != n1[k]:
                    break
            else:
                for k in range(len(s2)):
                    if s2[k] not in d:
                        d[s2[k]] = n2[k]
                    elif d[s2[k]] != n2[k]:
                        break
                else:
                    for k in range(len(s3)):
                        if s3[k] not in d:
                            d[s3[k]] = n3[k]
                        elif d[s3[k]] != n3[k]:
                            break
                    else:
                        print(i)
                        print(j)
                        print(i + j)
                        return
    print("UNSOLVABLE")

=======
Suggestion 5

def solve():
    s1 = input()
    s2 = input()
    s3 = input()
    #s1 = "send"
    #s2 = "more"
    #s3 = "money"
    #s1 = "abcd"
    #s2 = "efgh"
    #s3 = "ijkl"
    #s1 = "p"
    #s2 = "q"
    #s3 = "p"
    #s1 = "x"
    #s2 = "x"
    #s3 = "y"
    #s1 = "a"
    #s2 = "b"
    #s3 = "c"
    #s1 = "a"
    #s2 = "a"
    #s3 = "b"
    #s1 = "a"
    #s2 = "a"
    #s3 = "a"
    #s1 = "a"
    #s2 = "b"
    #s3 = "a"
    #s1 = "a"
    #s2 = "b"
    #s3 = "b"
    #s1 = "a"
    #s2 = "b"
    #s3 = "c"
    #s1 = "a"
    #s2 = "a"
    #s3 = "c"
    #s1 = "a"
    #s2 = "c"
    #s3 = "b"
    #s1 = "a"
    #s2 = "c"
    #s3 = "c"
    #s1 = "a"
    #s2 = "c"
    #s3 = "a"
    #s1 = "a"
    #s2 = "c"
    #s3 = "c"
    #s1 = "a"
    #s2 = "c"
    #s3 = "b"
    #s1 = "a"
    #s2 = "c"
    #s3 = "a"
    #s1 = "a"
    #s2 = "c"
    #s3 = "c"
    #s1 = "a"
    #s2 = "c"
    #s3 = "b"
    #s1 = "a"
    #s2 = "c"
    #s3 = "a

=======
Suggestion 6

def main():
    s1 = input()
    s2 = input()
    s3 = input()

    s1 = s1[::-1]
    s2 = s2[::-1]
    s3 = s3[::-1]

    n = max(len(s1), len(s2), len(s3))

    s1 += '0' * (n - len(s1))
    s2 += '0' * (n - len(s2))
    s3 += '0' * (n - len(s3))

    used = set()
    for i in range(10):
        used.add(str(i))

    def check(n1, n2, n3):
        if len(n1) != len(s1) or len(n2) != len(s2) or len(n3) != len(s3):
            return False
        if n1[0] == '0' or n2[0] == '0' or n3[0] == '0':
            return False

        d = {}
        for i in range(n):
            if n1[i] in d:
                if d[n1[i]] != s1[i]:
                    return False
            else:
                d[n1[i]] = s1[i]
                used.discard(s1[i])

            if n2[i] in d:
                if d[n2[i]] != s2[i]:
                    return False
            else:
                d[n2[i]] = s2[i]
                used.discard(s2[i])

            if n3[i] in d:
                if d[n3[i]] != s3[i]:
                    return False
            else:
                d[n3[i]] = s3[i]
                used.discard(s3[i])

        return True

    def dfs(n1, n2, n3, i):
        if i == n:
            if check(n1, n2, n3):
                print(n1[::-1])
                print(n2[::-1])
                print(n3[::-1])
                exit()
            return

        if s1[i] in d:
            if s2[i] in d:
                if d[s1[i]] == d[s2[i]]:
                    dfs(n1, n2, n3, i + 1)
                else:
                    return
            else:
                if s3[i] in d:
                    if d[s1[i]] == d[s3

=======
Suggestion 7

def main():
    S1 = input()
    S2 = input()
    S3 = input()
    S1 = list(S1)
    S2 = list(S2)
    S3 = list(S3)
    S = list(set(S1+S2+S3))
    if len(S) > 10:
        print("UNSOLVABLE")
        return
    for i in range(0,10):
        for j in range(0,10):
            for k in range(0,10):
                N1 = []
                N2 = []
                N3 = []
                for s in S1:
                    if s == S[0]:
                        N1.append(str(i))
                    elif s == S[1]:
                        N1.append(str(j))
                    elif s == S[2]:
                        N1.append(str(k))
                for s in S2:
                    if s == S[0]:
                        N2.append(str(i))
                    elif s == S[1]:
                        N2.append(str(j))
                    elif s == S[2]:
                        N2.append(str(k))
                for s in S3:
                    if s == S[0]:
                        N3.append(str(i))
                    elif s == S[1]:
                        N3.append(str(j))
                    elif s == S[2]:
                        N3.append(str(k))
                if len(N1) == len(S1) and len(N2) == len(S2) and len(N3) == len(S3):
                    if int(''.join(N1)) + int(''.join(N2)) == int(''.join(N3)):
                        print(''.join(N1))
                        print(''.join(N2))
                        print(''.join(N3))
                        return
    print("UNSOLVABLE")
    return

=======
Suggestion 8

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    if len(s1) > len(s2):
        s1, s2 = s2, s1
    if len(s2) > len(s3):
        s2, s3 = s3, s2
    if len(s1) > len(s2):
        s1, s2 = s2, s1
    if len(s1) + len(s2) != len(s3):
        print("UNSOLVABLE")
        return
    s1 = s1[::-1]
    s2 = s2[::-1]
    s3 = s3[::-1]
    for i in range(10 ** len(s1)):
        for j in range(10 ** len(s2)):
            if i + j == int(s3):
                n1 = str(i)
                n2 = str(j)
                while len(n1) < len(s1):
                    n1 = "0" + n1
                while len(n2) < len(s2):
                    n2 = "0" + n2
                for k in range(len(s1)):
                    if s1[k] == "?":
                        continue
                    if s1[k] != n1[k]:
                        break
                else:
                    for k in range(len(s2)):
                        if s2[k] == "?":
                            continue
                        if s2[k] != n2[k]:
                            break
                    else:
                        print(i)
                        print(j)
                        print(i + j)
                        return
    print("UNSOLVABLE")

=======
Suggestion 9

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    if len(s3) < len(s1) or len(s3) < len(s2):
        print("UNSOLVABLE")
        return
    s1 = list(s1)
    s2 = list(s2)
    s3 = list(s3)
    s1.reverse()
    s2.reverse()
    s3.reverse()
    # print(s1, s2, s3)
    s1 = list(map(ord, s1))
    s2 = list(map(ord, s2))
    s3 = list(map(ord, s3))
    # print(s1, s2, s3)
    for i in range(0, 26):
        s1 = list(map(lambda x: x-ord('a'), s1))
        s2 = list(map(lambda x: x-ord('a'), s2))
        s3 = list(map(lambda x: x-ord('a'), s3))
        # print(s1, s2, s3)
        for j in range(0, 26):
            s1 = list(map(lambda x: (x+1)%26, s1))
            s2 = list(map(lambda x: (x+1)%26, s2))
            s3 = list(map(lambda x: (x+1)%26, s3))
            # print(s1, s2, s3)
            if s1[-1] + s2[-1] == s3[-1]:
                s1 = list(map(lambda x: x+ord('a'), s1))
                s2 = list(map(lambda x: x+ord('a'), s2))
                s3 = list(map(lambda x: x+ord('a'), s3))
                s1.reverse()
                s2.reverse()
                s3.reverse()
                for i in range(0, len(s1)):
                    print(s1[i], end="")
                print()
                for i in range(0, len(s2)):
                    print(s2[i], end="")
                print()
                for i in range(0, len(s3)):
                    print(s3[i], end="")
                print()
                return
        s1 = list(map(lambda x: x+ord('a'), s1))
        s2 = list(map(lambda x: x+ord('a'), s2

=======
Suggestion 10

def solve():
    s1 = input()
    s2 = input()
    s3 = input()
    s = set(s1+s2+s3)
    if len(s) > 10:
        print('UNSOLVABLE')
        return
    s = list(s)
    for i in range(10-len(s)):
        s.append('')
    s.sort()
    for p in permutations(range(10), len(s)):
        d = {c: p[i] for i, c in enumerate(s)}
        if d[s1[0]] == 0 or d[s2[0]] == 0 or d[s3[0]] == 0:
            continue
        n1 = int(''.join([str(d[c]) for c in s1]))
        n2 = int(''.join([str(d[c]) for c in s2]))
        n3 = int(''.join([str(d[c]) for c in s3]))
        if n1 + n2 == n3:
            print(n1)
            print(n2)
            print(n3)
            return
    print('UNSOLVABLE')
