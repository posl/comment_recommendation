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

main()

=======
Suggestion 2

def main():
    s = input()
    d = {}
    for c in s:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    for c in s:
        if d[c] == 1:
            print(c)
            return
    print(-1)

=======
Suggestion 3

def main():
    S = input()
    if S[0] != S[1] and S[1] != S[2]:
        print(S[0])
    elif S[0] != S[1] and S[1] == S[2]:
        print(S[0])
    elif S[0] == S[1] and S[1] != S[2]:
        print(S[2])
    else:
        print(-1)

=======
Suggestion 4

def main():
    s = input()
    if len(s) == 3:
        if s[0] == s[1]:
            if s[0] == s[2]:
                print("-1")
            else:
                print(s[2])
        else:
            if s[0] == s[2]:
                print(s[1])
            else:
                print(s[0])
    else:
        print("-1")

=======
Suggestion 5

def main():
    s = input()
    for i in range(3):
        if s.count(s[i]) == 1:
            print(s[i])
            exit()
    print(-1)

=======
Suggestion 6

def main():
    s=input()
    for i in s:
        if s.count(i)==1:
            print(i)
            return
    print(-1)

=======
Suggestion 7

def find_unique(s):
    for c in s:
        if s.count(c) == 1:
            return c
    return -1

s = input()
print(find_unique(s))

=======
Suggestion 8

def main():
    S = input()
    S = S.lower()
    for i in S:
        if S.count(i) == 1:
            print(i)
            break
    else:
        print(-1)

=======
Suggestion 9

def main():
    s = input()
    if len(s) != 3:
        print("Input must be a string of length 3")
        return
    if s[0] == s[1] and s[1] == s[2]:
        print(-1)
        return
    elif s[0] == s[1]:
        print(s[2])
        return
    elif s[1] == s[2]:
        print(s[0])
        return
    elif s[0] == s[2]:
        print(s[1])
        return
    else:
        print(s[0])
        return

=======
Suggestion 10

def main():
    # Read in the input
    s = input()
    # Create a dictionary to store the character counts
    char_counts = {}
    # Loop through the characters in the string
    for c in s:
        # If the character is already in the dictionary
        if c in char_counts:
            # Increment the count
            char_counts[c] += 1
        # Otherwise, add it to the dictionary
        else:
            char_counts[c] = 1
    # Loop through the dictionary
    for c in char_counts:
        # If the count is 1, print the character
        if char_counts[c] == 1:
            print(c)
            # Exit the function
            return
    # If we get here, no character occurred only once
    print(-1)
