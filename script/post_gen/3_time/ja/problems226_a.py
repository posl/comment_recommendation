Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def my_round(x, d=0):
    p = 10 ** d
    return (x * p * 2 + 1) // 2 / p

x = input()
print(int(my_round(float(x), 0)))

=======
Suggestion 2

def round(x):
    if x - int(x) >= 0.5:
        return int(x) + 1
    else:
        return int(x)

x = float(input())
print(round(x))

=======
Suggestion 3

def rounding(x):
    x = x * 10
    x = int(x)
    if x % 10 >= 5:
        x = int(x / 10) + 1
    else:
        x = int(x / 10)
    return x

print(rounding(float(input())))

=======
Suggestion 4

def main():
    # input
    X = float(input())

    # compute

    # output
    print(round(X, 0))

=======
Suggestion 5

def main():
    X = float(input())
    print(int(X*10+0.5)//10)

=======
Suggestion 6

def main():
    x = float(input())
    print(round(x))

=======
Suggestion 7

def main():
    x = float(input())
    print(int(x + 0.5))

=======
Suggestion 8

def main():
    x = float(input())
    print(int(round(x, 1)))

=======
Suggestion 9

def round_float_str(x):
    return str(int(round(float(x))))
