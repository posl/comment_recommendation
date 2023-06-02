Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def max(a,b):
    if a>b:
        return a
    else:
        return b

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    print(max(a+b, a-b, a*b))

=======
Suggestion 3

def get_max(a, b):
    add = a + b
    sub = a - b
    mul = a * b
    return max(add, sub, mul)

=======
Suggestion 4

def max_num(a, b):
    if a + b > a - b:
        if a + b > a * b:
            return a + b
        else:
            return a * b
    else:
        if a - b > a * b:
            return a - b
        else:
            return a * b
