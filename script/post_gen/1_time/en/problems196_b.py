Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    X = input()
    if '.' in X:
        print(X.split('.')[0])
    else:
        print(X)

=======
Suggestion 2

def main():
    x = input()
    if '.' in x:
        print(x[:x.index('.')])
    else:
        print(x)

=======
Suggestion 3

def main():
    x = input()
    if x.find('.') == -1:
        print(x)
    else:
        print(x[:x.find('.')])

=======
Suggestion 4

def main():
    x = input()
    if x.find('.') != -1:
        print(x[0:x.find('.')])
    else:
        print(x)

=======
Suggestion 5

def main():
    X = input()
    print(int(float(X)))

=======
Suggestion 6

def main():
    x = input()
    print(int(x))

=======
Suggestion 7

def main():
    x = input()
    print(int(float(x)))

=======
Suggestion 8

def main():
    a = input()
    b = a.split(".")
    print(int(b[0]))
