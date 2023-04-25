Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A = int(input())
    B = int(input())
    if A == 1 and B == 2:
        print(3)
    elif A == 1 and B == 3:
        print(2)
    elif A == 2 and B == 1:
        print(3)
    elif A == 2 and B == 3:
        print(1)
    elif A == 3 and B == 1:
        print(2)
    elif A == 3 and B == 2:
        print(1)

=======
Suggestion 2

def main():
    a = int(input())
    b = int(input())
    for i in range(1,4):
        if i != a and i != b:
            print(i)

=======
Suggestion 3

def main():
    a = int(input())
    b = int(input())
    print(6 - a - b)

main()

=======
Suggestion 4

def main():
    a = int(input())
    b = int(input())
    print(6 - a - b)

=======
Suggestion 5

def main():
    a, b = [int(input()) for _ in range(2)]
    print(6 - a - b)

=======
Suggestion 6

def main():
    a = int(input())
    b = int(input())
    print(6-(a+b))
