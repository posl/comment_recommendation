Synthesizing 8/10 solutions

=======
Suggestion 1

def solve(s1, s2, s3):
    if len(s1) < len(s3):
        s1, s3 = s3, s1
    if len(s2) < len(s3):
        s2, s3 = s3, s2
    if len(s1) < len(s2):
        s1, s2 = s2, s1
    if len(s1) < len(s3):
        s1, s3 = s3, s1
    if len(s2) < len(s3):
        s2, s3 = s3, s2

    s = set(s1+s2+s3)
    if len(s) > 10:
        return 'UNSOLVABLE'

    l = len(s1)
    for i in range(10**l):
        d = {}
        for j, c in enumerate(s1):
            d[c] = i // 10**(l-1-j) % 10
        if d[s1[0]] == 0 or d[s2[0]] == 0 or d[s3[0]] == 0:
            continue

        a = 0
        for c in s1:
            a = 10*a + d[c]
        b = 0
        for c in s2:
            b = 10*b + d[c]
        c = 0
        for c in s3:
            c = 10*c + d[c]
        if a + b == c:
            return f'{a}

{b}

{c}'

    return 'UNSOLVABLE'

=======
Suggestion 2

def alphametic(s1, s2, s3):
    if len(s1) < len(s3):
        s1, s3 = s3, s1
    if len(s2) < len(s3):
        s2, s3 = s3, s2
    if len(s1) < len(s2):
        s1, s2 = s2, s1
    if len(s1) < len(s3):
        s1, s3 = s3, s1
    if len(s2) < len(s3):
        s2, s3 = s3, s2
    if len(s1) < len(s2):
        s1, s2 = s2, s1
    if len(s1) == len(s2) == len(s3):
        if len(s1) == 1:
            if s1 == s2 == s3:
                return '0', '0', '0'
            elif s1 == s2:
                return '1', '1', '2'
            elif s1 == s3:
                return '1', '2', '3'
            elif s2 == s3:
                return '2', '3', '5'
            else:
                return 'UNSOLVABLE'
        else:
            if s1[-1] == s2[-1] == s3[-1]:
                if s1[-1] == '0':
                    return 'UNSOLVABLE'
                else:
                    n1, n2, n3 = alphametic(s1[:-1], s2[:-1], s3[:-1])
                    if n1 == 'UNSOLVABLE':
                        return 'UNSOLVABLE'
                    else:
                        return n1 + '1', n2 + '1', n3 + '2'
            elif s1[-1] == s2[-1]:
                if s1[-1] == '0':
                    return 'UNSOLVABLE'
                else:
                    n1, n2, n3 = alphametic(s1[:-1], s2[:-1], s3[:-1])
                    if n1 == 'UNSOLVABLE':
                        return 'UNSOLVABLE'
                    else:
                        return n1 + '1', n2 + '1', n3 + '1'
            elif s1[-1] == s

=======
Suggestion 3

def solve():
    S1 = input()
    S2 = input()
    S3 = input()
    N = len(S1)
    if N != len(S2) or N != len(S3):
        print("UNSOLVABLE")
        return
    if N == 1:
        if S1 == S2 and S2 == S3:
            print("0")
            print("0")
            print("0")
        else:
            print("UNSOLVABLE")
        return
    if N == 2:
        if S1[0] == S2[0] and S2[0] == S3[0]:
            print("0", end="")
        elif S1[0] == S2[0]:
            print("0", end="")
        elif S1[0] == S3[0]:
            print("0", end="")
        elif S2[0] == S3[0]:
            print("0", end="")
        else:
            print("1", end="")
        if S1[1] == S2[1] and S2[1] == S3[1]:
            print("0", end="")
        elif S1[1] == S2[1]:
            print("0", end="")
        elif S1[1] == S3[1]:
            print("0", end="")
        elif S2[1] == S3[1]:
            print("0", end="")
        else:
            print("1", end="")
        print()
        if S1[0] == S2[0] and S2[0] == S3[0]:
            print("0", end="")
        elif S1[0] == S2[0]:
            print("0", end="")
        elif S1[0] == S3[0]:
            print("0", end="")
        elif S2[0] == S3[0]:
            print("0", end="")
        else:
            print("1", end="")
        if S1[1] == S2[1] and S2[1] == S3[1]:
            print("0", end="")
        elif S1[1] == S2[1]:
            print("0", end="")
        elif S1[1] == S3[1]:
            print("0", end="")
        elif S2[1] == S

=======
Suggestion 4

def main():
    S1 = input()
    S2 = input()
    S3 = input()
    S = S1 + S2 + S3
    S = list(set(S))
    if len(S) > 10:
        print("UNSOLVABLE")
        return
    for i in range(10**len(S)):
        N = str(i).zfill(len(S))
        N = dict(zip(S, N))
        N1 = int("".join(N[s] for s in S1))
        N2 = int("".join(N[s] for s in S2))
        N3 = int("".join(N[s] for s in S3))
        if N1 + N2 == N3 and N[S1[0]] != "0" and N[S2[0]] != "0" and N[S3[0]] != "0":
            print(N1)
            print(N2)
            print(N3)
            return
    print("UNSOLVABLE")

main()

=======
Suggestion 5

def main():
    S1 = input()
    S2 = input()
    S3 = input()
    S = S1+S2+S3
    S = set(S)
    if len(S) > 10:
        print('UNSOLVABLE')
        return
    S = list(S)
    for p in permutations(range(10), len(S)):
        S1_ = S1.translate(str.maketrans(dict(zip(S, map(str, p)))))
        S2_ = S2.translate(str.maketrans(dict(zip(S, map(str, p)))))
        S3_ = S3.translate(str.maketrans(dict(zip(S, map(str, p)))))
        if S1_[0] == '0' or S2_[0] == '0' or S3_[0] == '0':
            continue
        if int(S1_) + int(S2_) == int(S3_):
            print(S1_)
            print(S2_)
            print(S3_)
            return
    print('UNSOLVABLE')

=======
Suggestion 6

def alphametic(S1, S2, S3):
    if len(S1) < len(S3) or len(S2) < len(S3):
        return "UNSOLVABLE"
    if len(S1) > len(S3) and S1[0] == "0" or len(S2) > len(S3) and S2[0] == "0":
        return "UNSOLVABLE"
    N1 = [0] * len(S1)
    N2 = [0] * len(S2)
    N3 = [0] * len(S3)
    for i in range(len(S3)):
        if S1[-1-i] == S2[-1-i] and S1[-1-i] != S3[-1-i]:
            return "UNSOLVABLE"
        if S1[-1-i] != S2[-1-i] and S1[-1-i] == S3[-1-i]:
            N1[-1-i] = 1
            N2[-1-i] = 1
            N3[-1-i] = 1
        if S1[-1-i] != S2[-1-i] and S2[-1-i] == S3[-1-i]:
            N1[-1-i] = 1
            N2[-1-i] = 1
            N3[-1-i] = 1
    for i in range(len(S3)):
        if S1[-1-i] == S2[-1-i] and S1[-1-i] == S3[-1-i]:
            if N1[-1-i] == 1 and N2[-1-i] == 1:
                N3[-1-i] = 1
            elif N1[-1-i] == 1 and N3[-1-i] == 1:
                N2[-1-i] = 1
            elif N2[-1-i] == 1 and N3[-1-i] == 1:
                N1[-1-i] = 1
            else:
                N1[-1-i] = 1
                N2[-1-i] = 1
                N3[-1-i] = 1
    if N1[0] == 0 and N2[0] == 0 and N3[0] == 0:
        return

=======
Suggestion 7

def main():
    S1 = input()
    S2 = input()
    S3 = input()

    # Check the length of S1, S2, S3
    if len(S1) < 1 or len(S1) > 10 or len(S2) < 1 or len(S2) > 10 or len(S3) < 1 or len(S3) > 10:
        print("UNSOLVABLE")
        return

    # Check the character of S1, S2, S3
    for i in range(len(S1)):
        if S1[i] < 'a' or S1[i] > 'z' or S2[i] < 'a' or S2[i] > 'z' or S3[i] < 'a' or S3[i] > 'z':
            print("UNSOLVABLE")
            return

    # Check the length of S1, S2, S3
    if len(S1) != len(S2) or len(S1) != len(S3) or len(S2) != len(S3):
        print("UNSOLVABLE")
        return

    # Check the character of S1, S2, S3
    for i in range(len(S1)):
        if S1[i] == S2[i] and S1[i] != S3[i]:
            print("UNSOLVABLE")
            return

    # Check the character of S1, S2, S3
    for i in range(len(S1)):
        if S1[i] == S3[i] and S1[i] != S2[i]:
            print("UNSOLVABLE")
            return

    # Check the character of S1, S2, S3
    for i in range(len(S1)):
        if S2[i] == S3[i] and S1[i] != S2[i]:
            print("UNSOLVABLE")
            return

    # Check the character of S1, S2, S3
    for i in range(len(S1)):
        if S1[i] == S2[i] and S2[i] == S3[i]:
            if i == 0:
                if len(S1) == 1:
                    print(1)
                    print(1)
                    print(2)
                    return
                else:
                    print("UNSOLV

=======
Suggestion 8

def main():
    S1 = input()
    S2 = input()
    S3 = input()

    # S1+S2=S3
    # 0<=N1<=9999
    # 0<=N2<=9999
    # 0<=N3<=9999
    # N1+N2=N3
    # N1,N2,N3はすべて異なる

    # 0<=N1<=9999
    # 0<=N2<=9999
    # 0<=N3<=9999
    # N1+N2=N3
    # N1,N2,N3はすべて異なる

    # 0<=N1<=9999
    # 0<=N2<=9999
    # 0<=N3<=9999
    # N1+N2=N3
    # N1,N2,N3はすべて異なる

    # 0<=N1<=9999
    # 0<=N2<=9999
    # 0<=N3<=9999
    # N1+N2=N3
    # N1,N2,N3はすべて異なる

    # 0<=N1<=9999
    # 0<=N2<=9999
    # 0<=N3<=9999
    # N1+N2=N3
    # N1,N2,N3はすべて異なる

    # 0<=N1<=9999
    # 0<=N2<=9999
    # 0<=N3<=9999
    # N1+N2=N3
    # N1,N2,N3はすべて異なる

    # 0<=N1<=9999
    # 0<=N2<=9999
    # 0<=N3<=9999
    # N1+N2=N3
    # N1,N2,N3はすべて異なる

    # 0<=N1<=9999
    # 0<=N2<=9999
    # 0<=N3<=9999
    # N1+N2=N3
    # N1,N2,N3は
