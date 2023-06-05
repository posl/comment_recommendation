Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    abc = int(input())
    a = abc // 100
    b = abc // 10 % 10
    c = abc % 10
    print(a*100+b*10+c+b*100+c*10+a+c*100+a*10+b)

=======
Suggestion 2

def cal(n):
    a = n // 100
    b = n // 10 % 10
    c = n % 10
    return a*100+b*10+c+a*10+b+c+a+b*100+c*10+b

=======
Suggestion 3

def main():
    abc = input()
    a = int(abc[0])
    b = int(abc[1])
    c = int(abc[2])
    print(a+b+c + a*100+b*10+c + b*100+c*10+a + c*100+a*10+b)

=======
Suggestion 4

def main():
    abc = input()
    a = int(abc[0])
    b = int(abc[1])
    c = int(abc[2])
    print(a*111+b*111+c*111)

=======
Suggestion 5

def problem235_a():
    abc = int(input())
    bca = abc % 100 * 10 + abc // 100
    cab = abc % 10 * 100 + abc // 10
    print(abc + bca + cab)

=======
Suggestion 6

def main():
    abc = input()
    a = int(abc[0])
    b = int(abc[1])
    c = int(abc[2])
    print(a*111+b*11+c*1+a*111+b*11+c*1+a*111+b*11+c*1)

=======
Suggestion 7

def main():
    abc = int(input())
    a = int(abc/100)
    b = int(abc/10)%10
    c = abc%10
    print(a+b+c+b+c+a+c+a+b+c)

=======
Suggestion 8

def main():
    abc = int(input())
    bca = int(str(abc)[1:]+str(abc)[0])
    cab = int(str(abc)[2]+str(abc)[:2])
    print(abc+bca+cab)

=======
Suggestion 9

def main():
    abc = int(input())
    bca = abc%10*100 + abc//10%10*10 + abc//100
    cab = abc%10*100 + abc//100*10 + abc//10%10
    print(abc+bca+cab)

=======
Suggestion 10

def main():
    a = input()
    b = a[::-1]
    c = a[1]+a[2]+a[0]
    print(int(a)+int(b)+int(c))
