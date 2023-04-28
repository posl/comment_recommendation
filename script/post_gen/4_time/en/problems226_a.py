Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x = float(input())
    if x % 1 >= 0.5:
        print(int(x) + 1)
    else:
        print(int(x))

main()

=======
Suggestion 2

def main():
    x = float(input())
    if x % 1 >= 0.5:
        print(int(x) + 1)
    else:
        print(int(x))

=======
Suggestion 3

def main():
    X = float(input())
    if X % 1 >= 0.5:
        print(int(X + 1))
    else:
        print(int(X))

=======
Suggestion 4

def round_to_nearest_integer(x):
    if x % 1 >= 0.5:
        return int(x) + 1
    else:
        return int(x)

=======
Suggestion 5

def main():
    X = float(input())
    print(int(X+0.5))

=======
Suggestion 6

def main():
    x = float(input())
    print(round(x))

=======
Suggestion 7

def main():
    X = float(input())
    print(int(round(X,0)))

=======
Suggestion 8

def round_to_nearest_integer(x):
    return round(x)

=======
Suggestion 9

def roundUp(num):
    return int(num) + 1
