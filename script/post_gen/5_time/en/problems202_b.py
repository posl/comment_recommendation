Synthesizing 8/10 solutions

=======
Suggestion 1

def main():
    s = input()
    s = s[::-1]
    s = s.replace('0', 'x')
    s = s.replace('1', '0')
    s = s.replace('x', '1')
    s = s.replace('6', 'x')
    s = s.replace('9', '6')
    s = s.replace('x', '9')
    print(s)

=======
Suggestion 2

def main():
    S = input()
    S = S[::-1]
    S = S.replace('0','a')
    S = S.replace('1','b')
    S = S.replace('6','1')
    S = S.replace('8','2')
    S = S.replace('9','6')
    S = S.replace('a','0')
    S = S.replace('b','1')
    print(S)

=======
Suggestion 3

def main():
    s = input()
    s = s[::-1]
    s = s.replace("0", "2")
    s = s.replace("1", "3")
    s = s.replace("2", "0")
    s = s.replace("3", "1")
    s = s.replace("6", "4")
    s = s.replace("7", "5")
    s = s.replace("8", "6")
    s = s.replace("9", "7")
    s = s.replace("4", "8")
    s = s.replace("5", "9")
    print(s)

=======
Suggestion 4

def rotate180(s):
    s = s[::-1]
    s = s.replace('0', 'x')
    s = s.replace('1', 'y')
    s = s.replace('6', 'z')
    s = s.replace('8', '0')
    s = s.replace('9', '1')
    s = s.replace('x', '0')
    s = s.replace('y', '1')
    s = s.replace('z', '6')
    return s

s = input()
print(rotate180(s))

=======
Suggestion 5

def rotate(string):
    reversed = string[::-1]
    rotated = ""
    for char in reversed:
        if char == "6":
            rotated += "9"
        elif char == "9":
            rotated += "6"
        else:
            rotated += char
    return rotated

=======
Suggestion 6

def rotate(string):
    string = string[::-1]
    string = string.replace('6','a')
    string = string.replace('9','6')
    string = string.replace('a','9')
    return string

=======
Suggestion 7

def rotate_string(str):
    str = str[::-1]
    str = str.replace("0", "a")
    str = str.replace("1", "b")
    str = str.replace("6", "0")
    str = str.replace("9", "1")
    str = str.replace("a", "6")
    str = str.replace("b", "9")
    return str

=======
Suggestion 8

def reverse_string(string):
    return string[::-1]
