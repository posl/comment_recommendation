Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    abc = input()
    bca = abc[1] + abc[2] + abc[0]
    cab = abc[2] + abc[0] + abc[1]
    print(int(abc) + int(bca) + int(cab))

=======
Suggestion 2

def main():
    abc = int(input())
    a = abc // 100
    b = (abc - a * 100) // 10
    c = (abc - a * 100 - b * 10)
    print(abc + b * 100 + c * 10 + c * 100)

=======
Suggestion 3

def main():
    abc = input()
    a = int(abc[0])
    b = int(abc[1])
    c = int(abc[2])
    print(a + b + c + b*10 + c*100 + c*10 + a*100 + a*10 + b*100)

=======
Suggestion 4

def main():
    abc = input()
    a = int(abc[0])
    b = int(abc[1])
    c = int(abc[2])
    print(a+b+c+a*b+b*c+c*a)

=======
Suggestion 5

def main():
    abc = int(input())
    a = abc // 100
    b = abc % 100 // 10
    c = abc % 10
    print((a + b + c) * (a * 100 + b * 10 + c))

=======
Suggestion 6

def main():
    # 入力
    abc = input()
    # 出力
    print(int(abc[0]) + int(abc[1]) + int(abc[2]) + int(abc[1]) + int(abc[2]) + int(abc[0]) + int(abc[2]) + int(abc[0]) + int(abc[1]))

=======
Suggestion 7

def main():
    abc = input()
    print(int(abc) + int(abc[::-1]) + int(abc[1:] + abc[0]))

=======
Suggestion 8

def main():
    #入力
    abc = int(input())
    #abcを桁ごとに分割
    a = abc // 100
    b = abc % 100 // 10
    c = abc % 100 % 10
    #出力
    print(a+b+c+b+c+a+c+a+b)

=======
Suggestion 9

def main():
    abc = input()
    x,y,z = list(abc)
    print(int(x)*2+int(y)*2+int(z)*2)

=======
Suggestion 10

def main():
    #入力
    abc = input()
    #abcが3桁の整数かどうか
    if len(abc) != 3:
        return -1
    #abcが0でない整数かどうか
    if int(abc) == 0:
        return -1
    #abcを各桁に分ける
    a = int(abc[0])
    b = int(abc[1])
    c = int(abc[2])
    #出力
    print(a+b+c + b+c+a + c+a+b)
