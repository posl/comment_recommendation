Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    A, B = map(int, input().split())
    if A + B >= 15 and B >= 8:
        print(1)
    elif A + B >= 10 and B >= 3:
        print(2)
    elif A + B >= 3:
        print(3)
    else:
        print(4)

main()

=======
Suggestion 2

def ice_cream_type(a, b):
    if a >= 15 and b >= 8:
        return 1
    elif a >= 10 and b >= 3:
        return 2
    elif a >= 3:
        return 3
    else:
        return 4

=======
Suggestion 3

def get_category(a, b):
    if a + b >= 15 and b >= 8:
        return 1
    elif a + b >= 10 and b >= 3:
        return 2
    elif a + b >= 3:
        return 3
    else:
        return 4

=======
Suggestion 4

def calc(a, b):
    if a + b >= 15 and b >= 8:
        return 1
    elif a + b >= 10 and b >= 3:
        return 2
    elif a + b >= 3:
        return 3
    else:
        return 4

=======
Suggestion 5

def main():
    a,b = map(int, input().split())
    if (a+b) >= 15 and b >= 8:
        print(1)
    elif (a+b) >= 10 and b >= 3:
        print(2)
    elif (a+b) >= 3:
        print(3)
    else:
        print(4)

=======
Suggestion 6

def icecream_type(a,b):
    if a+b >= 15 and b >= 8:
        return 1
    elif a+b >= 10 and b >= 3:
        return 2
    elif a+b >= 3:
        return 3
    else:
        return 4

=======
Suggestion 7

def problem194_a():
    a, b = map(int, input().split())

    if a+b >= 15 and b >= 8:
        print(1)
    elif a+b >= 10 and b >= 3:
        print(2)
    elif a+b >= 3:
        print(3)
    else:
        print(4)

=======
Suggestion 8

def main():
    a, b = map(int, input().split())
    if a + b < 15 or a < 8:
        print(4)
    elif a + b >= 15 and b >= 8:
        print(1)
    elif a + b >= 10 and b >= 3:
        print(2)
    else:
        print(3)

=======
Suggestion 9

def iceCreamType():
    A, B = map(int, input().split())
    if A+B >= 15 and B >= 8:
        print(1)
    elif A+B >= 10 and B >= 3:
        print(2)
    elif A+B >= 3:
        print(3)
    else:
        print(4)

=======
Suggestion 10

def icecream():
    input_str = input()
    input_list = input_str.split()
    milk_solids = int(input_list[0])
    milk_fat = int(input_list[1])
    if milk_solids >= 15 and milk_fat >= 8:
        return 1
    elif milk_solids >= 10 and milk_fat >= 3:
        return 2
    elif milk_solids >= 3:
        return 3
    else:
        return 4
