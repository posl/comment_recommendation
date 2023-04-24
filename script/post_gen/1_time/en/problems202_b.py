Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    S = S[::-1]
    S = S.replace('6', 'x')
    S = S.replace('9', '6')
    S = S.replace('x', '9')
    print(S)

=======
Suggestion 2

def rotate(s):
    s = s[::-1]
    s = s.replace('0', 'a')
    s = s.replace('1', 'b')
    s = s.replace('6', 'c')
    s = s.replace('8', 'd')
    s = s.replace('9', 'e')
    s = s.replace('a', '9')
    s = s.replace('b', '1')
    s = s.replace('c', '6')
    s = s.replace('d', '8')
    s = s.replace('e', '0')
    return s

=======
Suggestion 3

def main():
    S = input()
    S = S[::-1]
    S = S.replace("0","2")
    S = S.replace("1","0")
    S = S.replace("2","1")
    S = S.replace("6","9")
    S = S.replace("8","8")
    S = S.replace("9","6")
    print(S)

=======
Suggestion 4

def rotate(s):
    s = s[::-1]
    s = s.replace('0', 'x')
    s = s.replace('1', 'y')
    s = s.replace('6', '0')
    s = s.replace('9', '6')
    s = s.replace('x', '9')
    s = s.replace('y', '1')
    return s

s = input()
print(rotate(s))

=======
Suggestion 5

def main():
    S = input()
    S = S[::-1]
    S = S.replace("6","9")
    S = S.replace("9","6")
    print(S)

=======
Suggestion 6

def main():
    s = input()
    s = s[::-1]
    s = s.replace('0','t')
    s = s.replace('1','r')
    s = s.replace('6','y')
    s = s.replace('8','8')
    s = s.replace('9','6')
    s = s.replace('t','9')
    s = s.replace('r','1')
    s = s.replace('y','0')
    print(s)

=======
Suggestion 7

def main():
    print(input().translate(str.maketrans('01689', '61980'))[::-1])

=======
Suggestion 8

def main():
    s = input()
    s = s[::-1].replace("6", "9").replace("9", "6")
    print(s)

main()

=======
Suggestion 9

def rotate(s):
    return s[::-1].translate(str.maketrans('01689', '01986'))

=======
Suggestion 10

def rotate_180(s):
    #print(s)
    s = s[::-1]
    s = s.replace("0","x")
    s = s.replace("1","y")
    s = s.replace("6","0")
    s = s.replace("8","8")
    s = s.replace("9","6")
    s = s.replace("x","9")
    s = s.replace("y","1")
    return s

s = input()
print(rotate_180(s))
