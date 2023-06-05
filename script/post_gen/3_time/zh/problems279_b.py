Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    t = input()
    if t in s:
        print("Yes")
    else:
        print("No")
main()

=======
Suggestion 2

def main():
    S = input()
    T = input()
    if T in S:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    s = input()
    t = input()
    if t in s:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def check_substring(string1,string2):
    len1 = len(string1)
    len2 = len(string2)
    if len1 < len2:
        return False
    if len1 == len2:
        if string1 == string2:
            return True
        else:
            return False
    for i in range(len1-len2+1):
        if string1[i:i+len2] == string2:
            return True
    return False

=======
Suggestion 5

def solve():
    s = input()
    t = input()
    if t in s:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    S = input()
    T = input()
    S_length = len(S)
    T_length = len(T)
    for i in range(S_length - T_length + 1):
        if S[i: i + T_length] == T:
            print("Yes")
            exit()
    print("No")
