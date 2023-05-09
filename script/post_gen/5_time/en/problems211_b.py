Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    s4 = input()

    if s1 == "H" and s2 == "2B" and s3 == "3B" and s4 == "HR":
        print("Yes")
    elif s1 == "2B" and s2 == "3B" and s3 == "HR" and s4 == "H":
        print("Yes")
    elif s1 == "3B" and s2 == "HR" and s3 == "H" and s4 == "2B":
        print("Yes")
    elif s1 == "HR" and s2 == "H" and s3 == "2B" and s4 == "3B":
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    S = []
    for i in range(4):
        S.append(input())
    if "H" in S and "2B" in S and "3B" in S and "HR" in S:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    S1 = input()
    S2 = input()
    S3 = input()
    S4 = input()
    if S1 == 'H' and S2 == '2B' and S3 == '3B' and S4 == 'HR':
        print('Yes')
    elif S1 == '2B' and S2 == '3B' and S3 == 'HR' and S4 == 'H':
        print('Yes')
    elif S1 == '3B' and S2 == 'HR' and S3 == 'H' and S4 == '2B':
        print('Yes')
    elif S1 == 'HR' and S2 == 'H' and S3 == '2B' and S4 == '3B':
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    S1 = input()
    S2 = input()
    S3 = input()
    S4 = input()
    if S1 == 'H' and S2 == '2B' and S3 == '3B' and S4 == 'HR':
        print('Yes')
    elif S1 == '2B' and S2 == '3B' and S3 == 'HR' and S4 == 'H':
        print('Yes')
    elif S1 == '3B' and S2 == 'HR' and S3 == 'H' and S4 == '2B':
        print('Yes')
    elif S1 == 'HR' and S2 == 'H' and S3 == '2B' and S4 == '3B':
        print('Yes')
    else:
        print('No')

main()

=======
Suggestion 5

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    s4 = input()
    if s1 == "H" and s2 == "HR" and s3 == "2B" and s4 == "3B":
        print("Yes")
    elif s1 == "H" and s2 == "2B" and s3 == "HR" and s4 == "3B":
        print("Yes")
    elif s1 == "H" and s2 == "3B" and s3 == "2B" and s4 == "HR":
        print("Yes")
    elif s1 == "HR" and s2 == "H" and s3 == "2B" and s4 == "3B":
        print("Yes")
    elif s1 == "HR" and s2 == "2B" and s3 == "H" and s4 == "3B":
        print("Yes")
    elif s1 == "HR" and s2 == "3B" and s3 == "2B" and s4 == "H":
        print("Yes")
    elif s1 == "2B" and s2 == "H" and s3 == "HR" and s4 == "3B":
        print("Yes")
    elif s1 == "2B" and s2 == "HR" and s3 == "H" and s4 == "3B":
        print("Yes")
    elif s1 == "2B" and s2 == "3B" and s3 == "H" and s4 == "HR":
        print("Yes")
    elif s1 == "3B" and s2 == "H" and s3 == "HR" and s4 == "2B":
        print("Yes")
    elif s1 == "3B" and s2 == "HR" and s3 == "H" and s4 == "2B":
        print("Yes")
    elif s1 == "3B" and s2 == "2B" and s3 == "H" and s4 == "HR":
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    # input
    Ss = [input() for _ in range(4)]

    # compute

    # output
    if len(set(Ss)) == 4:
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def main():
    s = [input() for _ in range(4)]
    if len(set(s)) == 4:
        print('Yes')
    else:
        print('No')

=======
Suggestion 8

def solve(S):
    if len(set(S)) == 4:
        return "Yes"
    else:
        return "No"
