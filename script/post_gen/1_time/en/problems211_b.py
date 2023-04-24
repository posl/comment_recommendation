Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    s4 = input()
    if s1 == "H" and s2 == "2B" and s3 == "3B" and s4 == "HR":
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

    if s1 == "H" and s2 == "2B" and s3 == "3B" and s4 == "HR":
        print("Yes")
    elif s1 == "H" and s2 == "3B" and s3 == "2B" and s4 == "HR":
        print("Yes")
    elif s1 == "HR" and s2 == "2B" and s3 == "3B" and s4 == "H":
        print("Yes")
    elif s1 == "HR" and s2 == "3B" and s3 == "2B" and s4 == "H":
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
    if S_1 == S_2 or S_1 == S_3 or S_1 == S_4 or S_2 == S_3 or S_2 == S_4 or S_3 == S_4:
        print("No")
    else:
        print("Yes")

=======
Suggestion 4

def main():
    a = input()
    b = input()
    c = input()
    d = input()
    if a == "H" or a == "2B" or a == "3B" or a == "HR":
        if b == "H" or b == "2B" or b == "3B" or b == "HR":
            if c == "H" or c == "2B" or c == "3B" or c == "HR":
                if d == "H" or d == "2B" or d == "3B" or d == "HR":
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
Suggestion 5

def main():
    S = []
    for i in range(4):
        S.append(input())
    if S.count('H') == 1:
        if S.count('2B') == 1:
            if S.count('3B') == 1:
                if S.count('HR') == 1:
                    print('Yes')
                    return
    print('No')

=======
Suggestion 6

def main():
    s = [input() for _ in range(4)]
    if len(set(s)) == 4:
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def main():
    #input
    S = [input() for _ in range(4)]

    #output
    if len(set(S)) == 4:
        print('Yes')
    else:
        print('No')

=======
Suggestion 8

def main():
    # Read input
    s1 = input()
    s2 = input()
    s3 = input()
    s4 = input()
    # Check if the sequence has one of each of H, 2B, 3B, and HR
    if s1 == "H" or s2 == "H" or s3 == "H" or s4 == "H":
        if s1 == "2B" or s2 == "2B" or s3 == "2B" or s4 == "2B":
            if s1 == "3B" or s2 == "3B" or s3 == "3B" or s4 == "3B":
                if s1 == "HR" or s2 == "HR" or s3 == "HR" or s4 == "HR":
                    print("Yes")
                    return
    print("No")

=======
Suggestion 9

def main():
    # Get input
    S_1 = input()
    S_2 = input()
    S_3 = input()
    S_4 = input()
    
    # Check if we have one of each of H, 2B, 3B, and HR
    if (S_1 == "H" or S_2 == "H" or S_3 == "H" or S_4 == "H") and (S_1 == "2B" or S_2 == "2B" or S_3 == "2B" or S_4 == "2B") and (S_1 == "3B" or S_2 == "3B" or S_3 == "3B" or S_4 == "3B") and (S_1 == "HR" or S_2 == "HR" or S_3 == "HR" or S_4 == "HR"):
        print("Yes")
    else:
        print("No")

=======
Suggestion 10

def main():
    # 4つの文字列を入力
    S = [input() for i in range(4)]
    # 4つの文字列の中にH, 2B, 3B, HRが含まれているかを判定
    if 'H' in S and '2B' in S and '3B' in S and 'HR' in S:
        print('Yes')
    else:
        print('No')
