Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S1 = input()
    S2 = input()
    S3 = input()
    S = [S1, S2, S3]
    if "ABC" not in S:
        print("ABC")
    elif "ARC" not in S:
        print("ARC")
    elif "AGC" not in S:
        print("AGC")
    elif "AHC" not in S:
        print("AHC")

=======
Suggestion 2

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    if s1 == 'ABC' and s2 == 'ARC':
        print('AGC')
    elif s1 == 'ABC' and s2 == 'AGC':
        print('ARC')
    elif s1 == 'ARC' and s2 == 'ABC':
        print('AGC')
    elif s1 == 'ARC' and s2 == 'AGC':
        print('ABC')
    elif s1 == 'AGC' and s2 == 'ABC':
        print('ARC')
    elif s1 == 'AGC' and s2 == 'ARC':
        print('ABC')
    else:
        print('AHC')

=======
Suggestion 3

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    if s1 == 'ABC' and s2 == 'ARC':
        print('AGC')
    elif s1 == 'ABC' and s2 == 'AGC':
        print('ARC')
    elif s1 == 'ARC' and s2 == 'AGC':
        print('ABC')
    elif s1 == 'ARC' and s2 == 'ABC':
        print('AGC')
    elif s1 == 'AGC' and s2 == 'ABC':
        print('ARC')
    elif s1 == 'AGC' and s2 == 'ARC':
        print('ABC')

=======
Suggestion 4

def main():
    S1 = input()
    S2 = input()
    S3 = input()
    if S1 == 'ABC' and S2 == 'ARC':
        print('AGC')
    elif S1 == 'ABC' and S2 == 'AGC':
        print('ARC')
    elif S1 == 'ARC' and S2 == 'ABC':
        print('AGC')
    elif S1 == 'ARC' and S2 == 'AGC':
        print('ABC')
    elif S1 == 'AGC' and S2 == 'ABC':
        print('ARC')
    elif S1 == 'AGC' and S2 == 'ARC':
        print('ABC')
    elif S1 == 'ABC' and S3 == 'ARC':
        print('AGC')
    elif S1 == 'ABC' and S3 == 'AGC':
        print('ARC')
    elif S1 == 'ARC' and S3 == 'ABC':
        print('AGC')
    elif S1 == 'ARC' and S3 == 'AGC':
        print('ABC')
    elif S1 == 'AGC' and S3 == 'ABC':
        print('ARC')
    elif S1 == 'AGC' and S3 == 'ARC':
        print('ABC')
    elif S2 == 'ABC' and S3 == 'ARC':
        print('AGC')
    elif S2 == 'ABC' and S3 == 'AGC':
        print('ARC')
    elif S2 == 'ARC' and S3 == 'ABC':
        print('AGC')
    elif S2 == 'ARC' and S3 == 'AGC':
        print('ABC')
    elif S2 == 'AGC' and S3 == 'ABC':
        print('ARC')
    elif S2 == 'AGC' and S3 == 'ARC':
        print('ABC')

=======
Suggestion 5

def find_missing_element(list):
    for i in range(len(list)):
        if list[i] == "ABC":
            list.remove("ABC")
        elif list[i] == "ARC":
            list.remove("ARC")
        elif list[i] == "AGC":
            list.remove("AGC")
        elif list[i] == "AHC":
            list.remove("AHC")
    return list

=======
Suggestion 6

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    if s1 == 'ABC' and s2 == 'ARC':
        print('AGC')
    elif s1 == 'ABC' and s2 == 'AGC':
        print('ARC')
    elif s1 == 'ARC' and s2 == 'ABC':
        print('AGC')
    elif s1 == 'ARC' and s2 == 'AGC':
        print('ABC')
    elif s1 == 'AGC' and s2 == 'ABC':
        print('ARC')
    elif s1 == 'AGC' and s2 == 'ARC':
        print('ABC')
    elif s1 == 'ABC' and s3 == 'ARC':
        print('AGC')
    elif s1 == 'ABC' and s3 == 'AGC':
        print('ARC')
    elif s1 == 'ARC' and s3 == 'ABC':
        print('AGC')
    elif s1 == 'ARC' and s3 == 'AGC':
        print('ABC')
    elif s1 == 'AGC' and s3 == 'ABC':
        print('ARC')
    elif s1 == 'AGC' and s3 == 'ARC':
        print('ABC')
    elif s2 == 'ABC' and s3 == 'ARC':
        print('AGC')
    elif s2 == 'ABC' and s3 == 'AGC':
        print('ARC')
    elif s2 == 'ARC' and s3 == 'ABC':
        print('AGC')
    elif s2 == 'ARC' and s3 == 'AGC':
        print('ABC')
    elif s2 == 'AGC' and s3 == 'ABC':
        print('ARC')
    elif s2 == 'AGC' and s3 == 'ARC':
        print('ABC')

=======
Suggestion 7

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    if s1 == "ABC" and s2 == "ARC":
        print("AGC")
    elif s1 == "ABC" and s2 == "AGC":
        print("ARC")
    elif s1 == "ARC" and s2 == "AGC":
        print("ABC")
    else:
        print("AHC")

=======
Suggestion 8

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    s = [s1, s2, s3]
    if 'ABC' not in s:
        print('ABC')
    elif 'ARC' not in s:
        print('ARC')
    elif 'AGC' not in s:
        print('AGC')
    elif 'AHC' not in s:
        print('AHC')
    return

=======
Suggestion 9

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    if s1 == 'ABC' and s2 == 'ARC':
        print('AGC')
    elif s1 == 'ABC' and s2 == 'AGC':
        print('ARC')
    elif s1 == 'ARC' and s2 == 'ABC':
        print('AGC')
    elif s1 == 'ARC' and s2 == 'AGC':
        print('ABC')
    elif s1 == 'AGC' and s2 == 'ABC':
        print('ARC')
    elif s1 == 'AGC' and s2 == 'ARC':
        print('ABC')

=======
Suggestion 10

def solution():
    s = []
    for i in range(3):
        s.append(input())
    if 'ABC' not in s:
        print('ABC')
    elif 'ARC' not in s:
        print('ARC')
    elif 'AGC' not in s:
        print('AGC')
    elif 'AHC' not in s:
        print('AHC')
