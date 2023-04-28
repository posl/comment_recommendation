Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    if a == 0:
        print(b)
    elif b == 0:
        print(a)
    else:
        print(3 - a - b)

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    print(2*b-a)

=======
Suggestion 3

def main():
    A, B = map(int, input().split())
    print(2 * A + B)

=======
Suggestion 4

def main():
    A, B = map(int, input().split())
    print(3 - A - B + A * B)

=======
Suggestion 5

def main():
    a,b = map(int, input().split())
    print(3-a-b)

=======
Suggestion 6

def main():
    a,b = map(int, input().split())
    c = 1
    while True:
        if a == b:
            print(c)
            exit()
        else:
            if a > b:
                b += 2 ** c
            else:
                a += 2 ** c
        c += 1

=======
Suggestion 7

def solve(a, b):
    return 3 - a - b

=======
Suggestion 8

def main():
    #get the input
    a, b = map(int, input().split())
    #print the result
    print(3-(a+b)//2)
