Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x, y = map(int, input().split())
    if x < y:
        x, y = y, x
    if x - y < 3:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    x, y = map(int, input().split())
    if x < y:
        x, y = y, x
    if x - y > 2:
        print('No')
    else:
        print('Yes')

=======
Suggestion 3

def main():
    X, Y = map(int, input().split())
    if abs(X-Y) <= 2:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    x, y = map(int, input().split())
    if x < y:
        x, y = y, x
    print('Yes' if x - y >= 3 else 'No')

=======
Suggestion 5

def main():
    x, y = map(int, input().split())
    if x > y:
        print('No')
    else:
        print('Yes')

=======
Suggestion 6

def main():
    x, y = map(int,input().split())
    if x > y:
        print("Yes" if x-y < 3 else "No")
    else:
        print("Yes" if y-x < 3 else "No")

main()

If you like this post, please share it!

Related Posts

Python | Set 1 (Getting Started)

Python | Set 2 (Variables, Expressions, and Statements)

Python | Set 3 (If-Else and Loops)

Python | Set 4 (Functions)

Python | Set 5 (Strings)

Python | Set 6 (Lists)

Python | Set 7 (Tuples and Sequences)

Python | Set 8 (Dictionaries)

Python | Set 9 (Functions)

Python | Set 10 (Classes and Objects)

Python | Set 11 (Regular Expressions)

Python | Set 12 (Iterators)

Python | Set 13 (File Handling)

Python | Set 14 (Exceptions)

Python | Set 15 (Built-in Functions)

Python | Set 16 (Modules and Packages)

Python | Set 17 (Input and Output)

Python | Set 18 (Standard Library)

Python | Set 19 (Advanced)

Python | Set 20 (Data Structures)

Python | Set 21 (Data Structures)

Python | Set 22 (Data Structures)

Python | Set 23 (Data Structures)

Python | Set 24 (Data Structures)

Python | Set 25 (Data Structures)

Python | Set 26 (Data Structures)

Python | Set 27 (Data Structures)

Python | Set 28 (Data Structures)

Python | Set 29 (Data Structures)

Python | Set 30 (Data Structures)

Python | Set 31 (Data Structures)

Python | Set 32 (Data Structures)

Python | Set 33 (Data Structures)

Python | Set 34 (Data Structures)

Python | Set 35 (Data Structures)

Python | Set 36 (Data Structures)

Python | Set 37 (Data Structures)

Python | Set 38 (Data Structures)

Python | Set 39 (Data Structures)

Python | Set 40 (Data Structures)

Python | Set 41 (Data Structures)

Python | Set 42 (Data Structures)

Python | Set 43 (Data Structures)

Python | Set 44 (Data Structures)

Python | Set 45 (Data Structures)

Python | Set 46 (Data Structures)

Python | Set 47 (Data Structures

=======
Suggestion 7

def main():
    X, Y = map(int, input().strip().split())
    if X > Y:
        if X - Y >= 3:
            print('No')
        else:
            print('Yes')
    elif Y > X:
        if Y - X >= 3:
            print('No')
        else:
            print('Yes')

=======
Suggestion 8

def check_score(X, Y):
    if X > Y:
        if (X - Y) < 3:
            return "No"
        else:
            return "Yes"
    else:
        if (Y - X) < 3:
            return "No"
        else:
            return "Yes"

=======
Suggestion 9

def can_turn_tables(x, y):
    if x < y:
        return "Yes" if y - x >= 3 else "No"
    else:
        return "Yes" if x - y >= 3 else "No"

=======
Suggestion 10

def main():
    # Read input
    X, Y = map(int, input().split())
    
    # Process
    if X > Y:
        if X - Y > 2:
            print("No")
        else:
            print("Yes")
    else:
        if Y - X > 2:
            print("No")
        else:
            print("Yes")
