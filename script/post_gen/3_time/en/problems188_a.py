Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x, y = map(int, input().split())
    if abs(x - y) < 3:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    x, y = map(int, input().split())
    if abs(x - y) > 2:
        print("No")
    else:
        print("Yes")

=======
Suggestion 3

def main():
    x, y = map(int, input().split())
    if x > y:
        if (x - y) > 2:
            print("No")
        else:
            print("Yes")
    else:
        if (y - x) > 2:
            print("No")
        else:
            print("Yes")
main()

=======
Suggestion 4

def main():
    x, y = map(int, input().split())
    print("Yes" if abs(x-y) > 2 else "No")

=======
Suggestion 5

def main():
    x, y = map(int, input().split())
    print("Yes" if x < y else "No")

=======
Suggestion 6

def main():
    x,y = map(int,input().split())
    if x<y:
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def main():
    #input
    X, Y = map(int, input().split())
    #output
    print('Yes' if X < Y else 'No')

=======
Suggestion 8

def main():
    # Read the input
    X, Y = map(int, input().split())
    # Check if the team which is behind can turn the tables
    if abs(X - Y) < 3:
        print('Yes')
    else:
        print('No')

=======
Suggestion 9

def main():
    #Read input
    X, Y = map(int, input().split())
    
    #Solve problem
    if X < Y:
        if Y - X < 3:
            print("Yes")
        else:
            print("No")
    else:
        if X - Y < 3:
            print("Yes")
        else:
            print("No")

=======
Suggestion 10

def main():
    # Read the input
    X, Y = map(int, input().split())

    # Write the logic here
    diff = abs(X - Y)
    if diff <= 2:
        print("Yes")
    else:
        print("No")
