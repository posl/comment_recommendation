Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    S = input()
    count = 0
    for i in range(N):
        if S[i:i+3] == "ABC":
            count += 1
    print(count)

=======
Suggestion 2

def main():
    N = int(input())
    S = input()
    ans = 0
    for i in range(N-2):
        if S[i:i+3] == 'ABC':
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    S = input()
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if S[i] == 'A' and S[j] == 'B' and S[k] == 'C':
                    count += 1
    print(count)

=======
Suggestion 4

def solve():
    N = int(input())
    S = input()
    ans = 0
    for i in range(N-2):
        if S[i:i+3] == "ABC":
            ans += 1
    print(ans)
    return 0

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
main()

=======
Suggestion 6

def main():
    N = int(input())
    S = input()
    print(S.count("ABC"))

=======
Suggestion 7

def main():
    N = int(input())
    S = input()
    count = 0
    for i in range(N-2):
        if S[i:i+3] == "ABC":
            count += 1
    print(count)

=======
Suggestion 8

def main():
    N = int(input())
    S = input()
    count = 0
    for i in range(N-2):
        if S[i:i+3] == 'ABC':
            count += 1
    print(count)
