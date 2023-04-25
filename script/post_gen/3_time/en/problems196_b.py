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
    if x.find('.') == -1:
        print(x)
    else:
        print(x[:x.find('.')])

=======
Suggestion 3

def main():
    X = input()
    if "." in X:
        X = X.split(".")[0]
    print(X)

=======
Suggestion 4

def main():
    X = input().rstrip()
    if '.' not in X:
        print(X)
    else:
        print(X[0:X.index('.')])

=======
Suggestion 5

def main():
    X = input()
    print(int(X))

=======
Suggestion 6

def main():
    X = input()
    X = float(X)
    print(int(X))

=======
Suggestion 7

def main():
    x = input()
    print(int(float(x)))

=======
Suggestion 8

def round_down(x):
    return int(x)
