Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S_1 = input()
    S_2 = input()
    S_3 = input()
    S_4 = input()

    s_list = [S_1, S_2, S_3, S_4]
    if len(s_list) == len(set(s_list)):
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

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
                    return
    print('No')
    return

=======
Suggestion 3

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    s4 = input()
    s = [s1,s2,s3,s4]
    if "H" in s and "2B" in s and "3B" in s and "HR" in s:
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
    if s1 in ['H','2B','3B','HR'] and s2 in ['H','2B','3B','HR'] and s3 in ['H','2B','3B','HR'] and s4 in ['H','2B','3B','HR']:
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
    if s1 == "H" or s2 == "H" or s3 == "H" or s4 == "H":
        if s1 == "2B" or s2 == "2B" or s3 == "2B" or s4 == "2B":
            if s1 == "3B" or s2 == "3B" or s3 == "3B" or s4 == "3B":
                if s1 == "HR" or s2 == "HR" or s3 == "HR" or s4 == "HR":
                    print("Yes")
                    return
    print("No")

=======
Suggestion 6

def main():
    S_1 = input()
    S_2 = input()
    S_3 = input()
    S_4 = input()
    if S_1 == "H" or S_2 == "H" or S_3 == "H" or S_4 == "H":
        if S_1 == "2B" or S_2 == "2B" or S_3 == "2B" or S_4 == "2B":
            if S_1 == "3B" or S_2 == "3B" or S_3 == "3B" or S_4 == "3B":
                if S_1 == "HR" or S_2 == "HR" or S_3 == "HR" or S_4 == "HR":
                    print("Yes")
                else:
                    print("No")
            else:
                print("No")
        else:
            print("No")
    else:
        print("No")
main()

=======
Suggestion 7

def solve():
    S = []
    for i in range(4):
        S.append(input())
    if "H" in S and "2B" in S and "3B" in S and "HR" in S:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    # 读取输入
    s = []
    for i in range(4):
        s.append(input())
    # 判断是否有H、2B、3B和HR中的各一个
    if 'H' in s and '2B' in s and '3B' in s and 'HR' in s:
        print('Yes')
    else:
        print('No')

=======
Suggestion 9

def main():
    S1 = input()
    S2 = input()
    S3 = input()
    S4 = input()
    if S1 == "H" or S2 == "H" or S3 == "H" or S4 == "H":
        if S1 == "2B" or S2 == "2B" or S3 == "2B" or S4 == "2B":
            if S1 == "3B" or S2 == "3B" or S3 == "3B" or S4 == "3B":
                if S1 == "HR" or S2 == "HR" or S3 == "HR" or S4 == "HR":
                    print("Yes")
                    return
    print("No")

=======
Suggestion 10

def main():
    S_1 = input()
    S_2 = input()
    S_3 = input()
    S_4 = input()
    if S_1 == 'H' and S_2 == '2B' and S_3 == '3B' and S_4 == 'HR':
        print('Yes')
    elif S_1 == '2B' and S_2 == '3B' and S_3 == 'HR' and S_4 == '3B':
        print('Yes')
    else:
        print('No')
