Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = [input() for _ in range(4)]
    if S.count("H") == 1 and S.count("2B") == 1 and S.count("3B") == 1 and S.count("HR") == 1:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    S = []
    for i in range(4):
        S.append(input())
    if S.count("H") == 1 and S.count("2B") == 1 and S.count("3B") == 1 and S.count("HR") == 1:
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
    if S1 == "H" and S2 == "2B" and S3 == "3B" and S4 == "HR":
        print("Yes")
    else:
        print("No")
    return

=======
Suggestion 4

def main():
    S = []
    for i in range(4):
        S.append(input())
    if S.count('H') == 1 and S.count('2B') == 1 and S.count('3B') == 1 and S.count('HR') == 1:
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    s = []
    for i in range(4):
        s.append(input())
    if "H" in s and "2B" in s and "3B" in s and "HR" in s:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    s = set()
    for i in range(4):
        s.add(input())
    if len(s) == 4:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    s = input().split()
    if 'H' in s and '2B' in s and '3B' in s and 'HR' in s:
        print("Yes")
    else:
        print("No")

main()

=======
Suggestion 8

def main():
    s = set(input() for _ in range(4))
    if len(s) == 4:
        print('Yes')
    else:
        print('No')

=======
Suggestion 9

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    s4 = input()

    # print(s1, s2, s3, s4)

    if 'H' in s1 and 'H' in s2 and 'H' in s3 and 'H' in s4:
        if '2B' in s1 and '2B' in s2 and '2B' in s3 and '2B' in s4:
            if '3B' in s1 and '3B' in s2 and '3B' in s3 and '3B' in s4:
                if 'HR' in s1 and 'HR' in s2 and 'HR' in s3 and 'HR' in s4:
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
Suggestion 10

def main():
    # Read data
    S1 = input()
    S2 = input()
    S3 = input()
    S4 = input()
    # Check data
    if (S1 == 'H' or S2 == 'H' or S3 == 'H' or S4 == 'H') and \
        (S1 == '2B' or S2 == '2B' or S3 == '2B' or S4 == '2B') and \
        (S1 == '3B' or S2 == '3B' or S3 == '3B' or S4 == '3B') and \
        (S1 == 'HR' or S2 == 'HR' or S3 == 'HR' or S4 == 'HR'):
        print('Yes')
    else:
        print('No')

main()
