Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x = input()
    if '.' in x:
        print(x[:x.index('.')])
    else:
        print(x)

=======
Suggestion 2

def main():
    x = input()
    if x.find('.') == -1:
        print(x)
    else:
        print(x[0:x.find('.')])

=======
Suggestion 3

def main():
    X = input()
    if '.' in X:
        print(X[:X.find('.')])
    else:
        print(X)

=======
Suggestion 4

def main():
    X = input()
    if X.find('.') != -1:
        X = X[:X.find('.')]
    print(X)

=======
Suggestion 5

def main():
    x = input()
    if x.find('.') == -1:
        print(x)
    else:
        print(x[:x.find('.')])
    return

=======
Suggestion 6

def main():
    x = float(input())
    print(int(x))

=======
Suggestion 7

def main():
    X = float(input())
    print(int(X))

=======
Suggestion 8

def main():
    x = input()
    print(int(x.split('.')[0]))

main()

=======
Suggestion 9

def main():
    x = input()
    print(int(x))

=======
Suggestion 10

def main():
    print(int(input().split('.')[0]))
