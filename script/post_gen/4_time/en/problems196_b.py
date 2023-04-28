Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x = input()
    if '.' in x:
        print(x.split('.')[0])
    else:
        print(x)

=======
Suggestion 2

def main():
    x = input()
    if "." in x:
        print(int(x.split(".")[0]))
    else:
        print(x)

=======
Suggestion 3

def main():
    x = float(input())
    print(int(x))

=======
Suggestion 4

def round_down(x):
    if x.find('.') == -1:
        return x
    else:
        return x[:x.find('.')]

=======
Suggestion 5

def main():
    X = float(input())
    print(int(X))

=======
Suggestion 6

def round_down(x):
    return int(x)

x = float(input())
print(round_down(x))

=======
Suggestion 7

def main():
    x = float(input().strip())
    print(int(x))

=======
Suggestion 8

def problem196_b():
    x = float(input())
    print(int(x))

=======
Suggestion 9

def round_down(x):
    return int(x)
