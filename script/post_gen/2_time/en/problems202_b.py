Synthesizing 10/10 solutions

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
    s = s.replace("6", "x")
    s = s.replace("9", "6")
    s = s.replace("x", "9")
    print(s)

=======
Suggestion 4

def main():
    # input
    S = input()

    # compute

    # output
    print(S[::-1].translate(str.maketrans({'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'})))

=======
Suggestion 5

def rotate180(s):
    s = s[::-1]
    s = s.replace('6', 'x')
    s = s.replace('9', '6')
    s = s.replace('x', '9')
    return s

s = input()
print(rotate180(s))

=======
Suggestion 6

def rotate(s):
    reverse = s[::-1]
    result = ''
    for i in reverse:
        if i == '0':
            result += '0'
        elif i == '1':
            result += '1'
        elif i == '6':
            result += '9'
        elif i == '8':
            result += '8'
        elif i == '9':
            result += '6'
    return result

=======
Suggestion 7

def rotate180(s):
    s = s[::-1]
    s = s.replace('0','2')
    s = s.replace('1','3')
    s = s.replace('2','0')
    s = s.replace('3','1')
    s = s.replace('6','4')
    s = s.replace('8','5')
    s = s.replace('9','6')
    s = s.replace('4','8')
    s = s.replace('5','9')
    s = s.replace('7','7')
    return s

s = input()
print(rotate180(s))

=======
Suggestion 8

def rotate_string(s):
    #reverse string
    s = s[::-1]
    #replace 6 with 9 and vice versa
    s = s.replace("6", "2")
    s = s.replace("9", "6")
    s = s.replace("2", "9")
    return s

s = input()
print(rotate_string(s))

=======
Suggestion 9

def rotate(s):
    s = s[::-1]
    return s.translate(str.maketrans("01689","01986"))

print(rotate(input()))

=======
Suggestion 10

def reverse_string(s):
    return s[::-1]
