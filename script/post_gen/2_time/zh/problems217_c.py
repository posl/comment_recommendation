Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S1 = input()
    S2 = input()
    S3 = input()
    if S1 == 'ABC':
        if S2 == 'ARC':
            print('AGC')
        else:
            print('ARC')
    elif S1 == 'AGC':
        if S2 == 'ABC':
            print('ARC')
        else:
            print('ABC')
    else:
        if S2 == 'ABC':
            print('AGC')
        else:
            print('ABC')

=======
Suggestion 2

def main():
    S_1 = input()
    S_2 = input()
    S_3 = input()
    S = [S_1, S_2, S_3]
    if "ABC" not in S:
        print("ABC")
    elif "ARC" not in S:
        print("ARC")
    elif "AGC" not in S:
        print("AGC")
    elif "AHC" not in S:
        print("AHC")

=======
Suggestion 3

def main():
    S1 = input()
    S2 = input()
    S3 = input()
    S = [S1, S2, S3]
    S.sort()
    if S[0] == 'ABC' and S[1] == 'AGC' and S[2] == 'AHC':
        print('ARC')
        print('AGC')
        print('AHC')
    elif S[0] == 'ABC' and S[1] == 'AGC' and S[2] == 'ARC':
        print('AHC')
        print('ARC')
        print('AGC')
    elif S[0] == 'ABC' and S[1] == 'ARC' and S[2] == 'AHC':
        print('AGC')
        print('ARC')
        print('AHC')
    elif S[0] == 'ABC' and S[1] == 'ARC' and S[2] == 'AGC':
        print('AHC')
        print('AGC')
        print('ARC')
    elif S[0] == 'ABC' and S[1] == 'AHC' and S[2] == 'AGC':
        print('ARC')
        print('AGC')
        print('AHC')
    elif S[0] == 'ABC' and S[1] == 'AHC' and S[2] == 'ARC':
        print('AGC')
        print('ARC')
        print('AHC')
    elif S[0] == 'AGC' and S[1] == 'ABC' and S[2] == 'AHC':
        print('ARC')
        print('AGC')
        print('AHC')
    elif S[0] == 'AGC' and S[1] == 'ABC' and S[2] == 'ARC':
        print('AHC')
        print('ARC')
        print('AGC')
    elif S[0] == 'AGC' and S[1] == 'AHC' and S[2] == 'ABC':
        print('ARC')
        print('AGC')
        print('AHC')
    elif S[0] == 'AGC' and S[1] == 'AHC' and S[2] == 'ARC':
        print('ABC')
        print('ARC')
        print('AGC

=======
Suggestion 4

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    if s1 == 'ABC':
        if s2 == 'ARC':
            print('AGC')
        else:
            print('ARC')
    elif s1 == 'ARC':
        if s2 == 'ABC':
            print('AGC')
        else:
            print('ABC')
    else:
        if s2 == 'ABC':
            print('ARC')
        else:
            print('ABC')

=======
Suggestion 5

def main():
    S = []
    for i in range(3):
        S.append(input())
    
    if "ABC" not in S:
        print("ABC")
    elif "ARC" not in S:
        print("ARC")
    elif "AGC" not in S:
        print("AGC")
    elif "AHC" not in S:
        print("AHC")

=======
Suggestion 6

def main():
    S_1 = input()
    S_2 = input()
    S_3 = input()
    S = [S_1, S_2, S_3]
    S.sort()
    if S[0] == 'ABC':
        print('AGC')
    elif S[0] == 'ARC':
        print('AHC')
    elif S[0] == 'AGC':
        print('ABC')
    else:
        print('ARC')

=======
Suggestion 7

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    s = [s1, s2, s3]
    S = ['ABC', 'ARC', 'AGC', 'AHC']
    for i in range(4):
        if S[i] not in s:
            print(S[i])
            break

=======
Suggestion 8

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    if s1 == 'ABC':
        if s2 == 'ARC':
            print('AGC')
        else:
            print('ARC')
    elif s1 == 'AGC':
        if s2 == 'ABC':
            print('ARC')
        else:
            print('ABC')
    else:
        if s2 == 'ABC':
            print('AGC')
        else:
            print('ABC')

=======
Suggestion 9

def main():
    S1 = input()
    S2 = input()
    S3 = input()
    if S1 == "ABC":
        if S2 == "ARC":
            if S3 == "AGC":
                print("AHC")
            else:
                print("AGC")
        else:
            print("ARC")
    elif S1 == "ARC":
        if S2 == "ABC":
            if S3 == "AGC":
                print("AHC")
            else:
                print("AGC")
        else:
            print("ABC")
    else:
        if S2 == "ABC":
            if S3 == "ARC":
                print("AGC")
            else:
                print("ARC")
        else:
            print("ABC")

=======
Suggestion 10

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    if s1 == 'ARC':
        if s2 == 'AGC':
            print('ABC')
        elif s3 == 'AGC':
            print('ABC')
        elif s2 == 'AHC':
            print('ABC')
        elif s3 == 'AHC':
            print('ABC')
    elif s1 == 'AGC':
        if s2 == 'ARC':
            print('ABC')
        elif s3 == 'ARC':
            print('ABC')
        elif s2 == 'AHC':
            print('ABC')
        elif s3 == 'AHC':
            print('ABC')
    elif s1 == 'AHC':
        if s2 == 'ARC':
            print('ABC')
        elif s3 == 'ARC':
            print('ABC')
        elif s2 == 'AGC':
            print('ABC')
        elif s3 == 'AGC':
            print('ABC')
    elif s1 == 'ABC':
        if s2 == 'ARC':
            print('AGC')
        elif s3 == 'ARC':
            print('AGC')
        elif s2 == 'AGC':
            print('ARC')
        elif s3 == 'AGC':
            print('ARC')
        elif s2 == 'AHC':
            print('AGC')
        elif s3 == 'AHC':
            print('AGC')
    else:
        print('ARC')
main()
