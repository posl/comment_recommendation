Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def relu(x):
    if x >= 0:
        return x
    else:
        return 0

x = int(input())
print(relu(x))

=======
Suggestion 2

def relu(x):
    if x < 0:
        return 0
    else:
        return x

x = int(input())
print(relu(x))

=======
Suggestion 3

def relu(x):
    return max(0, x)

x = int(input())
print(relu(x))
