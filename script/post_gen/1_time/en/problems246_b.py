Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B = map(int, input().split())
    d = (A ** 2 + B ** 2) ** 0.5
    print(A / d, B / d)

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    print(a / (a + b), b / (a + b))

=======
Suggestion 3

def main():
    A, B = map(int, input().split())
    print(A / (A + B), B / (A + B))

=======
Suggestion 4

def main():
    A, B = map(int, input().split())
    d = (A**2 + B**2)**(0.5)
    x = A / d
    y = B / d
    print(x, y)

=======
Suggestion 5

def main():
    A,B = map(int,input().split())
    #print(A,B)
    d = (A**2 + B**2)**0.5
    print(A/d,B/d)

=======
Suggestion 6

def main():
    # Read the input
    A, B = map(int, input().split())

    # Compute the length of the segment (0,0) -> (A,B)
    L = (A**2 + B**2)**0.5

    # Compute the coordinates of the point on the segment (0,0) -> (A,B)
    # whose distance from (0,0) is 1
    x = A/L
    y = B/L

    # Print the coordinates
    print(x, y)

=======
Suggestion 7

def main():
    #input
    ab = list(map(int,input().split()))
    a = ab[0]
    b = ab[1]
    #process
    #output
    print(a/(a+b),b/(a+b))

=======
Suggestion 8

def main():
    A,B = map(int,input().split())
    print(A/(A+B),B/(A+B))

main()

I have been learning Python for a while now, and I have been trying to create a program that will take a string of text and then count the number of times each letter appears in the text. I have tried a few different ways to do this, but I have not been able to get it to work. Here is an example of what I am trying to do:
