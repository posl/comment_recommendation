Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    if a > b:
        print(0)
    else:
        print(b - a + 1)

=======
Suggestion 2

def main():
    a, b = input().split()
    a = int(a)
    b = int(b)
    if (a >= 1 and a <= 100) and (b >= 1 and b <= 100):
        if a <= b:
            print(b - a + 1)
        else:
            print(0)

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    print(b - a + 1 if b - a >= 0 else 0)

=======
Suggestion 4

def main():
    input_line = input()
    input_line = input_line.split()
    a = int(input_line[0])
    b = int(input_line[1])
    if a > b:
        print(0)
    else:
        print(b - a + 1)

main()

=======
Suggestion 5

def solve():
    a, b = map(int, input().split())
    print(max(0, b - a + 1))

=======
Suggestion 6

def main():
    # Get input here
    a, b = map(int, input().strip().split())
    # Calculate result here
    if a > b:
        print(0)
    else:
        print(b-a+1)
    # Print output here

main()

=======
Suggestion 7

def main():
    a, b = map(int, input().split())
    print(b-a+1 if b>=a else 0)

=======
Suggestion 8

def main():
    # get input
    a, b = map(int, input().split())
    if a > b:
        print(0)
    else:
        print(b - a + 1)

=======
Suggestion 9

def main():
    a,b = map(int, input().split())
    print(max(0,b-a+1))
