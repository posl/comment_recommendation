Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x,a = map(int,input().split())
    if x < a:
        print(0)
    else:
        print(10)

=======
Suggestion 2

def main():
    input_data = input()
    X = int(input_data.split()[0])
    A = int(input_data.split()[1])
    if X < A:
        print(0)
    else:
        print(10)

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    if a < b:
        print(0)
    else:
        print(10)

=======
Suggestion 4

def f(x,a):
    if x < a:
        return 0
    else:
        return 10

=======
Suggestion 5

def compare(x, a):
    if x < a:
        print(0)
    else:
        print(10)
