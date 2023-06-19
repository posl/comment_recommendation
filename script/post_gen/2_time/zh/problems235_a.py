Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    abc = input()
    a = int(abc[0])
    b = int(abc[1])
    c = int(abc[2])
    print(a*111+b*111+c*111)

=======
Suggestion 2

def main():
    abc = raw_input()
    a = int(abc[0])
    b = int(abc[1])
    c = int(abc[2])
    print a*111 + b*11 + c*1 + b*100 + c*10 + a*1 + c*100 + a*10 + b*1

=======
Suggestion 3

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    print(a+b+c)

=======
Suggestion 4

def problem235_a():
    abc = input()
    a = int(abc[0])
    b = int(abc[1])
    c = int(abc[2])
    result = a*100+b*10+c + b*100+c*10+a + c*100+a*10+b
    print(result)

=======
Suggestion 5

def main():
    num = input()
    if len(num) == 3:
        num = int(num)
        x = num // 100
        y = (num // 10) % 10
        z = num % 10
        print(x + y + z + (x * 10 + y) + (y * 10 + z) + (z * 10 + x))
    else:
        print("输入不合法")

=======
Suggestion 6

def main():
    num = input()
    a = int(num[0])
    b = int(num[1])
    c = int(num[2])
    print(a*111+b*11+c*1+a*100+b*10+c*1+a*100+b*10+c*1)

=======
Suggestion 7

def main():
    abc = int(input())
    a = abc // 100
    b = abc // 10 % 10
    c = abc % 10
    print(a * 111 + b * 111 + c * 111)

=======
Suggestion 8

def solution():
    abc = int(input())
    bca = abc % 100 * 10 + abc // 100
    cab = abc % 10 * 100 + abc // 10
    print(abc + bca + cab)

=======
Suggestion 9

def f(x):
    return int(x[0])*100+int(x[1])*10+int(x[2])
