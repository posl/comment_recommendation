Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    S = input()
    count = 0
    for i in range(N-2):
        if S[i:i+3] == "ABC":
            count += 1
    print(count)

=======
Suggestion 2

def main():
    N = int(input())
    S = input()
    count = 0
    for i in range(N-2):
        if S[i] == "A" and S[i+1] == "B" and S[i+2] == "C":
            count += 1
    print(count)

=======
Suggestion 3

def main():
    n = int(input())
    s = input()
    cnt = 0
    for i in range(n-2):
        if s[i] == "A" and s[i+1] == "B" and s[i+2] == "C":
            cnt += 1
    print(cnt)

=======
Suggestion 4

def main():
    N = int(input())
    S = input()
    cnt = 0
    for i in range(N-2):
        if S[i] == "A" and S[i+1] == "B" and S[i+2] == "C":
            cnt += 1
    print(cnt)

=======
Suggestion 5

def main():
    n = int(input())
    s = input()
    c = 0
    for i in range(n-2):
        if s[i] == 'A' and s[i+1] == 'B' and s[i+2] == 'C':
            c += 1
    print(c)

=======
Suggestion 6

def main():
    n = int(input())
    s = input()
    c = 0
    for i in range(n-2):
        if s[i:i+3] == "ABC":
            c += 1
    print(c)

=======
Suggestion 7

def main():
    N = int(input())
    S = input()
    count = 0
    for i in range(0, N-2):
        if S[i] == 'A' and S[i+1] == 'B' and S[i+2] == 'C':
            count += 1
    print(count)

=======
Suggestion 8

def main():
    N = int(input())
    S = input()
    count = 0
    for i in range(0, N-2):
        if S[i] == "A" and S[i+1] == "B" and S[i+2] == "C":
            count += 1
    print(count)

=======
Suggestion 9

def countABC(s):
    count = 0
    for i in range(len(s)-2):
        if s[i:i+3] == "ABC":
            count += 1
    return count

=======
Suggestion 10

def main():
    # Read the data
    n = int(input())
    s = input()
    # Count the number of occurrences of ABC
    count = 0
    for i in range(n-2):
        if s[i:i+3] == 'ABC':
            count += 1
    # Print the result
    print(count)
