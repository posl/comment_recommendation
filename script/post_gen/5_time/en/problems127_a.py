Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B = map(int, input().split())
    if A >= 13:
        print(B)
    elif A >= 6:
        print(B//2)
    else:
        print(0)

=======
Suggestion 2

def main():
    a,b = map(int, input().split())
    if a >= 13:
        print(b)
    elif a >= 6:
        print(int(b/2))
    else:
        print(0)

=======
Suggestion 3

def main():
    A,B = map(int, input().split())
    if A >= 13:
        print(B)
    elif A >= 6 and A <= 12:
        print(int(B/2))
    else:
        print(0)

=======
Suggestion 4

def main():
    a,b = map(int, input().split())
    if a < 6:
        print(0)
    elif a < 13:
        print(b//2)
    else:
        print(b)

=======
Suggestion 5

def cost(age, price):
    if age >= 13:
        return price
    elif age >= 6:
        return price//2
    else:
        return 0

=======
Suggestion 6

def function():
    A, B = map(int, input().split())

    if A >= 13:
        print(B)
    elif A >= 6:
        print(int(B/2))
    else:
        print(0)

=======
Suggestion 7

def ferris_wheel():
    age, cost = map(int, input().split())
    if age <= 5:
        print(0)
    elif age in range(6, 13):
        print(cost//2)
    else:
        print(cost)

=======
Suggestion 8

def main():
    # get input
    a, b = map(int, input().split())

    # your code
    if a >= 13:
        print(b)
    elif 6 <= a <= 12:
        print(int(b/2))
    else:
        print(0)

=======
Suggestion 9

def main():
    # Take input Here and Call solution function
    a,b = get_ints_in_variables()
    print(solution(a,b))
