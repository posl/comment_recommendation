Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    if s[0].isupper() and s[7].isupper() and s[1:7].isdigit() and 100000 <= int(s[1:7]) <= 999999:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    s = input()
    if s[0].isupper() and s[7].isupper() and s[1:7].isdigit() and 100000 <= int(s[1:7]) <= 999999:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    s = input()
    if s[0].isupper() and s[-1].isupper() and len(s) == 8 and s[1:7].isdigit() and int(s[1:7]) >= 100000 and int(s[1:7]) <= 999999:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    S = input()
    if S[0].isupper() and S[7].isupper() and S[1:7].isdecimal():
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    s = input()
    if s[0].isupper() and s[-1].isupper() and s[1:-1].isdigit() and len(s) == 8 and 100000 <= int(s[1:-1]) <= 999999:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    S = input()
    if S[0].isupper() and S[-1].isupper() and len(S) == 8 and S[1:7].isdigit() and int(S[1:7]) >= 100000 and int(S[1:7]) <= 999999:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def check(s):
    if len(s) != 8:
        return False
    if not s[0].isupper():
        return False
    if not s[7].isupper():
        return False
    if not s[1:7].isdigit():
        return False
    if not 100000 <= int(s[1:7]) <= 999999:
        return False
    return True

print('Yes' if check(input()) else 'No')

=======
Suggestion 8

def check(s):
    if s[0].isupper() == False:
        return False
    elif s[-1].isupper() == False:
        return False
    elif len(s) != 8:
        return False
    elif s[1:7].isdecimal() == False:
        return False
    elif int(s[1:7]) < 100000 or int(s[1:7]) > 999999:
        return False
    else:
        return True

s = input()

=======
Suggestion 9

def check(s):
    if len(s) != 8:
        return False
    if s[0] < "A" or s[0] > "Z":
        return False
    if s[2:7] < "100000" or s[2:7] > "999999":
        return False
    if s[7] < "A" or s[7] > "Z":
        return False
    return True

s = input()
print("Yes" if check(s) else "No")
