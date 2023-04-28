Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s1 = input()
    s2 = input()
    s3 = input()

    if s1 == 'ABC':
        if s2 == 'ARC':
            if s3 == 'AGC':
                print('AHC')
            else:
                print('AGC')
        else:
            print('ARC')
    elif s1 == 'ARC':
        if s2 == 'ABC':
            if s3 == 'AGC':
                print('AHC')
            else:
                print('AGC')
        else:
            print('ABC')
    else:
        if s2 == 'ABC':
            if s3 == 'ARC':
                print('AHC')
            else:
                print('ARC')
        else:
            print('ABC')

=======
Suggestion 2

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
        if s2 == 'ARC':
            print('ABC')
        else:
            print('ARC')
    else:
        if s2 == 'ARC':
            print('AGC')
        else:
            print('ABC')

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
    elif s1 == 'AGC' and s2 == 'ARC':
        print('ABC')
    elif s1 == 'AGC' and s2 == 'ABC':
        print('ARC')
    elif s1 == 'ABC' and s3 == 'ARC':
        print('AGC')
    elif s1 == 'ABC' and s3 == 'AGC':
        print('ARC')
    elif s1 == 'ARC' and s3 == 'AGC':
        print('ABC')
    elif s1 == 'ARC' and s3 == 'ABC':
        print('AGC')
    elif s1 == 'AGC' and s3 == 'ARC':
        print('ABC')
    elif s1 == 'AGC' and s3 == 'ABC':
        print('ARC')
    elif s2 == 'ABC' and s3 == 'ARC':
        print('AGC')
    elif s2 == 'ABC' and s3 == 'AGC':
        print('ARC')
    elif s2 == 'ARC' and s3 == 'AGC':
        print('ABC')
    elif s2 == 'ARC' and s3 == 'ABC':
        print('AGC')
    elif s2 == 'AGC' and s3 == 'ARC':
        print('ABC')
    elif s2 == 'AGC' and s3 == 'ABC':
        print('ARC')

=======
Suggestion 4

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
    elif s1 == "ARC" and s2 == "ABC":
        print("AGC")
    elif s1 == "AGC" and s2 == "ARC":
        print("ABC")
    elif s1 == "AGC" and s2 == "ABC":
        print("ARC")

=======
Suggestion 5

def main():
    s1 = input()
    s2 = input()
    s3 = input()

    if s1 == 'ABC' and s2 == 'ARC':
        print('AGC')
    elif s1 == 'ARC' and s2 == 'ABC':
        print('AGC')
    elif s1 == 'AGC' and s2 == 'ARC':
        print('ABC')
    elif s1 == 'ARC' and s2 == 'AGC':
        print('ABC')
    elif s1 == 'ABC' and s2 == 'AGC':
        print('ARC')
    elif s1 == 'AGC' and s2 == 'ABC':
        print('ARC')

=======
Suggestion 6

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    s = ["ABC", "ARC", "AGC", "AHC"]
    s.remove(s1)
    s.remove(s2)
    s.remove(s3)
    print(s[0])

=======
Suggestion 7

def main():
    # input
    S1 = input()
    S2 = input()
    S3 = input()

    # compute

    # output
    if S1 == 'ABC':
        if S2 == 'ARC':
            print('AGC')
        else:
            print('ARC')
    elif S1 == 'ARC':
        if S2 == 'ABC':
            print('AGC')
        else:
            print('ABC')
    else:
        if S2 == 'ABC':
            print('ARC')
        else:
            print('ABC')

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

=======
Suggestion 9

def solve(S_1, S_2, S_3):
    if S_1 == "ABC":
        if S_2 == "ARC":
            return "AGC"
        elif S_2 == "AGC":
            return "ARC"
    elif S_1 == "ARC":
        if S_2 == "ABC":
            return "AGC"
        elif S_2 == "AGC":
            return "ABC"
    elif S_1 == "AGC":
        if S_2 == "ABC":
            return "ARC"
        elif S_2 == "ARC":
            return "ABC"

S_1 = input()
S_2 = input()
S_3 = input()

print(solve(S_1, S_2, S_3))

=======
Suggestion 10

def find_missing_element():
    # Get the list of input strings
    input_list = []
    for i in range(3):
        input_list.append(input())

    # Define the list of all the 4 contest series
    contest_series = ['ABC', 'ARC', 'AGC', 'AHC']

    # Find the missing element
    for i in range(3):
        for j in range(4):
            if input_list[i] == contest_series[j]:
                contest_series[j] = ''

    for i in range(4):
        if contest_series[i] != '':
            print(contest_series[i])


find_missing_element()
