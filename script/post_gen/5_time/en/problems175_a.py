Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    if S[0] == S[1] == S[2]:
        print(0)
    elif S[0] == S[1] or S[1] == S[2]:
        print(1)
    else:
        print(2)

=======
Suggestion 2

def main():
    s = input()
    count = 0
    max = 0
    for i in range(len(s)):
        if s[i] == 'R':
            count += 1
        else:
            count = 0
        if count > max:
            max = count
    print(max)

=======
Suggestion 3

def main():
    S = input()
    count = 0
    max_count = 0
    for i in range(len(S)):
        if S[i] == 'R':
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0
    print(max_count)

=======
Suggestion 4

def main():
    S = input()
    count = 0
    max_count = 0
    for i in range(3):
        if S[i] == "R":
            count += 1
            if max_count < count:
                max_count = count
        else:
            count = 0
    print(max_count)

=======
Suggestion 5

def main():
    s = input()
    if s[0] == s[1] == s[2]:
        print(3)
    elif s[0] == s[1] != s[2] or s[0] != s[1] == s[2]:
        print(2)
    else:
        print(1)

=======
Suggestion 6

def main():
    S = input()
    count = 0
    max_count = 0
    for i in range(0, 3):
        if S[i] == 'R':
            count += 1
        else:
            count = 0
        if count > max_count:
            max_count = count
    print(max_count)

=======
Suggestion 7

def solution():
    S = input()
    if S[0] == S[1] and S[1] == S[2]:
        print(1)
    elif S[0] == S[1] or S[1] == S[2]:
        print(2)
    else:
        print(0)

solution()

=======
Suggestion 8

def solve():
    #import sys
    #input = sys.stdin.readline
    s = input()
    print(s.count("R"))

=======
Suggestion 9

def main():
    S = input()
    print(S.count('R'))

=======
Suggestion 10

def main():
    # Take input
    s = input()

    # Initialize variables
    max_streak = 0
    streak = 0

    # Compute the streak
    for i in range(3):
        if s[i] == "R":
            streak += 1
        else:
            streak = 0

        if streak > max_streak:
            max_streak = streak

    # Print the result
    print(max_streak)
