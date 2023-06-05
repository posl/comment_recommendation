Synthesizing 10/10 solutions

=======
Suggestion 1

def main(abc):
    abc = int(abc)
    a = abc // 100
    b = abc // 10 % 10
    c = abc % 10
    print(a * 100 + b * 10 + c + b * 100 + c * 10 + a + c * 100 + a * 10 + b)

=======
Suggestion 2

def main():
    num = input()
    num1 = int(num[0] + num[1] + num[2])
    num2 = int(num[0] + num[2] + num[1])
    num3 = int(num[1] + num[0] + num[2])
    num4 = int(num[1] + num[2] + num[0])
    num5 = int(num[2] + num[0] + num[1])
    num6 = int(num[2] + num[1] + num[0])
    print(num1 + num2 + num3 + num4 + num5 + num6)

=======
Suggestion 3

def sum_abc(a, b, c):
    return a * 100 + b * 10 + c + b * 100 + c * 10 + a + c * 100 + a * 10 + b

=======
Suggestion 4

def f():
    abc = int(input())
    a = abc // 100
    b = abc // 10 - a * 10
    c = abc % 10
    print(a * 100 + b * 10 + c + b * 100 + c * 10 + a + c * 100 + a * 10 + b)

f()

=======
Suggestion 5

def abc():
    abc = input()
    a = int(abc[0])
    b = int(abc[1])
    c = int(abc[2])
    print(a*100+b*10+c+b*100+c*10+a+c*100+a*10+b)

abc()

=======
Suggestion 6

def main():
    abc = input()
    a, b, c = abc[0], abc[1], abc[2]
    print(int(a+b+c)+int(b+c+a)+int(c+a+b))

=======
Suggestion 7

def main():
    abc = int(input())
    bca = int(str(abc)[1:] + str(abc)[0])
    cab = int(str(abc)[2:] + str(abc)[:2])
    print(abc + bca + cab)

=======
Suggestion 8

def main():
    abc = input()
    a = int(abc[0])
    b = int(abc[1])
    c = int(abc[2])
    print(a*111+b*111+c*111)

=======
Suggestion 9

def main():
    abc = int(input())
    bca = abc % 100 * 10 + abc // 100
    cab = abc % 10 * 100 + abc // 10
    print(abc + bca + cab)

=======
Suggestion 10

def main():
    abc = input()
    a = int(abc[0])
    b = int(abc[1])
    c = int(abc[2])
    print(a*111+b*11+c*1+a*100+b*10+c+a*10+b*100+c*10)
