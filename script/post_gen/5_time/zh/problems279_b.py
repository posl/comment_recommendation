Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S = input()
    T = input()
    if T in S:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    str1 = input()
    str2 = input()
    if str2 in str1:
        print('Yes')
    else:
        print('No')

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

def problem279_b():
    s = input()
    t = input()
    print('Yes' if t in s else 'No')

=======
Suggestion 5

def main():
    S = input()
    T = input()
    if T in S:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    s = input()
    t = input()
    for i in range(len(s)):
        if s[i:len(t)+i] == t:
            print("Yes")
            break
    else:
        print("No")
