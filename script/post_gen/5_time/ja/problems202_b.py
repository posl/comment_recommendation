Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S = input()
    S = S[::-1]
    S = S.replace('6', 'x')
    S = S.replace('9', '6')
    S = S.replace('x', '9')
    S = S.replace('0', 'x')
    S = S.replace('1', '0')
    S = S.replace('x', '1')
    print(S)

=======
Suggestion 2

def main():
    S = input()
    S = S[::-1]
    S = S.replace("6", "x")
    S = S.replace("9", "6")
    S = S.replace("x", "9")
    S = S.replace("0", "x")
    S = S.replace("1", "0")
    S = S.replace("x", "1")
    print(S)

=======
Suggestion 3

def reverse(text):
    return text[::-1]

=======
Suggestion 4

def main():
    S = input()
    S = S[::-1]
    ans = ''
    for i in range(len(S)):
        if S[i] == '6':
            ans += '9'
        elif S[i] == '9':
            ans += '6'
        else:
            ans += S[i]
    print(ans)

=======
Suggestion 5

def main():
    s = input()
    s = s[::-1]
    s = s.replace('6', 'x')
    s = s.replace('9', '6')
    s = s.replace('x', '9')
    s = s.replace('0', 'x')
    s = s.replace('1', '0')
    s = s.replace('x', '1')
    print(s)

=======
Suggestion 6

def main():
    s = input()
    s = s[::-1]
    s = s.replace('6', 'a')
    s = s.replace('9', '6')
    s = s.replace('a', '9')
    s = s.replace('0', 'a')
    s = s.replace('1', 'b')
    s = s.replace('8', '0')
    s = s.replace('b', '1')
    print(s)

=======
Suggestion 7

def main():
    S = input()
    S = S[::-1]
    S = S.replace('6','X')
    S = S.replace('9','6')
    S = S.replace('X','9')
    print(S)

=======
Suggestion 8

def main():
    S = input()
    S = S[::-1]

    for i in range(len(S)):
        if S[i] == "6":
            S = S[:i] + "9" + S[i+1:]
        elif S[i] == "9":
            S = S[:i] + "6" + S[i+1:]

    print(S)

=======
Suggestion 9

def main():
    S = input()
    s = S[::-1]
    ans = ""
    for i in range(len(s)):
        if s[i] == "0":
            ans += "0"
        elif s[i] == "1":
            ans += "1"
        elif s[i] == "6":
            ans += "9"
        elif s[i] == "8":
            ans += "8"
        elif s[i] == "9":
            ans += "6"
    print(ans)
