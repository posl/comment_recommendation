Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    X, Y = map(int, input().split())
    for i in range(X+1):
        j = X - i
        if i*2 + j*4 == Y:
            print("Yes")
            return
    print("No")

=======
Suggestion 2

def check(X, Y):
    for i in range(X + 1):
        if i * 2 + (X - i) * 4 == Y:
            return True
    return False

X, Y = map(int, input().split())

=======
Suggestion 3

def main():
    x, y = map(int, input().split())
    for i in range(x+1):
        if i*2+(x-i)*4 == y:
            print('Yes')
            break
    else:
        print('No')

=======
Suggestion 4

def main():
    X, Y = map(int, input().split())
    if X*2 <= Y <= X*4:
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    X, Y = map(int, input().split())
    if X * 4 >= Y and Y >= X * 2:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    X, Y = map(int, input().split())

    if Y % 2 == 0:
        if X * 4 >= Y and X * 2 <= Y:
            print("Yes")
        else:
            print("No")
    else:
        print("No")

=======
Suggestion 7

def main():
    X, Y = map(int, input().split())
    if X == Y == 1:
        print("Yes")
        return
    for i in range(X + 1):
        if 2 * i + 4 * (X - i) == Y:
            print("Yes")
            return
    print("No")

=======
Suggestion 8

def main():
    #input
    X, Y = map(int, input().split())

    #output
    if Y % 2 == 0:
        if X*2 <= Y <= X*4:
            print('Yes')
        else:
            print('No')
    else:
        print('No')

=======
Suggestion 9

def main():
    inputs = input().split()
    x = int(inputs[0])
    y = int(inputs[1])
    if x*2 == y or x*4 == y or x*2 + x*4 == y:
        print("Yes")
    else:
        print("No")

=======
Suggestion 10

def is_legs_correct(crane_num, turtle_num, legs_num):
    return crane_num*2 + turtle_num*4 == legs_num
