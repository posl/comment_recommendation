Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    s = s[::-1]
    s = s.replace('6', 'x')
    s = s.replace('9', '6')
    s = s.replace('x', '9')
    print(s)

=======
Suggestion 2

def main():
    S = input()
    S = S[::-1]
    S = S.replace("6", "x")
    S = S.replace("9", "6")
    S = S.replace("x", "9")
    print(S)

=======
Suggestion 3

def main():
    s = input()
    s = s[::-1]
    s = s.replace("6", "a")
    s = s.replace("9", "6")
    s = s.replace("a", "9")
    print(s)

=======
Suggestion 4

def main():
    S = input()
    S = S[::-1]
    S = S.replace("0", "a")
    S = S.replace("1", "b")
    S = S.replace("6", "1")
    S = S.replace("8", "2")
    S = S.replace("9", "6")
    S = S.replace("a", "0")
    S = S.replace("b", "1")
    print(S)

=======
Suggestion 5

def rotate(s):
    s = s[::-1]
    s = s.replace('6','a')
    s = s.replace('9','6')
    s = s.replace('a','9')
    return s

s = input()
print(rotate(s))

=======
Suggestion 6

def rotate(n):
    n = n[::-1]
    n = n.replace('0', 'a')
    n = n.replace('1', 'b')
    n = n.replace('6', 'c')
    n = n.replace('8', 'd')
    n = n.replace('9', 'e')
    n = n.replace('a', '0')
    n = n.replace('b', '1')
    n = n.replace('c', '9')
    n = n.replace('d', '8')
    n = n.replace('e', '6')
    return n

=======
Suggestion 7

def main():
    S = input()

    S = S[::-1]
    S = S.replace('6','x')
    S = S.replace('9','6')
    S = S.replace('x','9')

    print(S)

=======
Suggestion 8

def rotate(string):
    string = string[::-1]
    string = string.replace('0','*')
    string = string.replace('1','0')
    string = string.replace('*','1')
    string = string.replace('6','*')
    string = string.replace('8','6')
    string = string.replace('*','8')
    string = string.replace('9','*')
    string = string.replace('0','9')
    string = string.replace('*','0')
    return string

string = input()
print(rotate(string))

=======
Suggestion 9

def rev(s):
    return s[::-1]
