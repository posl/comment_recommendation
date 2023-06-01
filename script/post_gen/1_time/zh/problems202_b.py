Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    s = s[::-1]
    s = s.replace("6","x")
    s = s.replace("9","6")
    s = s.replace("x","9")
    s = s.replace("0","x")
    s = s.replace("1","0")
    s = s.replace("x","1")
    print(s)

=======
Suggestion 2

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
Suggestion 3

def reverse(n):
    return n[::-1]

=======
Suggestion 4

def main():
    # 获取输入内容
    str = input()
    # 旋转180度后的数字
    str180 = ""
    # 旋转180度后的数字
    str180 = str[::-1]
    # 旋转180度后的数字
    str180 = str180.replace("0", "a")
    str180 = str180.replace("1", "b")
    str180 = str180.replace("6", "c")
    str180 = str180.replace("8", "d")
    str180 = str180.replace("9", "e")
    str180 = str180.replace("a", "1")
    str180 = str180.replace("b", "0")
    str180 = str180.replace("c", "9")
    str180 = str180.replace("d", "8")
    str180 = str180.replace("e", "6")
    # 输出旋转180度后的数字
    print(str180)

=======
Suggestion 5

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
Suggestion 6

def main():
    s = input()
    s = s[::-1]
    s = s.replace('6', 'a')
    s = s.replace('9', 'b')
    s = s.replace('1', 'c')
    s = s.replace('a', '1')
    s = s.replace('b', '9')
    s = s.replace('c', '1')
    print(s)

=======
Suggestion 7

def main():
    S = input()
    S = S[::-1]
    S = S.replace('0','a')
    S = S.replace('1','b')
    S = S.replace('6','c')
    S = S.replace('8','d')
    S = S.replace('9','e')
    S = S.replace('a','0')
    S = S.replace('b','1')
    S = S.replace('c','9')
    S = S.replace('d','8')
    S = S.replace('e','6')
    print(S)

=======
Suggestion 8

def main():
    s = input()
    #s = "0601889"
    s = s[::-1]
    #print(s)
    s = s.replace("0","a")
    s = s.replace("1","b")
    s = s.replace("6","c")
    s = s.replace("8","d")
    s = s.replace("9","e")
    s = s.replace("a","0")
    s = s.replace("b","1")
    s = s.replace("c","9")
    s = s.replace("d","8")
    s = s.replace("e","6")
    print(s)

main()

=======
Suggestion 9

def main():
    #S = input()
    S = '0601889'
    S = S[::-1]
    S = S.replace('0','a')
    S = S.replace('1','b')
    S = S.replace('9','c')
    S = S.replace('8','d')
    S = S.replace('6','e')
    S = S.replace('a','0')
    S = S.replace('b','1')
    S = S.replace('c','9')
    S = S.replace('d','8')
    S = S.replace('e','6')
    print(S)

=======
Suggestion 10

def problem202_b():
    s = input()
    s = s[::-1]
    s = s.replace('6', 't')
    s = s.replace('9', '6')
    s = s.replace('t', '9')
    s = s.replace('0', 't')
    s = s.replace('1', '0')
    s = s.replace('t', '1')
    print(s)
