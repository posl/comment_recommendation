Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s_list = []
    for i in range(4):
        s_list.append(input())
    if 'H' in s_list and '2B' in s_list and '3B' in s_list and 'HR' in s_list:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    s4 = input()
    list = [s1,s2,s3,s4]
    if "H" in list and "2B" in list and "3B" in list and "HR" in list:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    S_1 = input()
    S_2 = input()
    S_3 = input()
    S_4 = input()

    if S_1 == "H" and S_2 == "2B" and S_3 == "3B" and S_4 == "HR":
        print("Yes")
    elif S_1 == "2B" and S_2 == "3B" and S_3 == "HR" and S_4 == "2B":
        print("Yes")
    elif S_1 == "3B" and S_2 == "HR" and S_3 == "2B" and S_4 == "3B":
        print("Yes")
    elif S_1 == "HR" and S_2 == "2B" and S_3 == "3B" and S_4 == "HR":
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    S = []
    for i in range(4):
        S.append(input())
    if 'H' in S and '2B' in S and '3B' in S and 'HR' in S:
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    a = []
    for i in range(4):
        a.append(input())
    if "H" in a and "2B" in a and "3B" in a and "HR" in a:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    S1 = input()
    S2 = input()
    S3 = input()
    S4 = input()
    if S1 == "H" or S1 == "2B" or S1 == "3B" or S1 == "HR":
        if S2 == "H" or S2 == "2B" or S2 == "3B" or S2 == "HR":
            if S3 == "H" or S3 == "2B" or S3 == "3B" or S3 == "HR":
                if S4 == "H" or S4 == "2B" or S4 == "3B" or S4 == "HR":
                    if S1 != S2 and S1 != S3 and S1 != S4 and S2 != S3 and S2 != S4 and S3 != S4:
                        print("Yes")
                    else:
                        print("No")
                else:
                    print("No")
            else:
                print("No")
        else:
            print("No")
    else:
        print("No")

=======
Suggestion 7

def main():
    s = []
    for i in range(4):
        s.append(input())
    if s.count('H') == 1 and s.count('2B') == 1 and s.count('3B') == 1 and s.count('HR') == 1:
        print('Yes')
    else:
        print('No')

=======
Suggestion 8

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    s4 = input()
    if s1 == 'HR' or s2 == 'HR' or s3 == 'HR' or s4 == 'HR':
        if s1 == '2B' or s2 == '2B' or s3 == '2B' or s4 == '2B':
            if s1 == '3B' or s2 == '3B' or s3 == '3B' or s4 == '3B':
                print('Yes')
            else:
                print('No')
        else:
            print('No')
    else:
        print('No')

=======
Suggestion 9

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    s4 = input()

    if (s1 == 'H' or s2 == 'H' or s3 == 'H' or s4 == 'H') and (s1 == '2B' or s2 == '2B' or s3 == '2B' or s4 == '2B') and (s1 == '3B' or s2 == '3B' or s3 == '3B' or s4 == '3B') and (s1 == 'HR' or s2 == 'HR' or s3 == 'HR' or s4 == 'HR'):
        print('Yes')
    else:
        print('No')

=======
Suggestion 10

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    s4 = input()
    if s1 == 'H' or s2 == 'H' or s3 == 'H' or s4 == 'H':
        if s1 == '2B' or s2 == '2B' or s3 == '2B' or s4 == '2B':
            if s1 == '3B' or s2 == '3B' or s3 == '3B' or s4 == '3B':
                if s1 == 'HR' or s2 == 'HR' or s3 == 'HR' or s4 == 'HR':
                    print('Yes')
                else:
                    print('No')
            else:
                print('No')
        else:
            print('No')
    else:
        print('No')
