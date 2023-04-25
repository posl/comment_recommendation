Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S = input()
    T = input()
    ans = 0
    for i in range(3):
        if S[i] == T[i]:
            ans += 1
    print(ans)

=======
Suggestion 2

def main():
    s = input()
    t = input()
    ans = 0
    for i in range(3):
        if s[i] == t[i]:
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    s = input()
    t = input()
    cnt = 0
    for i in range(3):
        if s[i] == t[i]:
            cnt += 1
    print(cnt)

=======
Suggestion 4

def main():
    S = input()
    T = input()
    ans = 0
    for i in range(len(S)):
        if S[i] == T[i]:
            ans += 1
    print(ans)

=======
Suggestion 5

def main():
    #input
    S = input()
    T = input()

    #compute
    ans = 0
    for i in range(3):
        if S[i] == T[i]:
            ans += 1

    #output
    print(ans)

=======
Suggestion 6

def main():
    s = input()
    t = input()
    print(sum([1 for i in range(3) if s[i] == t[i]]))

main()

=======
Suggestion 7

def main():
    S = input()
    T = input()
    print(sum([1 for i in range(3) if S[i] == T[i]]))

=======
Suggestion 8

def main():
    S = input()
    T = input()
    ans = 0
    for i in range(3):
        if S[i] == T[i]:
            ans += 1
    print(ans)

main()

Problem Statement

You will be given a string S of length 3 representing the weather forecast for three days in the past.

The i-th character (1 ≦ i ≦ 3) of S represents the forecast for the i-th day. S, C, and R stand for sunny, cloudy, and rainy, respectively.

You will also be given a string T of length 3 representing the actual weather on those three days.

The i-th character (1 ≦ i ≦ 3) of S represents the actual weather on the i-th day. S, C, and R stand for sunny, cloudy, and rainy, respectively.

Print the number of days for which the forecast was correct.

Constraints

S and T are strings of length 3 each.

S and T consist of S, C, and R.

Input

Input is given from Standard Input in the following format:

S
T

Output

Print the number of days for which the forecast was correct.

Sample Input 1

CSS
CSR

Sample Output 1

2

For the first day, it was forecast to be cloudy, and it was indeed cloudy.
For the second day, it was forecast to be sunny, and it was indeed sunny.
For the third day, it was forecast to be sunny, but it was rainy.
Thus, the forecast was correct for two days in this case.

Sample Input 2

SSR
SSR

Sample Output 2

3

Sample Input 3

RRR
SSS

Sample Output 3

0
