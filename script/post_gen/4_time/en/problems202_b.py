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
    S = S.replace('6', 'x')
    S = S.replace('9', '6')
    S = S.replace('x', '9')
    print(S)

=======
Suggestion 3

def main():
    s = input()
    s = s[::-1]
    s = s.replace("0", "a")
    s = s.replace("1", "b")
    s = s.replace("6", "0")
    s = s.replace("8", "1")
    s = s.replace("9", "6")
    s = s.replace("a", "9")
    s = s.replace("b", "8")
    print(s)

=======
Suggestion 4

def main():
    S = input()
    S = S[::-1]
    S = S.replace('6','a')
    S = S.replace('9','6')
    S = S.replace('a','9')
    print(S)

=======
Suggestion 5

def main():
    s = input()
    s = s[::-1]
    s = s.replace("6", "a")
    s = s.replace("9", "6")
    s = s.replace("a", "9")
    s = s.replace("0", "0")
    s = s.replace("1", "1")
    s = s.replace("8", "8")
    print(s)

=======
Suggestion 6

def rotate(s):
    s = s[::-1]
    s = s.replace("0", "a")
    s = s.replace("1", "b")
    s = s.replace("6", "c")
    s = s.replace("8", "d")
    s = s.replace("9", "e")
    s = s.replace("a", "0")
    s = s.replace("b", "1")
    s = s.replace("c", "9")
    s = s.replace("d", "8")
    s = s.replace("e", "6")
    return s

=======
Suggestion 7

def rotate(s):
    s = s[::-1]
    s = s.replace("0","x")
    s = s.replace("1","y")
    s = s.replace("6","0")
    s = s.replace("8","8")
    s = s.replace("9","6")
    s = s.replace("x","0")
    s = s.replace("y","1")
    return s

s = input()
print(rotate(s))

=======
Suggestion 8

def solve(string):
    result = ""
    for i in range(len(string)-1,-1,-1):
        if string[i] == "6":
            result += "9"
        elif string[i] == "9":
            result += "6"
        else:
            result += string[i]
    return result

=======
Suggestion 9

def reverse(string):
    string = string[::-1]
    return string
