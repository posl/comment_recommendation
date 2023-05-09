Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x, y = map(int, input().split("."))
    if y <= 2:
        print(str(x) + "-")
    elif y <= 6:
        print(x)
    else:
        print(str(x) + "+")

=======
Suggestion 2

def main():
    x, y = map(int, input().split('.'))
    if y <= 2:
        print(str(x) + '-')
    elif y <= 6:
        print(str(x))
    else:
        print(str(x) + '+')

=======
Suggestion 3

def main():
    x, y = map(int, input().split('.'))
    if 0 <= y <= 2:
        print(str(x) + '-')
    elif 3 <= y <= 6:
        print(x)
    elif 7 <= y <= 9:
        print(str(x) + '+')

=======
Suggestion 4

def main():
    x, y = map(int, input().split("."))
    if y <= 2:
        print("{}-".format(x))
    elif y <= 6:
        print(x)
    else:
        print("{}+".format(x))

=======
Suggestion 5

def main():
    x, y = input().split('.')
    y = int(y)
    if y <= 2:
        print(x + '-')
    elif y <= 6:
        print(x)
    elif y <= 9:
        print(x + '+')

=======
Suggestion 6

def main():
    x, y = input().split('.')
    y = int(y)
    if y <= 2:
        print(x+'-')
    elif y <= 6:
        print(x)
    else:
        print(x+'+')

=======
Suggestion 7

def main():
    x,y = input().split('.')
    if int(y) <= 2:
        print(x+'-')
    elif int(y) <= 6:
        print(x)
    else:
        print(x+'+')

=======
Suggestion 8

def main():
    num = input()
    num = num.split(".")
    if int(num[1]) >= 0 and int(num[1]) <= 2:
        print(num[0] + "-")
    elif int(num[1]) >= 3 and int(num[1]) <= 6:
        print(num[0])
    elif int(num[1]) >= 7 and int(num[1]) <= 9:
        print(num[0] + "+")

=======
Suggestion 9

def main():
    input = raw_input()
    input = input.split('.')
    x = int(input[0])
    y = int(input[1])

    if y <= 2:
        print str(x) + "-"
    elif y <= 6:
        print str(x)
    else:
        print str(x) + "+"

=======
Suggestion 10

def get_input():
    x, y = input().split('.')
    return (int(x), int(y))
