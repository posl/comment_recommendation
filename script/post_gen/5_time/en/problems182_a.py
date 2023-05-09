Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    if b < 2 * a + 100:
        print(2 * a + 100 - b)
    else:
        print(0)

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    print(2 * a + 100 - b)

=======
Suggestion 3

def main():
    A, B = map(int, input().split())
    print(2*A+100-B)

=======
Suggestion 4

def max_follow(a,b):
    if a <= 2*b + 100:
        return 2*b + 100 - a
    else:
        return 0

=======
Suggestion 5

def main():
    a,b = map(int,raw_input().split())
    print (2*a+100)-b
