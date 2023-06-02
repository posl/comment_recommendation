Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    s = s[::-1]
    s = s.replace("6", "x")
    s = s.replace("9", "6")
    s = s.replace("x", "9")
    s = s.replace("1", "x")
    s = s.replace("0", "1")
    s = s.replace("x", "0")
    print(s)

=======
Suggestion 2

def main():
    S = input()
    S = S[::-1]
    S = S.replace('0', 'x')
    S = S.replace('1', '0')
    S = S.replace('x', '1')
    S = S.replace('6', 'x')
    S = S.replace('9', '6')
    S = S.replace('x', '9')
    print(S)

=======
Suggestion 3

def main():
    S = input()
    S = S[::-1]
    S = S.replace('6', 'x')
    S = S.replace('9', '6')
    S = S.replace('x', '9')
    S = S.replace('8', 'x')
    S = S.replace('1', 'x')
    S = S.replace('0', '1')
    S = S.replace('x', '0')
    print(S)

=======
Suggestion 4

def main():
    S = input()
    S = S[::-1]
    S = S.replace("6","a")
    S = S.replace("9","6")
    S = S.replace("a","9")
    S = S.replace("1","a")
    S = S.replace("0","1")
    S = S.replace("a","0")
    print(S)

=======
Suggestion 5

def main():
    s = input()
    s = s[::-1]
    s = s.replace('6', 'a')
    s = s.replace('9', '6')
    s = s.replace('a', '9')
    s = s.replace('0', 'a')
    s = s.replace('1', '0')
    s = s.replace('a', '1')
    print(s)

=======
Suggestion 6

def main():
    S = input()
    S = S[::-1]
    for i in range(len(S)):
        if S[i] == '9':
            S = S[:i] + '6' + S[i+1:]
        elif S[i] == '6':
            S = S[:i] + '9' + S[i+1:]
    S = S.replace('0', 'a')
    S = S.replace('1', 'b')
    S = S.replace('9', '0')
    S = S.replace('8', '1')
    S = S.replace('6', '9')
    S = S.replace('a', '0')
    S = S.replace('b', '1')
    print(S)

=======
Suggestion 7

def main():
    S = input()
    S = S[::-1]
    S = S.replace('0', 'a')
    S = S.replace('1', 'b')
    S = S.replace('6', 'c')
    S = S.replace('8', 'd')
    S = S.replace('9', 'e')
    S = S.replace('a', '1')
    S = S.replace('b', '0')
    S = S.replace('c', '9')
    S = S.replace('d', '8')
    S = S.replace('e', '6')
    print(S)

=======
Suggestion 8

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
Suggestion 9

def main():
    s = input()
    s = s[::-1]
    s = s.replace('6','x')
    s = s.replace('9','6')
    s = s.replace('x','9')
    s = s.replace('0','x')
    s = s.replace('1','0')
    s = s.replace('x','1')
    print(s)

=======
Suggestion 10

def main():
    # input
    s = input()

    # compute
    s = s[::-1]
    s = s.replace('6', 'x')
    s = s.replace('9', '6')
    s = s.replace('x', '9')

    # output
    print(s)
