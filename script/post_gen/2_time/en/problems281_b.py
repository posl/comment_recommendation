Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    if S[0].isupper() and S[7].isupper() and S[1:7].isdigit() and 100000 <= int(S[1:7]) <= 999999:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    s = input()
    if s[0].isupper() and s[-1].isupper() and s[1:-1].isdecimal() and 100000 <= int(s[1:-1]) <= 999999:
        print('Yes')
    else:
        print('No')

main()

=======
Suggestion 3

def main():
    s = input()
    if s[0].isupper() and s[-1].isupper() and s[1:-1].isdigit() and len(s[1:-1]) == 6 and 100000 <= int(s[1:-1]) <= 999999:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    s = input()
    if s[0].isupper() and s[1:7].isdigit() and s[7].isupper():
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    S = input()
    if S[0].isupper() and S[1:7].isdigit() and S[7].isupper():
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    S = input()
    if S[0].isupper() and S[-1].isupper() and S[1:7].isdigit() and S[1:7].isdecimal() and int(S[1:7]) in range(100000, 999999+1):
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def main():
    s = input()
    if len(s) != 10:
        print("No")
        return
    if s[0].isupper() and s[9].isupper():
        if s[1:7].isdigit():
            if int(s[1:7]) >= 100000 and int(s[1:7]) <= 999999:
                print("Yes")
                return
    print("No")

=======
Suggestion 8

def main():
    s = input()
    if len(s) != 10:
        print("No")
        return
    if s[0].isupper() and s[9].isupper():
        if s[1:7].isdigit() and 100000 <= int(s[1:7]) <= 999999:
            print("Yes")
            return
    print("No")

main()

=======
Suggestion 9

def main():
    S = input()
    if len(S) == 10 and S[0].isupper() and S[1:7].isdigit() and S[7].isupper():
        print("Yes")
    else:
        print("No")

=======
Suggestion 10

def main():
    S = input()
    print('Yes' if S[0].isupper() and S[1:7].isdigit() and S[7].isupper() and len(S)==8 else 'No')
