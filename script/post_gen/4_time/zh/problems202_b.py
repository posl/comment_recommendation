Synthesizing 10/10 solutions

=======
Suggestion 1

def rotate(s):
    return s[::-1]

=======
Suggestion 2

def solve():
    S = input()
    S = S[::-1]
    S = S.replace('0', 'a')
    S = S.replace('1', 'b')
    S = S.replace('6', '1')
    S = S.replace('8', '2')
    S = S.replace('9', '6')
    S = S.replace('a', '0')
    S = S.replace('b', '1')
    print(S)

=======
Suggestion 3

def main():
    # 输入
    S = input()
    # 反转
    S = S[::-1]
    # 替换
    S = S.replace('6', 't')
    S = S.replace('9', '6')
    S = S.replace('t', '9')
    S = S.replace('0', 't')
    S = S.replace('1', '0')
    S = S.replace('t', '1')
    # 输出
    print(S)

=======
Suggestion 4

def reverse_str(s):
    return s[::-1]

=======
Suggestion 5

def main():
    S = input()
    S = S[::-1]
    S = S.replace('6','a')
    S = S.replace('9','6')
    S = S.replace('a','9')
    S = S.replace('1','a')
    S = S.replace('0','1')
    S = S.replace('a','0')
    print(S)

main()

=======
Suggestion 6

def main():
    s = input()
    s = s[::-1]
    s = s.replace('6', 't')
    s = s.replace('9', '6')
    s = s.replace('t', '9')
    s = s.replace('1', 't')
    s = s.replace('0', '1')
    s = s.replace('t', '0')
    print(s)

=======
Suggestion 7

def main():
    S = input()
    S = S[::-1]
    S = S.replace("6","a")
    S = S.replace("9","6")
    S = S.replace("a","9")
    S = S.replace("0","a")
    S = S.replace("1","b")
    S = S.replace("a","1")
    S = S.replace("b","0")
    print(S)

=======
Suggestion 8

def rotate_180(S):
    S = S[::-1]
    S = S.replace('0', 'x')
    S = S.replace('1', '0')
    S = S.replace('x', '1')
    S = S.replace('6', 'x')
    S = S.replace('9', '6')
    S = S.replace('x', '9')
    return S

print(rotate_180('0601889'))
print(rotate_180('86910'))
print(rotate_180('01010'))

=======
Suggestion 9

def main():
    S = input()
    S = S[::-1]
    S = S.replace('6','a')
    S = S.replace('9','6')
    S = S.replace('a','9')
    S = S.replace('0','a')
    S = S.replace('1','b')
    S = S.replace('a','1')
    S = S.replace('b','0')
    print(S)

=======
Suggestion 10

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
main()
