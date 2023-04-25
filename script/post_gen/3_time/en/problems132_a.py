Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    if (s[0]==s[1] and s[2]==s[3] and s[0]!=s[2]) or (s[0]==s[2] and s[1]==s[3] and s[0]!=s[1]) or (s[0]==s[3] and s[1]==s[2] and s[0]!=s[1]):
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    S = input()
    S = sorted(S)
    if S[0] == S[1] and S[2] == S[3] and S[0] != S[2]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    S = input()
    S = list(S)
    S.sort()
    if S[0] == S[1] and S[2] == S[3] and S[1] != S[2]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    S = input()
    if len(set(S)) != 2:
        print("No")
    elif S.count(S[0]) == 2:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    s = input()
    if len(set(s)) == 2:
        print("Yes")
    else:
        print("No")

main()

=======
Suggestion 6

def check(s):
    if len(s) != 4:
        return False
    if s[0] == s[1] == s[2] == s[3]:
        return False
    if s[0] == s[1] and s[2] == s[3]:
        return True
    if s[0] == s[2] and s[1] == s[3]:
        return True
    if s[0] == s[3] and s[1] == s[2]:
        return True
    return False

s = input()

=======
Suggestion 7

def main():
    s = input()
    if len(set(s)) == 2:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    s = input()
    if len(set(s)) == 2 and len(list(filter(lambda x: x == 2, [s.count(c) for c in set(s)]))) == 2:
        print('Yes')
    else:
        print('No')

=======
Suggestion 9

def main():
    # Read the input.
    s = input()
    # Count the number of each character.
    count = {}
    for c in s:
        if c in count:
            count[c] += 1
        else:
            count[c] = 1
    # Check the number of each character.
    # If the number of each character is 2, print Yes.
    # Otherwise, print No.
    if len(count) == 2 and 2 in count.values():
        print("Yes")
    else:
        print("No")
