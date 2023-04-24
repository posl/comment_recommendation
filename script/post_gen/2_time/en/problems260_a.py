Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    if S[0] == S[1] and S[0] == S[2]:
        print(-1)
    elif S[0] == S[1]:
        print(S[2])
    elif S[0] == S[2]:
        print(S[1])
    else:
        print(S[0])

=======
Suggestion 2

def main():
    s = input()
    if s[0] == s[1] and s[1] == s[2]:
        print(-1)
    else:
        if s[0] != s[1] and s[0] != s[2]:
            print(s[0])
        elif s[1] != s[2]:
            print(s[1])
        else:
            print(s[2])

=======
Suggestion 3

def main():
    s = input()
    for i in s:
        if s.count(i) == 1:
            print(i)
            break
    else:
        print(-1)

=======
Suggestion 4

def main():
    s = input()
    if len(s) == 3:
        if s[0] == s[1] and s[0] == s[2]:
            print(-1)
        elif s[0] == s[1]:
            print(s[2])
        elif s[0] == s[2]:
            print(s[1])
        elif s[1] == s[2]:
            print(s[0])
        else:
            print(s[0])
    else:
        print('Input must be a string of length 3')

=======
Suggestion 5

def main():
    s = input()
    if (s[0] == s[1]) and (s[0] == s[2]):
        print("-1")
    elif (s[0] == s[1]):
        print(s[2])
    elif (s[0] == s[2]):
        print(s[1])
    elif (s[1] == s[2]):
        print(s[0])
    else:
        print(s[0])

main()

=======
Suggestion 6

def main():
    s = input()
    for c in s:
        if s.count(c) == 1:
            print(c)
            exit()
    print(-1)

=======
Suggestion 7

def main():
    S = input()
    S = S.lower()
    S = sorted(S)
    if S[0] == S[1]:
        if S[1] == S[2]:
            print(-1)
        else:
            print(S[2])
    else:
        print(S[0])

=======
Suggestion 8

def main():
    s = input()
    for i in range(0, len(s)):
        print(s[i])
        print(s[0:i])
        print(s[i+1:len(s)])
        if s[i] not in s[0:i] and s[i] not in s[i+1:len(s)]:
            print(s[i])
            return
    print(-1)
    return

=======
Suggestion 9

def single_char(s):
    """Return the single character in 's' or -1 if no such character."""
    for c in s:
        if s.count(c) == 1:
            return c
    return -1

s = input()
print(single_char(s))

=======
Suggestion 10

def main():
    # Read the string from the standard input
    s = input()
    # Create a dictionary to count the number of occurrences
    # of each character
    dict = {}
    for c in s:
        if c in dict:
            dict[c] += 1
        else:
            dict[c] = 1
    # Look for a character that occurs only once
    for c in s:
        if dict[c] == 1:
            print(c)
            return
    # If we get here, no character occurs only once
    print(-1)
