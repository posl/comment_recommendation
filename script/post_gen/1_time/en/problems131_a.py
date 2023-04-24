Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S = input()
    if S[0] == S[1] or S[1] == S[2] or S[2] == S[3]:
        print("Bad")
    else:
        print("Good")
main()

=======
Suggestion 2

def main():
    s = input()
    if s[0] == s[1] or s[1] == s[2] or s[2] == s[3]:
        print("Bad")
    else:
        print("Good")

main()

=======
Suggestion 3

def main():
    S = input()
    if S[0] == S[1] or S[1] == S[2] or S[2] == S[3]:
        print("Bad")
    else:
        print("Good")

=======
Suggestion 4

def main():
    s = input()
    if s[0] == s[1] or s[1] == s[2] or s[2] == s[3]:
        print("Bad")
    else:
        print("Good")

=======
Suggestion 5

def main():
    s = input()
    print('Bad' if s[0] == s[1] or s[1] == s[2] or s[2] == s[3] else 'Good')

=======
Suggestion 6

def main():
    sec_code = input()
    if sec_code[0] == sec_code[1] or sec_code[1] == sec_code[2] or sec_code[2] == sec_code[3]:
        print("Bad")
    else:
        print("Good")

=======
Suggestion 7

def main():
    S = input()
    for i in range(len(S)-1):
        if S[i] == S[i+1]:
            print("Bad")
            return
    print("Good")
    return

=======
Suggestion 8

def check_hard_to_enter(s):
    for i in range(3):
        if s[i] == s[i+1]:
            return True
    return False

s = raw_input()
