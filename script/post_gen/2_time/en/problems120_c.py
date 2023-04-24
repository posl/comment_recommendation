Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    print(min(s.count('0'), s.count('1')) * 2)

main()

=======
Suggestion 2

def main():
    S = input()
    N = len(S)
    ans = 0
    for i in range(N):
        if S[i] == '0':
            ans += 1
        else:
            ans -= 1
    print(abs(ans))

=======
Suggestion 3

def main():
    S = input()
    print(min(S.count('0'), S.count('1')) * 2)

=======
Suggestion 4

def main():
    S = input()
    ans = 0
    for i in range(len(S)):
        if S[i] == '0':
            ans += 1
        else:
            ans -= 1
    print(abs(ans))

=======
Suggestion 5

def main():
    s = input()
    print(min(s.count("0"), s.count("1")) * 2)

=======
Suggestion 6

def main():
    S = input()
    print(S.count('0') * S.count('1'))

=======
Suggestion 7

def main():
    s = input()
    print(s.count('0') * s.count('1'))

=======
Suggestion 8

def main():
    # Write your code here
    s = input()
    print(min(s.count("0"), s.count("1")) * 2)
