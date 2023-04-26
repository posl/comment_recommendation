Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = list(input())
    s.reverse()
    for i in range(len(s)):
        if s[i] == "6":
            s[i] = "9"
        elif s[i] == "9":
            s[i] = "6"
    print("".join(s))

=======
Suggestion 2

def main():
    s = input()
    ans = ''
    for i in s:
        if i == '6':
            ans += '9'
        elif i == '9':
            ans += '6'
        else:
            ans += i
    print(ans[::-1])

=======
Suggestion 3

def main():
    S = input()
    S = S[::-1]
    S = S.replace('0', 'a')
    S = S.replace('1', 'b')
    S = S.replace('6', 'c')
    S = S.replace('8', 'd')
    S = S.replace('9', 'e')
    S = S.replace('a', '9')
    S = S.replace('b', '1')
    S = S.replace('c', '6')
    S = S.replace('d', '8')
    S = S.replace('e', '0')
    print(S)

=======
Suggestion 4

def main():
    s = input()
    s = s[::-1]
    s = s.replace('0','a')
    s = s.replace('1','b')
    s = s.replace('6','c')
    s = s.replace('8','d')
    s = s.replace('9','e')
    s = s.replace('a','9')
    s = s.replace('b','1')
    s = s.replace('c','6')
    s = s.replace('d','8')
    s = s.replace('e','0')
    print(s)

=======
Suggestion 5

def main():
    s = input()
    s = s[::-1]
    s = s.replace('6', 'x')
    s = s.replace('9', '6')
    s = s.replace('x', '9')
    print(s)

=======
Suggestion 6

def main():
    s = input()
    s = s[::-1]
    s = s.replace('6', 'a')
    s = s.replace('9', '6')
    s = s.replace('a', '9')
    print(s)

=======
Suggestion 7

def main():
    S = input()
    S = S[::-1]
    S = S.replace("6", "x")
    S = S.replace("9", "6")
    S = S.replace("x", "9")
    print(S)
