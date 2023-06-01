Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    abc = int(input())
    bca = abc % 100 * 10 + abc // 100
    cab = abc % 10 * 100 + abc // 10
    print(abc + bca + cab)

=======
Suggestion 2

def main():
    abc = input()
    abc = int(abc)
    a = abc // 100
    b = (abc - a * 100) // 10
    c = abc - a * 100 - b * 10
    print(a * 100 + b * 10 + c + b * 100 + c * 10 + a + c * 100 + a * 10 + b)

=======
Suggestion 3

def main():
    abc = input()
    a = int(abc[0])
    b = int(abc[1])
    c = int(abc[2])
    print(a*100+b*10+c+b*100+c*10+a+c*100+a*10+b)

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

def get_num(num):
    a = num // 100
    b = num // 10 % 10
    c = num % 10
    return a, b, c

=======
Suggestion 6

def main():
    abc = int(input())
    bca = abc * 10 % 1000 + abc // 100
    cab = abc * 100 % 1000 + abc // 10
    print(abc + bca + cab)

=======
Suggestion 7

def main():
    abc = int(input())
    bca = 100 * (abc % 10) + 10 * (abc // 10 % 10) + abc // 100
    cab = 100 * (abc // 100) + 10 * (abc % 10) + abc // 10 % 10
    print(abc + bca + cab)
