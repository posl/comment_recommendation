Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x = input()
    print(int(round(float(x))))

=======
Suggestion 2

def main():
    num = input()
    print(round(float(num)))

=======
Suggestion 3

def main():
    X = input()
    print(round(float(X)))

=======
Suggestion 4

def solution(x):
    x = str(x)
    if '.' in x:
        return int(float(x)+0.5)
    else:
        return int(x)

=======
Suggestion 5

def main():
    x = float(input())
    print(round(x))

=======
Suggestion 6

def main():
    X = input()
    print(int(float(X)+0.5))

=======
Suggestion 7

def main():
    x = input()
    if x.find(".") == -1:
        print(x)
    else:
        print(x[:x.find(".")])

=======
Suggestion 8

def main():
    print(round(float(input())))

=======
Suggestion 9

def main():
    x = input()
    print(round(float(x)))
