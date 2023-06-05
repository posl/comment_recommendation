Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x = float(input())
    print(int(x+0.5))

=======
Suggestion 2

def main():
    x = float(input())
    print(round(x))

=======
Suggestion 3

def main():
    x = input()
    print(int(x))

=======
Suggestion 4

def main():
    x = input()
    print(int(float(x) + 0.5))

=======
Suggestion 5

def round_number(x):
    # Write your code here.
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    if '.' in x:
        x = x.split('.')
        if int(x[1][0]) >= 5:
            return int(x[0])+1
        else:
            return int(x[0])
    else:
        return int(x)

=======
Suggestion 6

def main():
    x = input()
    print(round(float(x)))

main()

=======
Suggestion 7

def main():
    x = input()
    print(round(float(x)))

=======
Suggestion 8

def round_off(x):
    x = float(x)
    if x.is_integer():
        return int(x)
    else:
        return round(x)

=======
Suggestion 9

def main():
    x = input()
    if '.' in x:
        i = x.index('.')
        x = x[:i]
    print(x)
