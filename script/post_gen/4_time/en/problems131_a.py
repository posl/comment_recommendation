Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    if s[0] == s[1] or s[1] == s[2] or s[2] == s[3]:
        print("Bad")
    else:
        print("Good")

=======
Suggestion 2

def main():
    s = input()
    if s[0] == s[1] and s[1] == s[2] and s[2] == s[3]:
        print("Bad")
    elif s[0] == s[1] and s[1] == s[2]:
        print("Bad")
    elif s[1] == s[2] and s[2] == s[3]:
        print("Bad")
    else:
        print("Good")

=======
Suggestion 3

def main():
    S = input()
    if S[0] == S[1] and S[1] == S[2] and S[2] == S[3]:
        print("Bad")
    elif S[0] == S[1] and S[1] == S[2]:
        print("Bad")
    elif S[1] == S[2] and S[2] == S[3]:
        print("Bad")
    else:
        print("Good")
main()

=======
Suggestion 4

def main():
    str = input()
    if str[0] == str[1] and str[1] == str[2]:
        print("Bad")
    elif str[1] == str[2] and str[2] == str[3]:
        print("Bad")
    else:
        print("Good")

=======
Suggestion 5

def main():
    input_string = input()
    if input_string[0] == input_string[1] and input_string[1] == input_string[2]:
        print('Bad')
    elif input_string[1] == input_string[2] and input_string[2] == input_string[3]:
        print('Bad')
    else:
        print('Good')

=======
Suggestion 6

def check(S):
    if S[0] == S[1] or S[1] == S[2] or S[2] == S[3]:
        return "Bad"
    else:
        return "Good"

S = input()
print(check(S))

=======
Suggestion 7

def check(s):
    if s[0] == s[1] or s[1] == s[2] or s[2] == s[3]:
        return True
    else:
        return False

=======
Suggestion 8

def check_number(number):
    if number[0] == number[1]:
        return False
    elif number[1] == number[2]:
        return False
    elif number[2] == number[3]:
        return False
    else:
        return True

=======
Suggestion 9

def main():
    #Take input from user
    S = input()
    #Check if the number is hard to enter
    if S[0] == S[1] or S[1] == S[2] or S[2] == S[3]:
        print("Bad")
    else:
        print("Good")

=======
Suggestion 10

def main():
    print('Bad' if len(set(input()))==1 else 'Good')
