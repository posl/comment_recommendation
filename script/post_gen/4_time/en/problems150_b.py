Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    s = input()
    count = 0
    for i in range(n-2):
        if s[i] == 'A' and s[i+1] == 'B' and s[i+2] == 'C':
            count += 1
    print(count)

main()

The solution is very simple. It is just a matter of counting the number of times ABC occurs in the string.

=======
Suggestion 2

def main():
    n = int(input())
    s = input()
    count = 0
    for i in range(n-2):
        if s[i:i+3] == 'ABC':
            count += 1
    print(count)

=======
Suggestion 3

def main():
    N = int(input())
    S = input()
    count = 0
    for i in range(N-2):
        if S[i:i+3] == "ABC":
            count += 1
    print(count)

=======
Suggestion 4

def main():
    n = int(input())
    s = input()
    ans = 0
    for i in range(n-2):
        if s[i:i+3] == 'ABC':
            ans += 1
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    S = input()
    cnt = 0
    for i in range(N-2):
        if S[i:i+3] == "ABC":
            cnt += 1
    print(cnt)

=======
Suggestion 6

def main():
    # put your code here
    n = int(input())
    s = input()
    count = 0
    for i in range(n-2):
        if s[i:i+3] == 'ABC':
            count += 1
    print(count)

=======
Suggestion 7

def countABC(s):
    count = 0
    for i in range(len(s)):
        if s[i] == 'A':
            if i+2 < len(s):
                if s[i+1] == 'B':
                    if s[i+2] == 'C':
                        count += 1
    return count

=======
Suggestion 8

def main():
    n = int(input())
    s = input()
    print(s.count('ABC'))

=======
Suggestion 9

def count_abc(s):
    return s.count('ABC')
