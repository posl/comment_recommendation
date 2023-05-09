Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    X = int(input())
    a = X // 500
    b = (X % 500) // 5
    print(a * 1000 + b * 5)

=======
Suggestion 2

def main():
    x = int(input())
    happiness = 0
    happiness += (x//500)*1000
    x = x%500
    happiness += (x//5)*5
    print(happiness)

=======
Suggestion 3

def main():
    x = int(input())
    print((x//500)*1000+((x%500)//5)*5)

=======
Suggestion 4

def main():
    x = int(input())
    print(int(x/500)*1000 + int((x%500)/5)*5)

=======
Suggestion 5

def main():
    x = int(input())
    print(int((x//500)*1000+((x%500)//5)*5))

=======
Suggestion 6

def solve():
    x = int(input())
    print((x//500)*1000+((x%500)//5)*5)

=======
Suggestion 7

def main():
    x = int(input())
    a = int(x/500)
    x = x - (a*500)
    b = int(x/5)
    print(a*1000 + b*5)

=======
Suggestion 8

def main():
    x = int(input())
    n = x // 500
    m = x % 500
    o = m // 5
    print(n*1000 + o*5)

=======
Suggestion 9

def coin_exchange():
    x = int(input())
    n = x // 500
    m = (x % 500) // 5
    print(n * 1000 + m * 5)
