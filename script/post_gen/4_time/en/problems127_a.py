Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    if a >= 13:
        print(b)
    elif 6 <= a <= 12:
        print(int(b/2))
    else:
        print(0)

=======
Suggestion 2

def main():
    A, B = map(int, input().split())
    if A >= 13:
        print(B)
    elif A >= 6 and A <= 12:
        print(int(B/2))
    else:
        print(0)

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    if a >= 13:
        print(b)
    elif a >= 6:
        print(int(b/2))
    else:
        print(0)

=======
Suggestion 4

def main():
    a,b = map(int, input().split())
    if a >= 13:
        print(b)
    elif a >= 6 and a <= 12:
        print(int(b/2))
    else:
        print(0)

main()

=======
Suggestion 5

def problem127_a():
    a, b = map(int, input().split())
    if a >= 13:
        print(b)
    elif 6 <= a <= 12:
        print(b // 2)
    else:
        print(0)

=======
Suggestion 6

def main():
    a, b = map(int, input().split())
    if a > 12:
        print(b)
    elif a > 5:
        print(b//2)
    else:
        print(0)

=======
Suggestion 7

def main():
    A, B = map(int, input().split())
    if A < 6:
        print(0)
    elif A < 13:
        print(B//2)
    else:
        print(B)

=======
Suggestion 8

def main():
    a,b = map(int, input().split())
    if a>=13:
        print(b)
    elif a>=6 and a<=12:
        print(int(b/2))
    else:
        print(0)

=======
Suggestion 9

def main():
    a,b = map(int, input().split())
    if a>=13:
        print(b)
    elif a>=6 and a<=12:
        print(b//2)
    else:
        print(0)

=======
Suggestion 10

def calc_ferris_wheel_cost(age, cost):
    if age >= 13:
        return cost
    elif age >= 6:
        return cost / 2
    else:
        return 0
