Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    if S[0] == "0":
        print("No")
        return
    if S[-1] == "0":
        print("No")
        return
    for i in range(1, 10):
        if S[i] == "1":
            if S[i-1] == "0" and S[i+1] == "0":
                print("No")
                return
    print("Yes")

=======
Suggestion 2

def main():
    s = input()
    if s[0] == "0":
        print("No")
        return
    for i in range(1, 9):
        if s[i] == "0" and s[i-1] == "1" and s[i+1] == "1":
            print("Yes")
            return
    print("No")

=======
Suggestion 3

def main():
    s = input()
    if s[0] == '0':
        print('No')
        return
    if s[-1] == '1':
        print('No')
        return
    if s[1:-1].count('1') > 1:
        print('Yes')
        return
    print('No')

=======
Suggestion 4

def main():
    S = input()
    if S[0] == '1':
        print('No')
        return
    if S[1] == '0':
        print('Yes')
        return
    if S[2] == '1':
        print('No')
        return
    if S[3] == '0':
        print('Yes')
        return
    if S[4] == '1':
        print('No')
        return
    if S[5] == '0':
        print('Yes')
        return
    if S[6] == '1':
        print('No')
        return
    if S[7] == '0':
        print('Yes')
        return
    if S[8] == '1':
        print('No')
        return
    if S[9] == '0':
        print('Yes')
        return
    print('No')

=======
Suggestion 5

def main():
    S = input()
    if S[0] == '0':
        print('No')
        exit()
    for i in range(1, 9):
        if S[i] == '1' and S[i-1] == '0' and S[i+1] == '0':
            print('Yes')
            exit()
    print('No')
    exit()

=======
Suggestion 6

def main():
    s = input()
    print('Yes' if s[0] == '0' and s[1:].count('1') >= 2 else 'No')

=======
Suggestion 7

def main():
    S = input()
    print('Yes' if S[0] == '0' and S[1:].count('1') >= 2 else 'No')

=======
Suggestion 8

def main():
    S = input()
    print("Yes" if S[1:9].count("1") >= 2 and S[0] == "0" and S[9] == "0" else "No")

=======
Suggestion 9

def bowling_pins(s):
    if s[0] == '0':
        return 'No'
    for i in range(1, 10):
        if s[i] == '1' and '0' in s[i+1:]:
            return 'Yes'
    return 'No'

=======
Suggestion 10

def main():
    S = input()
    print('Yes' if S[1:].count('1') > 0 and S[:9].count('0') > 0 else 'No')
