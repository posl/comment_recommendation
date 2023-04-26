Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x = int(input())
    if x >= 0:
        print(x)
    else:
        print(0)

main()

=======
Suggestion 2

def main():
    x = int(input())
    if x >= 0:
        print(x)
    else:
        print(0)

=======
Suggestion 3

def relu(x):
    if x < 0:
        return 0
    else:
        return x

x = int(input())
print(relu(x))

=======
Suggestion 4

def main():
    x = int(input())
    if x > 0:
        print(x)
    else:
        print(0)

=======
Suggestion 5

def relu(x):
    if x > 0:
        return x
    else:
        return 0

=======
Suggestion 6

def relu(x):
    if x < 0:
        x = 0
    return x

x = int(input())
print(relu(x))

=======
Suggestion 7

def main():
    x = int(input())
    print(max(x, 0))
