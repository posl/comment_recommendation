Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def round(x):
    if x - int(x) >= 0.5:
        return int(x) + 1
    else:
        return int(x)

x = float(input())
print(round(x))

=======
Suggestion 2

def round(x):
    if x - int(x) >= 0.5:
        return int(x) + 1
    else:
        return int(x)

=======
Suggestion 3

def round(x):
    if x - int(x) >= 0.5:
        return int(x) + 1
    else:
        return int(x)

print(round(float(input())))

=======
Suggestion 4

def round(number):
    if number >= 0:
        if number % 1 >= 0.5:
            return int(number) + 1
        else:
            return int(number)
    else:
        if number % 1 <= -0.5:
            return int(number) - 1
        else:
            return int(number)

=======
Suggestion 5

def main():
    x = float(input())
    print(int(x + 0.5))

=======
Suggestion 6

def main():
    x = float(input())
    print(round(x))

=======
Suggestion 7

def main():
    x = float(input())
    print(int(round(x)))

=======
Suggestion 8

def round(x):
    if x % 1 >= 0.5:
        return int(x) + 1
    else:
        return int(x)

x = float(input())
print(round(x))

This is the first time I've ever written a program in Python, so I'm not sure if this is the best way to do it. It seems to work fine, though.

I'm not sure if there's a better way to do this, but I would probably use the round function.
