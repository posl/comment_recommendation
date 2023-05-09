Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    count = 0
    for i in range(len(s)):
        if s[i] == '+':
            count += 1
        else:
            count -= 1
    print(count)

=======
Suggestion 2

def main():
    S = input()
    ans = 0
    for i in range(4):
        if S[i] == '+':
            ans += 1
        else:
            ans -= 1
    print(ans)
    return 0

=======
Suggestion 3

def main():
    s = input()
    print(s.count('+') - s.count('-'))

=======
Suggestion 4

def main():
    s = input()
    print(s.count("+") - s.count("-"))

=======
Suggestion 5

def main():
    S = input()
    print(S.count("+") - S.count("-"))

=======
Suggestion 6

def main():
    #S = input()
    S = '----'
    print(S.count('+') - S.count('-'))

=======
Suggestion 7

def main():
    #S = input()
    S = '-+-+'
    print(S.count('+') - S.count('-'))
