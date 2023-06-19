Synthesizing 10/10 solutions

=======
Suggestion 1

def check_legs(x, y):
    if x == 2 * y or x == 4 * y:
        return True
    else:
        return False

x, y = map(int, input().split())

=======
Suggestion 2

def check_legs(x,y):
    '''
    x = cranes
    y = turtles
    '''
    if x*2 + y*4 == legs:
        return True
    else:
        return False

legs = input("How many legs does the animals have in total? ")
legs = int(legs)

cranes = input("How many cranes are there? ")
cranes = int(cranes)

turtles = input("How many turtles are there? ")
turtles = int(turtles)

=======
Suggestion 3

def solve(x, y):
    for i in range(x+1):
        if i*2 + (x-i)*4 == y:
            return True
    return False

x, y = map(int, input().split())

=======
Suggestion 4

def problem170_b():
    x,y = map(int, input().split())
    for i in range(x+1):
        if i*2 + (x-i)*4 == y:
            print("Yes")
            return
    print("No")

=======
Suggestion 5

def count_legs(num_animals, num_legs):
    for num_tur in range(num_animals + 1):
        num_crane = num_animals - num_tur
        if 2 * num_crane + 4 * num_tur == num_legs:
            return True
    return False

=======
Suggestion 6

def solve():
    x, y = map(int, input().split())
    for i in range(x + 1):
        if i * 4 + (x - i) * 2 == y:
            print('Yes')
            return
    print('No')

=======
Suggestion 7

def main():
    x,y = map(int,input().split())
    for i in range(x+1):
        if i*2 + (x-i)*4 == y:
            print("Yes")
            exit()
    print("No")

=======
Suggestion 8

def problems170_b():
    x, y = map(int, input().split())
    for i in range(0, x + 1):
        for j in range(0, x + 1):
            if 2 * i + 4 * j == y and i + j == x:
                print('Yes')
                exit()
    print('No')
    exit()

=======
Suggestion 9

def main():
    x, y = map(int, input().split())
    for i in range(x+1):
        if 2*i + 4*(x-i) == y:
            print("Yes")
            return
    print("No")

=======
Suggestion 10

def solve():
    x,y = map(int,input().split())
    for i in range(x+1):
        if i*2 + (x-i)*4 == y:
            print("Yes")
            return
    print("No")
