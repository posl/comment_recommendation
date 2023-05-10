Synthesizing 10/10 solutions

=======
Suggestion 1

def check_same_number(input_str):
    if input_str[0] == input_str[1]:
        if input_str[0] == input_str[2]:
            return True
    if input_str[1] == input_str[2]:
        if input_str[1] == input_str[3]:
            return True
    return False

input_str = input()

=======
Suggestion 2

def main():
    s = input()
    if s[0] == s[1] and s[1] == s[2] and s[2] == s[3]:
        print('Bad')
    elif s[1] == s[2] and s[2] == s[3]:
        print('Bad')
    elif s[0] == s[1] and s[1] == s[2]:
        print('Bad')
    elif s[0] == s[1] and s[1] == s[3]:
        print('Bad')
    elif s[0] == s[2] and s[2] == s[3]:
        print('Bad')
    else:
        print('Good')

=======
Suggestion 3

def main():
    S = input()
    if S[0] == S[1] == S[2] == S[3]:
        print("Bad")
    elif S[0] == S[1] == S[2] or S[1] == S[2] == S[3]:
        print("Bad")
    else:
        print("Good")

main()

=======
Suggestion 4

def is_same_number(s):
    if s[0] == s[1] and s[1] == s[2]:
        return True
    elif s[1] == s[2] and s[2] == s[3]:
        return True
    return False

=======
Suggestion 5

def main():
    S = input()
    if S[0] == S[1] and S[1] == S[2] and S[2] == S[3]:
        print('Bad')
    elif S[0] != S[1] and S[1] != S[2] and S[2] != S[3]:
        print('Good')
    else:
        print('Bad')

=======
Suggestion 6

def main():
    S = input()
    if S[0] == S[1] == S[2] or S[1] == S[2] == S[3]:
        print("Bad")
    else:
        print("Good")

=======
Suggestion 7

def check_security_code(security_code):
    if security_code[0] == security_code[1]:
        if security_code[1] == security_code[2]:
            return "Bad"
        else:
            if security_code[2] == security_code[3]:
                return "Bad"
    elif security_code[1] == security_code[2]:
        if security_code[2] == security_code[3]:
            return "Bad"
    return "Good"

=======
Suggestion 8

def check_num(num):
    if num[0] == num[1] and num[1] == num[2]:
        return True
    elif num[1] == num[2] and num[2] == num[3]:
        return True
    else:
        return False

=======
Suggestion 9

def main():
    s = input()
    if s[0] == s[1] == s[2] or s[1] == s[2] == s[3]:
        print("Bad")
    else:
        print("Good")

=======
Suggestion 10

def main():
    s = input()
    if s[0] == s[1] == s[2] == s[3]:
        print("Bad")
    elif s[1] == s[2] == s[3]:
        print("Bad")
    elif s[0] == s[1] == s[2]:
        print("Bad")
    elif s[0] == s[1] == s[3]:
        print("Bad")
    elif s[0] == s[2] == s[3]:
        print("Bad")
    else:
        print("Good")
