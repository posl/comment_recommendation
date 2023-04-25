Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    if s[0] != s[1] and s[0] != s[2]:
        print(s[0])
    elif s[1] != s[0] and s[1] != s[2]:
        print(s[1])
    elif s[2] != s[0] and s[2] != s[1]:
        print(s[2])
    else:
        print(-1)

=======
Suggestion 2

def main():
    s = raw_input()
    if s[0] != s[1] and s[0] != s[2]:
        print s[0]
    elif s[1] != s[0] and s[1] != s[2]:
        print s[1]
    elif s[2] != s[0] and s[2] != s[1]:
        print s[2]
    else:
        print -1

=======
Suggestion 3

def main():
    s = input()
    for c in s:
        if s.count(c) == 1:
            print(c)
            return
    print(-1)

main()

=======
Suggestion 4

def main():
    s = input()
    for c in s:
        if s.count(c) == 1:
            print(c)
            return
    print(-1)

=======
Suggestion 5

def main():
    s = input()
    for i in s:
        if s.count(i) == 1:
            print(i)
            return
    print(-1)
    return

=======
Suggestion 6

def main():
    s = input()
    print(-1 if len(set(s)) == 1 else [c for c in s if s.count(c) == 1][0])

main()

=======
Suggestion 7

def main():
    s = input()
    s1 = set(s)
    if len(s1) == 3:
        print(s[0])
    elif len(s1) == 2:
        print(list(s1 - set(s[0]))[0])
    else:
        print(-1)

=======
Suggestion 8

def main():
    # Read the string
    s = input()
    # If the string has only one character, print it
    if len(s) == 1:
        print(s)
    # If the string has two characters, print the one that is different
    elif len(s) == 2:
        if s[0] == s[1]:
            print(-1)
        else:
            print(s[0])
    # If the string has three characters, print the one that is different
    elif len(s) == 3:
        if s[0] == s[1] and s[0] == s[2]:
            print(-1)
        elif s[0] == s[1]:
            print(s[2])
        elif s[0] == s[2]:
            print(s[1])
        elif s[1] == s[2]:
            print(s[0])
    # If the string has more than three characters, print -1
    else:
        print(-1)

=======
Suggestion 9

def main():
    # Get the string from the user
    string = input()

    # Create a dictionary to hold the count of each character
    charCount = {}

    # Loop through the string and count the characters
    for char in string:
        if char in charCount:
            charCount[char] += 1
        else:
            charCount[char] = 1

    # Loop through the dictionary and print the first character that
    # only occurs once
    for char in charCount:
        if charCount[char] == 1:
            print(char)
            return

    # If we get here, then no character occurs once
    print(-1)

=======
Suggestion 10

def main():
    # Get the input
    s = input()

    # Get a list of characters
    chars = list(s)

    # Get a set of characters
    char_set = set(s)

    # Check if there is only one character
    if len(char_set) == 1:
        print("-1")
    else:
        # Loop through the characters
        for char in chars:
            # Check if the character is only in the string once
            if chars.count(char) == 1:
                print(char)
                break
