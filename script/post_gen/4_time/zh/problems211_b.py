Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve():
    s = []
    for i in range(4):
        s.append(input())
    if 'H' in s and '2B' in s and '3B' in s and 'HR' in s:
        print('Yes')
    else:
        print('No')

solve()

=======
Suggestion 2

def main():
    s = set()
    for _ in range(4):
        s.add(input())

    if len(s) == 4:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    s = []
    for i in range(4):
        s.append(input())
    if "H" in s and "2B" in s and "3B" in s and "HR" in s:
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
    s1 = input()
    s2 = input()
    s3 = input()
    s4 = input()
    l = [s1,s2,s3,s4]
    if l.count('H') == 1 and l.count('2B') == 1 and l.count('3B') == 1 and l.count('HR') == 1:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    s4 = input()
    if s1 == "HR" or s2 == "HR" or s3 == "HR" or s4 == "HR":
        if s1 == "2B" or s2 == "2B" or s3 == "2B" or s4 == "2B":
            if s1 == "3B" or s2 == "3B" or s3 == "3B" or s4 == "3B":
                print("Yes")
                exit()
    print("No")

=======
Suggestion 7

def main():
    S1 = input()
    S2 = input()
    S3 = input()
    S4 = input()
    if S1 == 'H' or S2 == 'H' or S3 == 'H' or S4 == 'H':
        if S1 == '2B' or S2 == '2B' or S3 == '2B' or S4 == '2B':
            if S1 == '3B' or S2 == '3B' or S3 == '3B' or S4 == '3B':
                if S1 == 'HR' or S2 == 'HR' or S3 == 'HR' or S4 == 'HR':
                    print('Yes')
                else:
                    print('No')
            else:
                print('No')
        else:
            print('No')
    else:
        print('No')

=======
Suggestion 8

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    s4 = input()
    if s1 == "H" and s2 == "2B" and s3 == "3B" and s4 == "HR":
        print("Yes")
    elif s1 == "H" and s2 == "2B" and s3 == "HR" and s4 == "3B":
        print("Yes")
    elif s1 == "H" and s2 == "3B" and s3 == "2B" and s4 == "HR":
        print("Yes")
    elif s1 == "H" and s2 == "3B" and s3 == "HR" and s4 == "2B":
        print("Yes")
    elif s1 == "H" and s2 == "HR" and s3 == "2B" and s4 == "3B":
        print("Yes")
    elif s1 == "H" and s2 == "HR" and s3 == "3B" and s4 == "2B":
        print("Yes")
    elif s1 == "2B" and s2 == "H" and s3 == "3B" and s4 == "HR":
        print("Yes")
    elif s1 == "2B" and s2 == "H" and s3 == "HR" and s4 == "3B":
        print("Yes")
    elif s1 == "2B" and s2 == "3B" and s3 == "H" and s4 == "HR":
        print("Yes")
    elif s1 == "2B" and s2 == "3B" and s3 == "HR" and s4 == "H":
        print("Yes")
    elif s1 == "2B" and s2 == "HR" and s3 == "H" and s4 == "3B":
        print("Yes")
    elif s1 == "2B" and s2 == "HR" and s3 == "3B" and s4 == "H":
        print("Yes")
    elif s1 == "3B" and s2 == "H" and s3 == "2B" and s4 == "HR":
        print("Yes")
    elif s1 == "

=======
Suggestion 9

def main():
    s = [input() for _ in range(4)]
    if "H" in s and "2B" in s and "3B" in s and "HR" in s:
        print("Yes")
    else:
        print("No")
