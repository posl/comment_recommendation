Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    s = input()
    print(s.count('ABC'))

=======
Suggestion 2

def count_ABC(s):
    cnt = 0
    for i in range(len(s)-2):
        if s[i:i+3] == "ABC":
            cnt += 1
    return cnt

=======
Suggestion 3

def main():
    N = int(input())
    S = input()
    cnt = 0
    for i in range(N-2):
        if S[i] == "A" and S[i+1] == "B" and S[i+2] == "C":
            cnt += 1
    print(cnt)

=======
Suggestion 4

def count_abc(s):
    count = 0
    for i in range(len(s)-2):
        if s[i:i+3] == 'ABC':
            count += 1
    return count

=======
Suggestion 5

def judge_abc(s):
    if s == "ABC":
        return True
    else:
        return False

=======
Suggestion 6

def countABC(s):
    count = 0
    for i in range(len(s)-2):
        if s[i] == 'A' and s[i+1] == 'B' and s[i+2] == 'C':
            count += 1
    return count

=======
Suggestion 7

def main():
    N = int(input())
    S = input()
    count = 0
    for i in range(N-2):
        if S[i:i+3] == 'ABC':
            count += 1
    print(count)

=======
Suggestion 8

def countABC(S):
    count = 0
    for i in range(0, len(S) - 2):
        if S[i] == 'A' and S[i + 1] == 'B' and S[i + 2] == 'C':
            count += 1
    return count

=======
Suggestion 9

def main():
    n = int(input())
    s = input()
    count = 0
    for i in range(n-2):
        if s[i] == 'A' and s[i+1] == 'B' and s[i+2] == 'C':
            count += 1
    print(count)

=======
Suggestion 10

def main():
    n = int(input())
    s = input()
    count = 0
    for i in range(0, n - 2):
        if s[i] == "A" and s[i + 1] == "B" and s[i + 2] == "C":
            count += 1
    print(count)
