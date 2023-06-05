Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    print(s.count("wv"))

=======
Suggestion 2

def problems279_a():
    s = input()
    count = 0
    for i in range(len(s)):
        if s[i] == "w":
            count += 1
    print(count * 2)

=======
Suggestion 3

def main():
    s = input()
    print(s.count('wv'))

=======
Suggestion 4

def count_underscores(S):
    count = 0
    for i in range(0, len(S)-1):
        if S[i] == 'v' and S[i+1] == 'w':
            count += 1
    return count

S = input()
print(count_underscores(S))

=======
Suggestion 5

def main():
    s = input()
    print(s.count('vv'))

=======
Suggestion 6

def count_bottoms(s):
    count = 0
    for i in range(len(s)-1):
        if s[i] == 'v' and s[i+1] == 'w':
            count += 1
    return count

=======
Suggestion 7

def count_bottoms(s):
    count = 0
    for i in range(len(s)):
        if s[i] == 'w':
            count += len(s) - i
    return count
