Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S = input()
    if S[0] == S[1] and S[2] == S[3] and S[0] != S[2]:
        print("Yes")
    elif S[0] == S[2] and S[1] == S[3] and S[0] != S[1]:
        print("Yes")
    elif S[0] == S[3] and S[1] == S[2] and S[0] != S[1]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    S = input()
    if S[0] == S[1] and S[2] == S[3] and S[0] != S[2]:
        print('Yes')
    elif S[0] == S[2] and S[1] == S[3] and S[0] != S[1]:
        print('Yes')
    elif S[0] == S[3] and S[1] == S[2] and S[0] != S[1]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    s = input()
    if len(set(s)) == 2:
        if s.count(s[0]) == 2:
            print('Yes')
        else:
            print('No')
    else:
        print('No')

=======
Suggestion 4

def main():
    s = input()
    if len(set(s)) == 2 and s.count(s[0]) == 2:
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    S = input()
    #print(S)
    if S[0] == S[1] and S[2] == S[3]:
        print("Yes")
    elif S[0] == S[2] and S[1] == S[3]:
        print("Yes")
    elif S[0] == S[3] and S[1] == S[2]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    s = input()
    if len(set(s)) == 2:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    input_string = input()
    if len(set(input_string)) == 2:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def check(s):
    if len(s) != 4:
        return False
    for i in range(0, 4):
        if s.count(s[i]) != 2:
            return False
    return True


s = input()

=======
Suggestion 9

def check_if_two_chars_appear_twice_in_str(str):
    if len(str) != 4:
        return False
    if len(set(str)) != 2:
        return False
    for char in set(str):
        if str.count(char) != 2:
            return False
    return True
