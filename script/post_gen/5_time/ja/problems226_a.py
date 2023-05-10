Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x = float(input())
    print(round(x))

=======
Suggestion 2

def main():
    X = float(input())
    print(int(X*10+0.5)//10)

=======
Suggestion 3

def solve():
    # n = int(input())
    # a,b,c = map(int,input().split())
    # s = input()
    X = float(input())

    print(int(X*10+0.5)//10)
    # print(n)

=======
Suggestion 4

def main():
    x = float(input())
    print(int(x*10+0.5)//10)

=======
Suggestion 5

def round_down(num, digit):
    p = 10 ** digit
    return (num * p // 1) / p

x = float(input())
print(round_down(x, 0))

=======
Suggestion 6

def main():
    x = float(input())
    print(round(x, 0))

=======
Suggestion 7

def round_float(number, decimal):
    return round(number, decimal)

=======
Suggestion 8

def main():
    x = float(input())
    print(int(x+0.5))
