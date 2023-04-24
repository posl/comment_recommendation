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
    if '.' in x:
        print(int(x.split('.')[0]))
    else:
        print(x)

=======
Suggestion 3

def main():
    x = input()
    if '.' in x:
        x = x.split('.')[0]
    print(x)

=======
Suggestion 4

def main():
    n = input()
    if n.find('.') != -1:
        n = n[:n.find('.')]
    print(n)

=======
Suggestion 5

def main():
    x = input()
    print(int(x))

=======
Suggestion 6

def main():
    x = input()
    print(int(float(x)))

=======
Suggestion 7

def main():
    x = input()
    print(int(x.split('.')[0]))
