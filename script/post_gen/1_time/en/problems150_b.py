Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    s = input()
    count = 0
    for i in range(n-2):
        if s[i:i+3] == 'ABC':
            count += 1
    print(count)

=======
Suggestion 2

def main():
    n = int(input())
    s = input()
    count = 0
    for i in range(n-2):
        if s[i:i+3] == "ABC":
            count += 1
    print(count)

=======
Suggestion 3

def main():
    N = int(input())
    S = input()
    count = 0
    for i in range(N-2):
        if S[i:i+3] == 'ABC':
            count += 1
    print(count)

=======
Suggestion 4

def main():
    n = int(input())
    s = input()
    cnt = 0
    for i in range(n-2):
        if s[i] == 'A' and s[i+1] == 'B' and s[i+2] == 'C':
            cnt += 1
    print(cnt)

=======
Suggestion 5

def main():
    n = int(input())
    s = input()
    count = 0
    for i in range(n-2):
        if s[i:i+3] == 'ABC':
            count += 1
    print(count)
    return 0

=======
Suggestion 6

def main():
    n = int(input())
    s = input()
    ans = 0
    for i in range(n - 2):
        if s[i:i+3] == 'ABC':
            ans += 1
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    s = input()
    count = 0
    for i in range(n):
        if s[i:i+3] == "ABC":
            count += 1
    print(count)

=======
Suggestion 8

def main():
    #write your code here
    n = int(input())
    s = input()
    count = 0
    for i in range(n-2):
        if s[i:i+3] == "ABC":
            count += 1
    print(count)

=======
Suggestion 9

def main():
    n = int(input())
    s = input()
    print(s.count('ABC'))
