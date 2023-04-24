Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    X, Y = map(int, input().split())
    for i in range(X + 1):
        if 2 * i + 4 * (X - i) == Y:
            print('Yes')
            return
    print('No')

=======
Suggestion 2

def main():
    x, y = map(int, input().split())
    if x == 1 and y == 2:
        print("Yes")
    elif x == 2 and y == 1:
        print("Yes")
    elif x == 2 and y == 2:
        print("Yes")
    elif x == 2 and y == 4:
        print("Yes")
    elif x == 4 and y == 2:
        print("Yes")
    elif x == 4 and y == 4:
        print("Yes")
    elif x == 4 and y == 8:
        print("Yes")
    elif x == 8 and y == 4:
        print("Yes")
    elif x == 8 and y == 8:
        print("Yes")
    elif x == 8 and y == 16:
        print("Yes")
    elif x == 16 and y == 8:
        print("Yes")
    elif x == 16 and y == 16:
        print("Yes")
    elif x == 16 and y == 32:
        print("Yes")
    elif x == 32 and y == 16:
        print("Yes")
    elif x == 32 and y == 32:
        print("Yes")
    elif x == 32 and y == 64:
        print("Yes")
    elif x == 64 and y == 32:
        print("Yes")
    elif x == 64 and y == 64:
        print("Yes")
    elif x == 64 and y == 128:
        print("Yes")
    elif x == 128 and y == 64:
        print("Yes")
    elif x == 128 and y == 128:
        print("Yes")
    elif x == 128 and y == 256:
        print("Yes")
    elif x == 256 and y == 128:
        print("Yes")
    elif x == 256 and y == 256:
        print("Yes")
    elif x == 256 and y == 512:
        print("Yes")
    elif x == 512 and y == 256:
        print("Yes")
    elif x == 512 and y == 512:
        print("Yes")
    elif x == 512 and y == 1024:
        print("Yes")
    elif x == 1024 and y

=======
Suggestion 3

def main():
    X, Y = map(int, input().split())
    if X * 4 >= Y and X * 2 <= Y:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    x, y = map(int, input().split())
    if x == 1 and y == 2:
        print('Yes')
        return
    for i in range(1, x):
        if 2 * i + 4 * (x - i) == y:
            print('Yes')
            return
    print('No')
    return

main()

=======
Suggestion 5

def main():
    x, y = map(int, input().split())
    if (y % 2 == 0) and (y / 2 <= x) and (y / 2 >= x - 2):
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def animals(x, y):
    if x * 2 == y or x * 4 == y:
        return "Yes"
    if x * 2 > y:
        return "No"
    if (y - x * 2) % 2 == 0:
        return "Yes"
    return "No"

=======
Suggestion 7

def main():

    x, y = map(int, input().split())

    if x*2 == y or x*4 == y or (x*2 + x*4) == y:
        print('Yes')
    else:
        print('No')

=======
Suggestion 8

def main():
    """Main function"""
    animals, legs = map(int, input().split())
    cranes = 0
    turtles = 0
    while cranes <= animals:
        if cranes * 2 + turtles * 4 == legs:
            print("Yes")
            return
        cranes += 1
        turtles = animals - cranes
    print("No")

=======
Suggestion 9

def main():
    # Write code here
    x,y = map(int,input().split())
    if x*4 >= y and x*2 <= y:
        print("Yes")
    else:
        print("No")

=======
Suggestion 10

def get_input():
    return input()
