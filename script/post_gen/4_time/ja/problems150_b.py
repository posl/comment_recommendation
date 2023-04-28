Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    s = input()
    ans = 0
    for i in range(n-2):
        if s[i:i+3] == "ABC":
            ans += 1
    print(ans)

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
        if S[i:i+3] == "ABC":
            count += 1
    print(count)

=======
Suggestion 4

def main():
    N = int(input())
    S = input()
    count = 0
    for i in range(N-2):
        if S[i] == "A" and S[i+1] == "B" and S[i+2] == "C":
            count += 1
    print(count)

main()

=======
Suggestion 5

def main():
    N = int(input())
    S = input()
    count = 0
    for i in range(N-2):
        if S[i] == "A" and S[i+1] == "B" and S[i+2] == "C":
            count += 1
    print(count)

=======
Suggestion 6

def main():
    N = int(input())
    S = input()
    ans = 0
    for i in range(N-2):
        if S[i:i+3] == "ABC":
            ans += 1
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    s = input()
    ans = 0
    for i in range(n-2):
        if s[i]=="A" and s[i+1]=="B" and s[i+2]=="C":
            ans+=1
    print(ans)
