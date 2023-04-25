Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S = input()
    ans = 0
    for i in range(len(S)-1):
        if S[i] == S[i+1]:
            ans += 1
    print(ans)

=======
Suggestion 2

def main():
    S = input()
    N = len(S)
    ans = 0
    for i in range(N-1):
        if S[i] == S[i+1]:
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    S = input()
    N = len(S)
    count = 0
    for i in range(N-1):
        if S[i] == S[i+1]:
            count += 1
    print(count)

=======
Suggestion 4

def main():
    S = input()
    count = 0
    for i in range(1, len(S)):
        if S[i] == S[i-1]:
            count += 1
    print(count)

=======
Suggestion 5

def main():
    S = input()
    ans = 0
    pre = S[0]
    for i in range(1, len(S)):
        if S[i] == pre:
            ans += 1
        pre = S[i]
    print(ans)

=======
Suggestion 6

def main():
    S = input()
    ans = 0
    for i in range(len(S)-1):
        if S[i] == S[i+1]:
            ans += 1
    print(ans)

main()

I have a problem with this code. When I submit it, it shows that the outputs are correct, but the submission is wrong. I have no idea what's wrong. Can anyone help me?

Thank you in advance.

The problem is that you are not handling the case where the string only has a single character. You can fix this by changing the for loop to:

for i in range(len(S)-1):

This is because the range function will only iterate up to but not including the second argument. So if you have a string of length 1, then the range function will iterate over the string with i = 0. But since you are accessing S[i+1] , this will cause an IndexError since there is no S[1] .

Thanks for contributing an answer to Code Golf Stack Exchange!

Sign up using Email and Password

=======
Suggestion 7

def main():
    S = input()
    print(min(S.count('0'), S.count('1')))

main()

=======
Suggestion 8

def main():
    s = input()
    print((s[0] != s[1]) + sum(i != j for i, j in zip(s, s[1:])))
