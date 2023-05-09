Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    if s[::2].islower() and s[1::2].isupper():
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    s = input()
    odd = s[0::2]
    even = s[1::2]
    if odd.islower() and even.isupper():
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    s = input()
    odd = s[::2]
    even = s[1::2]
    if odd.islower() and even.isupper():
        print("Yes")
    else:
        print("No")
main()

=======
Suggestion 4

def main():
    S = input()
    S_odd = S[::2]
    S_even = S[1::2]

    if S_odd.islower() and S_even.isupper():
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    s = input()
    if len(s) == 1:
        if s.islower():
            print('Yes')
        else:
            print('No')
    else:
        if s[0::2].islower() and s[1::2].isupper():
            print('Yes')
        else:
            print('No')

=======
Suggestion 6

def is_hard_to_read(s):
    if len(s) == 1:
        return s.islower()
    else:
        for i in range(0, len(s), 2):
            if not s[i].isupper():
                return False
        for i in range(1, len(s), 2):
            if not s[i].islower():
                return False
        return True

=======
Suggestion 7

def check_string(s):
    for i in range(0, len(s)):
        if i % 2 == 0:
            if s[i].islower():
                continue
            else:
                return False
        else:
            if s[i].isupper():
                continue
            else:
                return False
    return True

=======
Suggestion 8

def is_hard_to_read(s):
    if len(s) == 1:
        return s.islower()
    else:
        return s[::2].islower() and s[1::2].isupper()

=======
Suggestion 9

def is_hard_to_read(s):
    even = s[::2]
    odd = s[1::2]

    return even.isupper() and odd.islower()

s = input()
print('Yes' if is_hard_to_read(s) else 'No')

=======
Suggestion 10

def is_hard_to_read(s):
    return s[::2].islower() and s[1::2].isupper()
