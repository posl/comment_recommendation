Synthesizing 10/10 solutions

=======
Suggestion 1

def problem202_b():
    s=input()
    s=s[::-1]
    s=s.replace('0','a')
    s=s.replace('1','b')
    s=s.replace('6','1')
    s=s.replace('8','2')
    s=s.replace('9','6')
    s=s.replace('a','0')
    s=s.replace('b','1')
    print(s)

problem202_b()

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

=======
Suggestion 3

def reverse(num):
    num = str(num)
    num = num[::-1]
    return num

=======
Suggestion 4

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
Suggestion 5

def reverseString(s):
    return s[::-1]

=======
Suggestion 6

def main():
    S = input()
    S = S[::-1]
    S = S.replace('6', 'T')
    S = S.replace('9', '6')
    S = S.replace('T', '9')
    S = S.replace('0', 'T')
    S = S.replace('1', '0')
    S = S.replace('T', '1')
    print(S)

=======
Suggestion 7

def main():
    # S = input()
    S = "0601889"
    # S = "86910"
    # S = "01010"
    S = list(S)
    S.reverse()
    for i in range(len(S)):
        if S[i] == "6":
            S[i] = "9"
        elif S[i] == "9":
            S[i] = "6"
    print("".join(S))

=======
Suggestion 8

def problem202_b():
    S = input()
    S = S[::-1]
    S = S.replace('0', 'a')
    S = S.replace('1', 'b')
    S = S.replace('6', '1')
    S = S.replace('9', '6')
    S = S.replace('8', '0')
    S = S.replace('a', '0')
    S = S.replace('b', '1')
    print(S)

=======
Suggestion 9

def main():
    s = input()
    s = s[::-1]
    s = s.replace("6", "x")
    s = s.replace("9", "6")
    s = s.replace("x", "9")
    s = s.replace("0", "x")
    s = s.replace("1", "0")
    s = s.replace("x", "1")
    print(s)

=======
Suggestion 10

def main():
    S = input()
    S = S[::-1]
    S = S.replace('6', 'a')
    S = S.replace('9', '6')
    S = S.replace('a', '9')
    S = S.replace('1', 'a')
    S = S.replace('0', '1')
    S = S.replace('a', '0')
    print(S)
