Synthesizing 10/10 solutions

=======
Suggestion 1

def func():
    x, y = map(int, input().split())
    for i in range(x+1):
        if 2*i + 4*(x-i) == y:
            print('Yes')
            return
    print('No')
    return

=======
Suggestion 2

def is_answer(x, y):
    for i in range(x+1):
        if 2*i + 4*(x-i) == y:
            return True
    return False

=======
Suggestion 3

def problem170_b():
    x,y = map(int,input().split())
    for i in range(x+1):
        j = x-i
        if i*2 + j*4 == y:
            print('Yes')
            return
    print('No')

=======
Suggestion 4

def solve(x,y):
    for i in range(x+1):
        j = x - i
        if 2*i + 4*j == y:
            return True
    return False

=======
Suggestion 5

def main():
    X,Y = map(int,input().split())
    for i in range(X+1):
        if 2*i + 4*(X-i) == Y:
            print("Yes")
            exit()
    print("No")
main()

=======
Suggestion 6

def func(x, y):
    for i in range(x+1):
        if i*4+(x-i)*2 == y:
            return True
    return False

=======
Suggestion 7

def main():
    x,y = map(int,input().split())
    if y%2==0:
        if 2*x<=y and y<=4*x:
            print("Yes")
        else:
            print("No")
    else:
        print("No")

=======
Suggestion 8

def func():
    x,y = map(int,input().split())
    if 2*x <= y <= 4*x and y%2 == 0:
        print("Yes")
    else:
        print("No")

func()

=======
Suggestion 9

def main():
    num_animal, num_leg = map(int, input().split())

    for num_turtle in range(num_animal + 1):
        num_crane = num_animal - num_turtle
        total_leg = 2 * num_crane + 4 * num_turtle
        if total_leg == num_leg:
            print("Yes")
            return
    print("No")

=======
Suggestion 10

def main():
    x,y = map(int, input().split())
    if x*2 <= y <= x*4 and y%2 == 0:
        print("Yes")
    else:
        print("No")
