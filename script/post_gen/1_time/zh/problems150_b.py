Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    S = input()
    count = 0
    for i in range(N - 2):
        if S[i:i+3] == 'ABC':
            count += 1
    print(count)

=======
Suggestion 2

def count_abc(s):
    count = 0
    for i in range(len(s)-2):
        if s[i:i+3] == "ABC":
            count += 1
    return count

=======
Suggestion 3

def find_ABC(S):
    count = 0
    for i in range(len(S)-2):
        if S[i] == 'A' and S[i+1] == 'B' and S[i+2] == 'C':
            count += 1
    return count

=======
Suggestion 4

def abc(s):
    count = 0
    for i in range(len(s)):
        if s[i] == "A":
            for j in range(i+1,len(s)):
                if s[j] == "B":
                    for k in range(j+1,len(s)):
                        if s[k] == "C":
                            count += 1
    return count

=======
Suggestion 5

def main():
    n = int(input())
    s = input()
    count = 0
    for i in range(n-2):
        if s[i:i+3] == "ABC":
            count += 1
    print(count)

=======
Suggestion 6

def count_abc(s):
    count = 0
    for i in range(0,len(s)-2):
        if s[i:i+3] == 'ABC':
            count += 1
    return count

=======
Suggestion 7

def count_abc(s):
    count = 0
    for i in range(len(s)-2):
        if s[i:i+3] == 'ABC':
            count += 1
    return count

=======
Suggestion 8

def find_ABC(s):
    count = 0
    for i in range(0,len(s)-2):
        if s[i:i+3] == "ABC":
            count += 1
    return count

=======
Suggestion 9

def solve():
    n = int(input())
    s = input()
    count = 0
    for i in range(n-2):
        if s[i:i+3] == 'ABC':
            count += 1
    print(count)

solve()
