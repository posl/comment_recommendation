Synthesizing 10/10 solutions (Duplicates hidden)

=======

def main():
    s = input()
    ans = 0
    for i in range(4):
        if s[i] == '+':
            ans += 1
        else:
            ans -= 1
    print(ans)

=======

def main():
    s = input()
    ans = 0
    for i in range(len(s)):
        if s[i] == "+":
            ans += 1
        else:
            ans -= 1
    print(ans)

=======

def main():
    S = input()
    ans = 0
    for i in range(len(S)):
        if S[i] == "+":
            ans += 1
        else:
            ans -= 1
    print(ans)

=======

def main():
    S = input()
    ans = 0
    for i in range(4):
        if S[i] == '+':
            ans += 1
        else:
            ans -= 1
    print(ans)

=======

def main():
    s = input()
    ans = 0
    for i in s:
        if i == '+':
            ans += 1
        else:
            ans -= 1
    print(ans)

=======

def main():
    S = input()
    cnt = 0
    for i in S:
        if i == '+':
            cnt += 1
        elif i == '-':
            cnt -= 1
    print(cnt)

=======

def main():
    S = input()
    print(S.count('+') - S.count('-'))

=======

def main():
    S = input()
    print(S.count("+") - S.count("-"))

=======

def main():
    s = input()
    print(s.count("+") - s.count("-"))
