Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x = int(input())
    if x >= 0:
        print(x)
    else:
        print(0)

=======
Suggestion 2

def relu(x):
    if x >= 0:
        return x
    else:
        return 0

x = int(input())
print(relu(x))

=======
Suggestion 3

def relu(x):
    if x >= 0:
        return x
    else:
        return 0

=======
Suggestion 4

def relu(x):
    return max(0, x)

x = int(input())
print(relu(x))

=======
Suggestion 5

def main():
    x = int(input())
    print(max(0, x))
