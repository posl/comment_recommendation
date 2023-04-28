Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S = input()
    print(S[1] + S[2] + S[0])

=======
Suggestion 2

def main():
    s = input()
    print(s[1] + s[2] + s[0])

=======
Suggestion 3

def main():
    S = input()
    print(S[1:] + S[0])

=======
Suggestion 4

def main():
    s = input()
    print(s[1:]+s[0])

=======
Suggestion 5

def main():
    s = input()
    print(s[1:3] + s[0])

=======
Suggestion 6

def main():
    S = input()
    print(S[1:3]+S[0:1])

=======
Suggestion 7

def main():
    # Read input
    s = list(input())
    # Move the first character to the end
    s.append(s.pop(0))
    # Print result
    print(''.join(s))
