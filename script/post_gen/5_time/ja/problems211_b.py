Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    s = [input() for _ in range(4)]
    if "H" in s and "2B" in s and "3B" in s and "HR" in s:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    S1 = input()
    S2 = input()
    S3 = input()
    S4 = input()
    if S1 == 'H' and S2 == '2B' and S3 == '3B' and S4 == 'HR':
        print('Yes')
    elif S1 == '2B' and S2 == '3B' and S3 == 'HR' and S4 == '3B':
        print('No')
    else:
        print('No')

=======
Suggestion 3

def main():
    list = []
    for i in range(4):
        list.append(input())
    if "H" in list and "2B" in list and "3B" in list and "HR" in list:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    s4 = input()
    if s1 == "H" and s2 == "2B" and s3 == "3B" and s4 == "HR":
        print("Yes")
    elif s1 == "2B" and s2 == "3B" and s3 == "HR" and s4 == "3B":
        print("No")
    else:
        print("No")

=======
Suggestion 5

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    s4 = input()
    if s1 == "H" and s2 == "2B" and s3 == "3B" and s4 == "HR":
        print("Yes")
    elif s1 == "2B" and s2 == "3B" and s3 == "HR" and s4 == "2B":
        print("Yes")
    elif s1 == "3B" and s2 == "HR" and s3 == "2B" and s4 == "3B":
        print("Yes")
    elif s1 == "HR" and s2 == "2B" and s3 == "3B" and s4 == "HR":
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    s4 = input()

    if s1 == "H" and s2 == "2B" and s3 == "3B" and s4 == "HR":
        print("Yes")
    elif s1 == "2B" and s2 == "3B" and s3 == "HR" and s4 == "3B":
        print("No")
    elif s1 == "3B" and s2 == "HR" and s3 == "2B" and s4 == "H":
        print("Yes")
    elif s1 == "HR" and s2 == "2B" and s3 == "H" and s4 == "3B":
        print("Yes")
    elif s1 == "2B" and s2 == "HR" and s3 == "3B" and s4 == "H":
        print("Yes")
    elif s1 == "3B" and s2 == "2B" and s3 == "H" and s4 == "HR":
        print("No")
    elif s1 == "HR" and s2 == "3B" and s3 == "H" and s4 == "2B":
        print("Yes")
    elif s1 == "H" and s2 == "3B" and s3 == "HR" and s4 == "2B":
        print("Yes")
    elif s1 == "2B" and s2 == "H" and s3 == "HR" and s4 == "3B":
        print("Yes")
    elif s1 == "3B" and s2 == "H" and s3 == "2B" and s4 == "HR":
        print("No")
    elif s1 == "HR" and s2 == "H" and s3 == "3B" and s4 == "2B":
        print("Yes")
    elif s1 == "H" and s2 == "2B" and s3 == "HR" and s4 == "3B":
        print("Yes")
    elif s1 == "2B" and s2 == "H" and s3 == "3B" and s4 == "HR":
        print("No")
    elif s1 ==

=======
Suggestion 7

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    s4 = input()

    if s1 == "H" and s2 == "2B" and s3 == "3B" and s4 == "HR":
        print("Yes")
    elif s1 == "2B" and s2 == "3B" and s3 == "HR" and s4 == "3B":
        print("Yes")
    elif s1 == "3B" and s2 == "HR" and s3 == "3B" and s4 == "HR":
        print("Yes")
    elif s1 == "HR" and s2 == "3B" and s3 == "HR" and s4 == "3B":
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    s4 = input()
    if s1 == "H" and s2 == "2B" and s3 == "3B" and s4 == "HR":
        print("Yes")
    elif s1 == "2B" and s2 == "3B" and s3 == "HR" and s4 == "3B":
        print("No")
    elif s1 == "H" and s2 == "2B" and s3 == "3B" and s4 == "3B":
        print("No")
    elif s1 == "H" and s2 == "2B" and s3 == "HR" and s4 == "3B":
        print("No")
    elif s1 == "H" and s2 == "3B" and s3 == "HR" and s4 == "3B":
        print("No")
    elif s1 == "H" and s2 == "3B" and s3 == "HR" and s4 == "2B":
        print("No")
    elif s1 == "H" and s2 == "2B" and s3 == "HR" and s4 == "2B":
        print("No")
    elif s1 == "H" and s2 == "3B" and s3 == "2B" and s4 == "HR":
        print("No")
    elif s1 == "H" and s2 == "2B" and s3 == "3B" and s4 == "2B":
        print("No")
    elif s1 == "H" and s2 == "3B" and s3 == "2B" and s4 == "2B":
        print("No")
    elif s1 == "H" and s2 == "2B" and s3 == "2B" and s4 == "HR":
        print("No")
    elif s1 == "H" and s2 == "2B" and s3 == "2B" and s4 == "3B":
        print("No")
    elif s1 == "H" and s2 == "2B" and s3 == "2B" and s4 == "2B":
        print("No")

=======
Suggestion 9

def main():
    # input
    S_1 = input()
    S_2 = input()
    S_3 = input()
    S_4 = input()
    # compute
    S_list = [S_1, S_2, S_3, S_4]
    if (S_list.count("H") == 1) and (S_list.count("2B") == 1) and (S_list.count("3B") == 1) and (S_list.count("HR") == 1):
        result = "Yes"
    else:
        result = "No"
    # output
    print(result)

=======
Suggestion 10

def main():
    a = [input() for _ in range(4)]
    if 'H' in a and '2B' in a and '3B' in a and 'HR' in a:
        print('Yes')
    else:
        print('No')
