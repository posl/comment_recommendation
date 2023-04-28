Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

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
Suggestion 2

def main():
    S = input()
    S = S[::-1]
    S = S.replace('6','x')
    S = S.replace('9','6')
    S = S.replace('x','9')
    S = S.replace('0','x')
    S = S.replace('1','0')
    S = S.replace('x','1')
    print(S)
main()

=======
Suggestion 3

def main():
    s = input()
    ans = ''
    for i in range(len(s)):
        if s[i] == '0':
            ans = '0' + ans
        elif s[i] == '1':
            ans = '1' + ans
        elif s[i] == '6':
            ans = '9' + ans
        elif s[i] == '8':
            ans = '8' + ans
        elif s[i] == '9':
            ans = '6' + ans
    print(ans)

=======
Suggestion 4

def main():
    s = input()
    s = s[::-1]
    s = s.replace('6', 't')
    s = s.replace('9', '6')
    s = s.replace('t', '9')
    s = s.replace('0', 't')
    s = s.replace('1', '0')
    s = s.replace('t', '1')
    print(s)

=======
Suggestion 5

def main():
    S = input()
    S = list(S)
    for i in range(len(S)):
        if S[i] == '0':
            S[i] = '0'
        elif S[i] == '1':
            S[i] = '1'
        elif S[i] == '6':
            S[i] = '9'
        elif S[i] == '8':
            S[i] = '8'
        elif S[i] == '9':
            S[i] = '6'
    S.reverse()
    print(''.join(S))

=======
Suggestion 6

def main():
    S = input()
    S = S[::-1]
    S = S.replace("6", "a")
    S = S.replace("9", "6")
    S = S.replace("a", "9")
    S = S.replace("0", "a")
    S = S.replace("1", "0")
    S = S.replace("a", "1")
    print(S)

=======
Suggestion 7

def main():
    s = input()
    ans = ""
    for i in range(len(s)):
        if s[i] == '6':
            ans = '9' + ans
        elif s[i] == '9':
            ans = '6' + ans
        else:
            ans = s[i] + ans
    print(ans)

=======
Suggestion 8

def main():
    # input
    S = input()

    # compute

    # output
    print(S[::-1].translate(str.maketrans('01689', '01986')))

=======
Suggestion 9

def main():
    s = input()
    ans = ''
    for i in range(len(s)):
        ans += s[len(s)-1-i]
    ans = ans.replace('6', 'x')
    ans = ans.replace('9', '6')
    ans = ans.replace('x', '9')
    ans = ans.replace('0', 'x')
    ans = ans.replace('1', '0')
    ans = ans.replace('x', '1')
    print(ans)
