Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    s1 = input()
    s2 = input()
    s3 = input()
    n1 = len(s1)
    n2 = len(s2)
    n3 = len(s3)
    if n1 < n2:
        s1, s2 = s2, s1
        n1, n2 = n2, n1
    if n1 < n3:
        s1, s3 = s3, s1
        n1, n3 = n3, n1
    if n2 < n3:
        s2, s3 = s3, s2
        n2, n3 = n3, n2
    if n1 == n2 and n1 == n3:
        if s1 == s2 and s1 == s3:
            if s1 == 'a':
                print(1)
                print(1)
                print(1)
                return
            else:
                print('UNSOLVABLE')
                return
        else:
            for i in range(10):
                for j in range(10):
                    for k in range(10):
                        if i + j == k and s1[0] != str(i) and s2[0] != str(j) and s3[0] != str(k):
                            print(i)
                            print(j)
                            print(k)
                            return
    elif n1 == n2 and n1 > n3:
        for i in range(10):
            for j in range(10):
                for k in range(10):
                    if s1[0] != str(i) and s2[0] != str(j) and s3[0] != str(k):
                        if s1[-n3:] == s3:
                            if s2[-n3:] == s3:
                                if i + j == k:
                                    print(i)
                                    print(j)
                                    print(k)
                                    return
                            else:
                                if i + j == k:
                                    print(i)
                                    print(j)
                                    print(k)
                                    return
                                else:
                                    if i + j + 1 == k:
                                        print(i)
                                        print(j)
                                        print(k)
                                        return
        print('UNSOLVABLE')
        return
    elif n1 == n2 and n1 < n3:
        for i in range(10):
            for j

=======
Suggestion 2

def main():
    S1 = input()
    S2 = input()
    S3 = input()
    N1 = len(S1)
    N2 = len(S2)
    N3 = len(S3)
    if N1 < N2:
        S1, S2 = S2, S1
        N1, N2 = N2, N1
    if N1 < N3:
        S1, S3 = S3, S1
        N1, N3 = N3, N1
    if N2 < N3:
        S2, S3 = S3, S2
        N2, N3 = N3, N2
    if N1 > N2 + N3:
        print("UNSOLVABLE")
        return
    if N1 == N3 and S1[-1] == S3[-1]:
        print("UNSOLVABLE")
        return
    if N1 == N3 and S1[-1] != S3[-1]:
        print("UNSOLVABLE")
        return
    if N1 == N2 + N3 and S1[-1] != S3[-1]:
        print("UNSOLVABLE")
        return
    for i in range(10):
        for j in range(10):
            for k in range(10):
                if i == j or j == k or k == i:
                    continue
                if S1[-1] == S3[-1] and S1[-1] == S2[-1]:
                    if S1[-2] == S2[-2]:
                        if int(S1[-1]) + int(S2[-1]) + int(S1[-2]) != int(S3[-1]) + int(S1[-2]) * 10:
                            continue
                    else:
                        if int(S1[-1]) + int(S2[-1]) != int(S3[-1]):
                            continue
                elif S1[-1] == S3[-1]:
                    if S1[-2] == S2[-2]:
                        if int(S1[-1]) + int(S2[-1]) + int(S1[-2]) != int(S3[-1]) + int(S1[-2]) * 10:
                            continue
                    else:
                        if int(S1[-1]) + int(S2[-1]) != int

=======
Suggestion 3

def solve():
    S1 = input()
    S2 = input()
    S3 = input()
    N1 = len(S1)
    N2 = len(S2)
    N3 = len(S3)
    if N1 < N3 or N2 < N3:
        print("UNSOLVABLE")
        return
    if N1 > N3:
        if S1[0] == '0':
            print("UNSOLVABLE")
            return
    if N2 > N3:
        if S2[0] == '0':
            print("UNSOLVABLE")
            return
    if N1 == N3:
        if S1[0] == '0':
            print("UNSOLVABLE")
            return
    if N2 == N3:
        if S2[0] == '0':
            print("UNSOLVABLE")
            return
    if S3[0] == '0':
        if N1 == N3 and N2 == N3:
            print("UNSOLVABLE")
            return
        if N1 == N3:
            if S2[0] == '0':
                print("UNSOLVABLE")
                return
        if N2 == N3:
            if S1[0] == '0':
                print("UNSOLVABLE")
                return
    if N1 > N2:
        print("UNSOLVABLE")
        return
    if N1 == N2:
        if S1[0] < S2[0]:
            print("UNSOLVABLE")
            return
    S = S1 + S2 + S3
    S = list(set(S))
    if len(S) > 10:
        print("UNSOLVABLE")
        return
    for i in range(10):
        for j in range(10):
            for k in range(10):
                for l in range(10):
                    for m in range(10):
                        for n in range(10):
                            for o in range(10):
                                for p in range(10):
                                    for q in range(10):
                                        for r in range(10):
                                            if len(set([i, j, k, l, m, n, o, p, q, r])) == 10:
                                                S1_ = S1.replace(S[0], str(i)).replace

=======
Suggestion 4

def solve():
    S = [input() for _ in range(3)]
    if len(S[0]) < len(S[1]):
        S[0], S[1] = S[1], S[0]
    if len(S[0]) < len(S[2]):
        S[0], S[2] = S[2], S[0]
    if len(S[1]) < len(S[2]):
        S[1], S[2] = S[2], S[1]
    if len(S[0]) == len(S[1]) + len(S[2]):
        if len(S[1]) < len(S[2]):
            S[1], S[2] = S[2], S[1]
        if len(S[0]) == 1 and len(S[1]) == 1 and len(S[2]) == 1:
            print(1)
            print(1)
            print(2)
            return
        if S[0][0] == S[1][0] or S[0][0] == S[2][0]:
            print("UNSOLVABLE")
            return
        if len(S[0]) == len(S[1]) == len(S[2]):
            if S[0][0] == S[1][0] or S[0][0] == S[2][0]:
                print("UNSOLVABLE")
                return
            if S[0][1] == S[1][1] or S[0][1] == S[2][1]:
                print("UNSOLVABLE")
                return
            if S[0][2] == S[1][2] or S[0][2] == S[2][2]:
                print("UNSOLVABLE")
                return
            print(1)
            print(1)
            print(2)
            return
        print("UNSOLVABLE")
        return
    if len(S[0]) == len(S[1]):
        if len(S[0]) == 1 and len(S[1]) == 1 and len(S[2]) == 1:
            print(1)
            print(1)
            print(2)
            return
        if S[0][0] == S[1][0]:
            print("UNSOLVABLE")
            return

=======
Suggestion 5

def solve():
    s1 = input()
    s2 = input()
    s3 = input()
    n1 = len(s1)
    n2 = len(s2)
    n3 = len(s3)
    if n1 > n3 or n2 > n3:
        print("UNSOLVABLE")
        return
    s = set(s1 + s2 + s3)
    if len(s) > 10:
        print("UNSOLVABLE")
        return
    for i in range(10 ** (n1 - 1), 10 ** n1):
        for j in range(10 ** (n2 - 1), 10 ** n2):
            for k in range(10 ** (n3 - 1), 10 ** n3):
                if i + j == k:
                    si = str(i)
                    sj = str(j)
                    sk = str(k)
                    if len(si) != n1 or len(sj) != n2 or len(sk) != n3:
                        continue
                    flag = True
                    for c in s:
                        if si.count(c) != s1.count(c) or sj.count(c) != s2.count(c) or sk.count(c) != s3.count(c):
                            flag = False
                            break
                    if flag:
                        print(si)
                        print(sj)
                        print(sk)
                        return
    print("UNSOLVABLE")

=======
Suggestion 6

def main():
    S1 = input()
    S2 = input()
    S3 = input()
    S = set(S1+S2+S3)
    if len(S) > 10:
        print("UNSOLVABLE")
        return
    N = list(range(10))
    for i in range(10**len(S)):
        for j in range(10**len(S)):
            for k in range(10**len(S)):
                if len(set(str(i)+str(j)+str(k))) == len(S):
                    if str(i)+str(j) == str(k):
                        if len(str(i)) == len(S1) and len(str(j)) == len(S2) and len(str(k)) == len(S3):
                            if check(S1, S2, S3, str(i), str(j), str(k)):
                                print(i)
                                print(j)
                                print(k)
                                return
    print("UNSOLVABLE")

=======
Suggestion 7

def is_valid(n1,n2,n3):
    if len(n1) != len(n2) or len(n1) != len(n3) or len(n2) != len(n3):
        return False
    if n1[0] == '0' or n2[0] == '0' or n3[0] == '0':
        return False
    return True

=======
Suggestion 8

def solve():
    S1 = input()
    S2 = input()
    S3 = input()
    S = S1 + S2 + S3
    S = list(S)
    S = list(set(S))
    if len(S) > 10:
        print("UNSOLVABLE")
        return
    for i in range(10):
        for j in range(10):
            for k in range(10):
                for l in range(10):
                    for m in range(10):
                        for n in range(10):
                            for o in range(10):
                                for p in range(10):
                                    for q in range(10):
                                        for r in range(10):
                                            if i == 0 and S[0] == S1[0]:
                                                continue
                                            if j == 0 and S[1] == S1[0]:
                                                continue
                                            if k == 0 and S[2] == S1[0]:
                                                continue
                                            if l == 0 and S[3] == S1[0]:
                                                continue
                                            if m == 0 and S[4] == S2[0]:
                                                continue
                                            if n == 0 and S[5] == S2[0]:
                                                continue
                                            if o == 0 and S[6] == S2[0]:
                                                continue
                                            if p == 0 and S[7] == S2[0]:
                                                continue
                                            if q == 0 and S[8] == S3[0]:
                                                continue
                                            if r == 0 and S[9] == S3[0]:
                                                continue
                                            if S[0] == S1[0]:
                                                N1 = i*1000 + j*100 + k*10 + l
                                            elif S[0] == S2[0]:
                                                N1 = m*1000 + n*100 + o*10 + p
                                            else:
                                                N1 = q*1000 + r*100 + i*10 + j
                                            if S[1] == S1[0]:
                                                N2 = i*1000 + j*100 + k*10 + l
                                            elif S[1] == S2[0]:
                                                N2 = m*1000 + n*100 + o*10 + p
                                            else:
                                                N2 = q*

=======
Suggestion 9

def alphametic(S1,S2,S3):
    if len(S1) != len(S2) or len(S2) != len(S3):
        return "UNSOLVABLE"
    N1 = [0]*len(S1)
    N2 = [0]*len(S2)
    N3 = [0]*len(S3)
    for i in range(len(S1)):
        if S1[i] == S2[i] and S2[i] == S3[i]:
            continue
        else:
            if S1[i] == S2[i]:
                N1[i] = 1
                N2[i] = 1
                if N3[i] == 0:
                    N3[i] = 2
            elif S2[i] == S3[i]:
                N2[i] = 1
                N3[i] = 1
                if N1[i] == 0:
                    N1[i] = 2
            elif S1[i] == S3[i]:
                N1[i] = 1
                N3[i] = 1
                if N2[i] == 0:
                    N2[i] = 2
            else:
                N1[i] = 1
                N2[i] = 1
                N3[i] = 2
    if N1[0] == 0 or N2[0] == 0 or N3[0] == 0:
        return "UNSOLVABLE"
    else:
        return N1,N2,N3

S1 = input()
S2 = input()
S3 = input()
print(alphametic(S1,S2,S3))

This is my code. It is not working for all the testcases. How do I fix it?

I am new to python and I am trying to find the sum of the list of numbers in python. I am using python 3.6. I am getting the following error:

Traceback (most recent call last):
  File "C:/Users/USER/AppData/Local/Programs/Python/Python36-32/Python36-32/Python36-32/python36-32.py", line 1, in <module>
    print(sum(list))
TypeError: 'int' object is not callable

This is the code:

list = [1, 2, 3

=======
Suggestion 10

def alphametic(S1, S2, S3):
    # S1 + S2 = S3
    # S1 = 1234, S2 = 5678, S3 = 6912
    # 1234 + 5678 = 6912
    # 1 + 5 = 6
    # 2 + 6 = 8
    # 3 + 7 = 9
    # 4 + 8 = 1
    # 2 + 8 = 1
    # 3 + 7 = 9
    # 4 + 6 = 1
    # 3 + 7 = 9
    # 4 + 5 = 9
    # 4 + 5 = 9
    # 1 + 5 = 6
    # 2 + 4 = 6
    # 1 + 5 = 6
    # 2 + 3 = 5
    # 1 + 2 = 3
    #
