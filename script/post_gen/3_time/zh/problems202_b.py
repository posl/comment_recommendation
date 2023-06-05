Synthesizing 10/10 solutions

=======
Suggestion 1

def reverseString(s):
    return s[::-1]

=======
Suggestion 2

def main():
    S = input()
    S = S[::-1]
    for i in range(len(S)):
        if S[i] == '6':
            print('9', end='')
        elif S[i] == '9':
            print('6', end='')
        else:
            print(S[i], end='')
    print()

=======
Suggestion 3

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
    return

=======
Suggestion 4

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
Suggestion 5

def main():
    # 读入
    s = input()
    # 180度旋转
    s = s[::-1]
    # 0,1,6,8,9替换
    s = s.replace('0', 'x')
    s = s.replace('1', 'y')
    s = s.replace('6', 'z')
    s = s.replace('8', '6')
    s = s.replace('9', '8')
    s = s.replace('x', '1')
    s = s.replace('y', '0')
    s = s.replace('z', '9')
    # 读出
    print(s)

=======
Suggestion 6

def main():
    s = input()
    s = s[::-1]
    s = s.replace('6','a')
    s = s.replace('9','6')
    s = s.replace('a','9')
    s = s.replace('0','a')
    s = s.replace('1','b')
    s = s.replace('a','0')
    s = s.replace('b','1')
    print(s)

=======
Suggestion 7

def main():
    s = input()
    s = s[::-1]
    s = s.replace("9", "x")
    s = s.replace("6", "9")
    s = s.replace("x", "6")
    s = s.replace("1", "x")
    s = s.replace("0", "1")
    s = s.replace("x", "0")
    print(s)

main()

=======
Suggestion 8

def main():
    S = input()
    S = S[::-1]
    S = S.replace("0","a").replace("1","0").replace("a","1")
    S = S.replace("6","a").replace("9","6").replace("a","9")
    print(S)
main()

=======
Suggestion 9

def main():
    # 读入
    s = input()
    # 处理
    s2 = s[::-1]
    s3 = ""
    for i in range(len(s2)):
        if s2[i] == "0":
            s3 = s3 + "0"
        elif s2[i] == "1":
            s3 = s3 + "1"
        elif s2[i] == "6":
            s3 = s3 + "9"
        elif s2[i] == "8":
            s3 = s3 + "8"
        elif s2[i] == "9":
            s3 = s3 + "6"
    # 输出
    print(s3)

=======
Suggestion 10

def main():
    S = input()
    s = S[::-1]
    s = s.replace('6','t')
    s = s.replace('9','6')
    s = s.replace('t','9')
    s = s.replace('0','t')
    s = s.replace('1','0')
    s = s.replace('t','1')
    print(s)
