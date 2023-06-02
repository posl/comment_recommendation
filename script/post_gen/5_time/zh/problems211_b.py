Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S_1 = input()
    S_2 = input()
    S_3 = input()
    S_4 = input()
    if 'H' in [S_1, S_2, S_3, S_4] and '2B' in [S_1, S_2, S_3, S_4] and '3B' in [S_1, S_2, S_3, S_4] and 'HR' in [S_1, S_2, S_3, S_4]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    s = []
    for i in range(4):
        s.append(input())
    if "H" in s and "2B" in s and "3B" in s and "HR" in s:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    s4 = input()

    if (s1 == 'H' or s2 == 'H' or s3 == 'H' or s4 == 'H') and \
       (s1 == '2B' or s2 == '2B' or s3 == '2B' or s4 == '2B') and \
       (s1 == '3B' or s2 == '3B' or s3 == '3B' or s4 == '3B') and \
       (s1 == 'HR' or s2 == 'HR' or s3 == 'HR' or s4 == 'HR'):
        print('Yes')
    else:
        print('No')

main()

=======
Suggestion 4

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    s4 = input()
    if s1 == "H" or s2 == "H" or s3 == "H" or s4 == "H":
        if s1 == "2B" or s2 == "2B" or s3 == "2B" or s4 == "2B":
            if s1 == "3B" or s2 == "3B" or s3 == "3B" or s4 == "3B":
                if s1 == "HR" or s2 == "HR" or s3 == "HR" or s4 == "HR":
                    print("Yes")
                else:
                    print("No")
            else:
                print("No")
        else:
            print("No")
    else:
        print("No")

=======
Suggestion 5

def main():
    S = []
    for i in range(4):
        S.append(input())
    if "H" in S and "2B" in S and "3B" in S and "HR" in S:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    #input
    s1 = input()
    s2 = input()
    s3 = input()
    s4 = input()
    #compute
    s = [s1,s2,s3,s4]
    if 'H' in s and '2B' in s and '3B' in s and 'HR' in s:
        print('Yes')
    else:
        print('No')
    #output

=======
Suggestion 7

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    s4 = input()
    if s1 == "H" or s1 == "2B" or s1 == "3B" or s1 == "HR":
        if s2 == "H" or s2 == "2B" or s2 == "3B" or s2 == "HR":
            if s3 == "H" or s3 == "2B" or s3 == "3B" or s3 == "HR":
                if s4 == "H" or s4 == "2B" or s4 == "3B" or s4 == "HR":
                    print("Yes")
                else:
                    print("No")
            else:
                print("No")
        else:
            print("No")
    else:
        print("No")

=======
Suggestion 8

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    s4 = input()
    if s1 in ['H', '2B', '3B', 'HR'] and s2 in ['H', '2B', '3B', 'HR'] and s3 in ['H', '2B', '3B', 'HR'] and s4 in ['H', '2B', '3B', 'HR']:
        if s1 == s2 or s1 == s3 or s1 == s4 or s2 == s3 or s2 == s4 or s3 == s4:
            print('No')
        else:
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

=======
Suggestion 10

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    s4 = input()
    if s1 == 'HR' or s2 == 'HR' or s3 == 'HR' or s4 == 'HR':
        if s1 == '2B' or s2 == '2B' or s3 == '2B' or s4 == '2B':
            if s1 == '3B' or s2 == '3B' or s3 == '3B' or s4 == '3B':
                print('Yes')
                return
    print('No')
    return
