Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x, y = input().split(".")
    if 0 <= int(y) <= 2:
        print(x + "-")
    elif 3 <= int(y) <= 6:
        print(x)
    else:
        print(x + "+")

=======
Suggestion 2

def main():
    x, y = map(int, input().split('.'))
    if 0 <= y <= 2:
        print(x, '-', sep='')
    elif 3 <= y <= 6:
        print(x)
    elif 7 <= y <= 9:
        print(x, '+', sep='')

=======
Suggestion 3

def main():
    x, y = input().split(".")
    y = int(y)
    if 0 <= y <= 2:
        print(x + "-")
    elif 3 <= y <= 6:
        print(x)
    else:
        print(x + "+")

main()

=======
Suggestion 4

def main():
    x, y = [int(i) for i in input().split(".")]
    if 0 <= y <= 2:
        print(x, "-", sep="")
    elif 3 <= y <= 6:
        print(x)
    elif 7 <= y <= 9:
        print(x, "+", sep="")

=======
Suggestion 5

def main():
    x = float(input())
    if x >= 15:
        print("15+")
    elif x >= 12:
        print("12+")
    elif x >= 9:
        print("9+")
    elif x >= 6:
        print("6+")
    elif x >= 3:
        print("3+")
    elif x >= 0:
        print("0+")

=======
Suggestion 6

def main():
    x = float(input())
    if 0 <= x <= 2:
        print("X-")
    elif 3 <= x <= 6:
        print("X")
    else:
        print("X+")

=======
Suggestion 7

def main():
    X, Y = map(float, input().split('.'))
    if Y <= 2:
        print(int(X), '-', sep='')
    elif 3 <= Y <= 6:
        print(int(X))
    elif Y >= 7:
        print(int(X), '+', sep='')

=======
Suggestion 8

def main():
    # Read input
    x, y = input().split('.')
    y = int(y)
    
    # Check y
    if 0 <= y <= 2:
        print(x + '-')
    elif 3 <= y <= 6:
        print(x)
    elif 7 <= y <= 9:
        print(x + '+')
    else:
        print('Invalid input')

=======
Suggestion 9

def main():
    #write the code
    x,y = map(int,input().split('.'))
    if y<=2:
        print(x,'-',sep='')
    elif y<=6:
        print(x)
    else:
        print(x,'+',sep='')

=======
Suggestion 10

def main():
    # Read input
    x, y = input().split('.')
    # Convert to int
    x = int(x)
    y = int(y)
    # Check if y is in the range
    if y >= 0 and y <= 2:
        print(x, "-", sep="")
    elif y >= 3 and y <= 6:
        print(x)
    else:
        print(x, "+", sep="")
