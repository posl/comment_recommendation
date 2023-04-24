Synthesizing 9/10 solutions

=======
Suggestion 1

def solve(S1, S2, S3):
    if len(S1) < len(S3):
        S1, S3 = S3, S1
    if len(S2) < len(S3):
        S2, S3 = S3, S2
    if len(S1) < len(S2):
        S1, S2 = S2, S1
    if len(S1) < len(S3):
        S1, S3 = S3, S1
    if len(S2) < len(S3):
        S2, S3 = S3, S2

    if len(S1) != len(S2) + len(S3):
        return "UNSOLVABLE"

    for i in range(10):
        for j in range(10):
            for k in range(10):
                if len(S1) == len(S2) + len(S3):
                    if S1.count(str(i)) == S2.count(str(j)) + S3.count(str(k)):
                        if S1.count(str(i)) == 1:
                            if S1.index(str(i)) > S2.index(str(j)) + S3.index(str(k)):
                                return "UNSOLVABLE"
                        else:
                            if S1.index(str(i)) < S2.index(str(j)) + S3.index(str(k)):
                                return "UNSOLVABLE"
                    else:
                        return "UNSOLVABLE"

    return "UNSOLVABLE"

S1 = input()
S2 = input()
S3 = input()

print(solve(S1, S2, S3))

=======
Suggestion 2

def main():
    S1 = input()
    S2 = input()
    S3 = input()
    N1 = len(S1)
    N2 = len(S2)
    N3 = len(S3)
    if N1 > N3 or N2 > N3:
        print('UNSOLVABLE')
        return
    if N1 < N3 and S1[0] == '0':
        print('UNSOLVABLE')
        return
    if N2 < N3 and S2[0] == '0':
        print('UNSOLVABLE')
        return
    L = set(S1) | set(S2) | set(S3)
    if len(L) > 10:
        print('UNSOLVABLE')
        return
    N = len(L)
    for i in range(10**N):
        S = str(i).zfill(N)
        D = dict(zip(L, S))
        if D[S1[0]] == '0' or D[S2[0]] == '0':
            continue
        N1 = int(''.join([D[s] for s in S1]))
        N2 = int(''.join([D[s] for s in S2]))
        N3 = int(''.join([D[s] for s in S3]))
        if N1 + N2 == N3:
            print(N1)
            print(N2)
            print(N3)
            return
    print('UNSOLVABLE')

=======
Suggestion 3

def solve(S1,S2,S3):
    if len(S1) < len(S2):
        S1,S2 = S2,S1
    if len(S1) < len(S3):
        S1,S3 = S3,S1
    if len(S2) < len(S3):
        S2,S3 = S3,S2
    if len(S1) > 10 or len(S2) > 10 or len(S3) > 10:
        return "UNSOLVABLE"
    if len(S1) == len(S2) and len(S1) == len(S3):
        if S1 == S2 and S1 == S3:
            return "UNSOLVABLE"
        else:
            for i in range(1,len(S1)):
                if S1[i] != S2[i] or S1[i] != S3[i] or S2[i] != S3[i]:
                    return "UNSOLVABLE"
            return "1

1

2"
    elif len(S1) == len(S2) and len(S1) > len(S3):
        if S1 == S2:
            return "UNSOLVABLE"
        else:
            for i in range(1,len(S1)):
                if S1[i] != S2[i]:
                    return "UNSOLVABLE"
            for i in range(len(S3)):
                if S3[i] == S1[0] or S3[i] == S2[0]:
                    return "UNSOLVABLE"
            return "1

1

2"
    elif len(S1) > len(S2) and len(S1) == len(S3):
        if S1 == S3:
            return "UNSOLVABLE"
        else:
            for i in range(1,len(S1)):
                if S1[i] != S3[i]:
                    return "UNSOLVABLE"
            for i in range(len(S2)):
                if S2[i] == S1[0] or S2[i] == S3[0]:
                    return "UNSOLVABLE"
            return "1

1

2"
    elif len(S1) > len(S2) and len(S1) > len(S3):
        for i in range(len(S3)):
            if S3[i] == S1[0] or S3[i] == S

=======
Suggestion 4

def alphametic(S1, S2, S3):
    N1 = len(S1)
    N2 = len(S2)
    N3 = len(S3)
    if N1 < N2 or N1 < N3:
        return 'UNSOLVABLE'
    if N1 == N2 and N1 == N3:
        if S1 == S2 == S3:
            return 'UNSOLVABLE'
        if S1[0] == S2[0] == S3[0]:
            return 'UNSOLVABLE'
    if N1 == N2 and N1 > N3:
        if S1[0] == S2[0] and S1[0] == S3[0]:
            return 'UNSOLVABLE'
        if S1[0] == S2[0] and S1[0] != S3[0]:
            return 'UNSOLVABLE'
    if N1 == N3 and N1 > N2:
        if S1[0] == S3[0] and S1[0] == S2[0]:
            return 'UNSOLVABLE'
        if S1[0] == S3[0] and S1[0] != S2[0]:
            return 'UNSOLVABLE'
    if N2 == N3 and N2 > N1:
        if S2[0] == S3[0] and S2[0] == S1[0]:
            return 'UNSOLVABLE'
        if S2[0] == S3[0] and S2[0] != S1[0]:
            return 'UNSOLVABLE'
    if N1 > N2 and N1 > N3:
        if S1[0] == S2[0] == S3[0]:
            return 'UNSOLVABLE'
        if S1[0] == S2[0] and S1[0] != S3[0]:
            return 'UNSOLVABLE'
        if S1[0] == S3[0] and S1[0] != S2[0]:
            return 'UNSOLVABLE'
        if S2[0] == S3[0] and S2[0] != S1[0]:
            return 'UNSOLVABLE'
    if

=======
Suggestion 5

def solve(s1, s2, s3):
    for i in range(10):
        for j in range(10):
            for k in range(10):
                if s1[0] == s2[0] and s2[0] == s3[0] and i == j == k:
                    continue
                if s1[0] != s2[0] and s2[0] == s3[0] and i != j == k:
                    continue
                if s1[0] == s2[0] and s2[0] != s3[0] and i == j != k:
                    continue
                if s1[0] != s2[0] and s2[0] != s3[0] and i != j != k:
                    continue
                if s1[0] == s3[0] and s2[0] == s3[0] and i == k == j:
                    continue
                if s1[0] != s3[0] and s2[0] == s3[0] and i != k == j:
                    continue
                if s1[0] == s3[0] and s2[0] != s3[0] and i == k != j:
                    continue
                if s1[0] != s3[0] and s2[0] != s3[0] and i != k != j:
                    continue
                n1 = i
                n2 = j
                n3 = k
                for c1, c2, c3 in zip(s1[1:], s2[1:], s3[1:]):
                    if c1 == c2 == c3:
                        n1 = n1 * 10
                        n2 = n2 * 10
                        n3 = n3 * 10
                    elif c1 != c2 == c3:
                        n1 = n1 * 10
                        n2 = n2 * 10
                        n3 = n3 * 10 + 1
                    elif c1 == c2 != c3:
                        n1 = n1 * 10
                        n2 = n2 * 10 + 1
                        n3 = n3 * 10
                    elif c1 != c2 != c3:

=======
Suggestion 6

def main():
    S = [input() for _ in range(3)]
    N = [len(s) for s in S]
    if max(N) > 10:
        print('UNSOLVABLE')
        return
    if max(N) == 10:
        if len(set(S[0])) == 1 and len(set(S[1])) == 1 and len(set(S[2])) == 1:
            if S[0][0] == S[1][0] and S[1][0] == S[2][0]:
                print('UNSOLVABLE')
                return
    if N[0] > N[1]:
        S[0], S[1] = S[1], S[0]
        N[0], N[1] = N[1], N[0]
    if N[1] > N[2]:
        S[1], S[2] = S[2], S[1]
        N[1], N[2] = N[2], N[1]
    if N[0] > N[1]:
        S[0], S[1] = S[1], S[0]
        N[0], N[1] = N[1], N[0]
    if N[0] == N[1] == N[2] == 1:
        if S[0] == S[1] and S[1] == S[2]:
            print('UNSOLVABLE')
            return
        else:
            print(1)
            print(1)
            print(2)
            return
    if N[0] == N[1] == N[2] == 2:
        if S[0] == S[1] and S[1] == S[2]:
            print('UNSOLVABLE')
            return
        else:
            print(10)
            print(10)
            print(20)
            return
    if N[0] == N[1] == 1:
        if S[0] == S[1]:
            print('UNSOLVABLE')
            return
        else:
            print(1)
            print(1)
            print(2)
            return
    if N[1] == N[2] == 1:
        if S[1] == S[2]:

=======
Suggestion 7

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    #print(s1,s2,s3)
    s1s2s3 = s1+s2+s3
    #print(s1s2s3)
    s1s2s3 = sorted(list(set(s1s2s3)))
    #print(s1s2s3)
    if len(s1s2s3) > 10:
        print('UNSOLVABLE')
        exit()
    for i in range(10):
        if str(i) in s1s2s3:
            continue
        else:
            s1s2s3.append(str(i))
    #print(s1s2s3)
    for i in range(10**len(s1s2s3)):
        num = str(i).zfill(len(s1s2s3))
        #print(num)
        num_dic = {}
        for j in range(len(s1s2s3)):
            num_dic[s1s2s3[j]] = num[j]
        #print(num_dic)
        n1 = ''
        n2 = ''
        n3 = ''
        for j in range(len(s1)):
            n1 += num_dic[s1[j]]
        for j in range(len(s2)):
            n2 += num_dic[s2[j]]
        for j in range(len(s3)):
            n3 += num_dic[s3[j]]
        if n1[0] == '0' or n2[0] == '0' or n3[0] == '0':
            continue
        if int(n1)+int(n2) == int(n3):
            print(int(n1))
            print(int(n2))
            print(int(n3))
            exit()
    print('UNSOLVABLE')
    return

=======
Suggestion 8

def main():
    S1 = input()
    S

=======
Suggestion 9

def get_numbers(s):
    return [ord(c)-ord('a') for c in s]
