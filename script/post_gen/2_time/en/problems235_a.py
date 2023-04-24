Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    abc = input()
    a = int(abc[0])
    b = int(abc[1])
    c = int(abc[2])
    print(a+b+c + b+c+a + c+a+b)

=======
Suggestion 2

def main():
    abc = input()
    a, b, c = abc[0], abc[1], abc[2]
    print(int(a + b + c) + int(b + c + a) + int(c + a + b))

main()

=======
Suggestion 3

def main():
    abc = input()
    a = int(abc[0])
    b = int(abc[1])
    c = int(abc[2])
    print(abc + bca + cab)

=======
Suggestion 4

def main():
    a, b, c = input()
    print(int(a) + int(b) + int(c) + int(b + c + a) + int(c + a + b))

=======
Suggestion 5

def main():
    abc = int(input())
    a = abc // 100
    b = abc % 100 // 10
    c = abc % 10
    print(a + b + c + a * 10 + b * 100 + c * 1000 + b * 10 + c * 100 + a * 1000)

main()

=======
Suggestion 6

def main():
    abc = input()
    abc1 = abc[0]
    abc2 = abc[1]
    abc3 = abc[2]
    bca = abc2 + abc3 + abc1
    cab = abc3 + abc1 + abc2
    print(int(abc)+int(bca)+int(cab))

=======
Suggestion 7

def main():
    abc = input()
    abc = int(abc)
    a = abc // 100
    b = (abc // 10) % 10
    c = abc % 10
    print((a+b+c)*(a*100+b*10+c))

=======
Suggestion 8

def main():
    a, b, c = map(int, input())
    print(a+b+c, b+c+a, c+a+b, sep='')

=======
Suggestion 9

def sum_digits(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    return sum

=======
Suggestion 10

def main():
    s = input()
    print(3 * int(s))
