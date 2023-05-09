Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S = input()
    T = input()
    count = 0
    for i in range(3):
        if S[i] == T[i]:
            count += 1
    print(count)

=======
Suggestion 2

def main():
    s = input()
    t = input()
    count = 0
    for i in range(3):
        if s[i] == t[i]:
            count += 1
    print(count)

=======
Suggestion 3

def main():
    S = input()
    T = input()
    result = 0
    for i in range(3):
        if S[i] == T[i]:
            result += 1
    print(result)

=======
Suggestion 4

def main():
    s = input()
    t = input()

    count = 0
    for i in range(0, 3):
        if s[i] == t[i]:
            count += 1

    print(count)

=======
Suggestion 5

def main():
    # Read from standard input
    s = input()
    t = input()

    # Initialize the counter
    count = 0

    # Loop through the strings
    for i in range(len(s)):
        if s[i] == t[i]:
            count += 1

    # Print the result
    print(count)
