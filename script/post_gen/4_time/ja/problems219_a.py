Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x = int(input())
    if x < 40:
        print(40 - x)
    elif x < 70:
        print(70 - x)
    elif x < 90:
        print(90 - x)
    else:
        print("expert")

=======
Suggestion 2

def main():
    x = int(input())
    if x < 40:
        print(40 - x)
    elif x < 70:
        print(70 - x)
    elif x < 90:
        print(90 - x)
    else:
        print('expert')

=======
Suggestion 3

def main():
    x = int(input())
    if x >= 0 and x < 40:
        print(40 - x)
    elif x >= 40 and x < 70:
        print(70 - x)
    elif x >= 70 and x < 90:
        print(90 - x)
    elif x >= 90 and x <= 100:
        print("expert")

=======
Suggestion 4

def rank(x):
    if 0 <= x < 40:
        return 40 - x
    elif 40 <= x < 70:
        return 70 - x
    elif 70 <= x < 90:
        return 90 - x
    elif 90 <= x <= 100:
        return 'expert'
    else:
        return 'error'

x = int(input())
print(rank(x))

=======
Suggestion 5

def main():
    x = int(input())
    if x >= 90:
        print("expert")
    elif x >= 70:
        print(90 - x)
    elif x >= 40:
        print(70 - x)
    else:
        print(40 - x)

=======
Suggestion 6

def solve():
    x = int(input())
    if x < 40:
        print(40-x)
    elif x < 70:
        print(70-x)
    elif x < 90:
        print(90-x)
    else:
        print("expert")

=======
Suggestion 7

def rank(n):
    if n >= 90:
        return "expert"
    elif n >= 70:
        return 90 - n
    elif n >= 40:
        return 70 - n
    else:
        return 40 - n

n = int(input())
print(rank(n))
