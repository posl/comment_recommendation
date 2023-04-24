Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b, c = map(int, input().split())
    a, b = b, a
    a, c = c, a
    print(a, b, c)

=======
Suggestion 2

def main():
    x, y, z = map(int, input().split())
    print(z, x, y)

=======
Suggestion 3

def main():
    a, b, c = map(int, input().split())
    print(c, a, b)

=======
Suggestion 4

def main():
    # A,B,C = map(int,input().split())
    A,B,C = 1,2,3
    A,B = B,A
    A,C = C,A
    print(A,B,C)

=======
Suggestion 5

def main():
    # Read input
    inputList = input().split()
    # Swap the contents of the boxes A and B
    inputList[0], inputList[1] = inputList[1], inputList[0]
    # Swap the contents of the boxes A and C
    inputList[0], inputList[2] = inputList[2], inputList[0]
    # Print the integers contained in the boxes A, B, and C, in this order, with space in between.
    print(' '.join(inputList))

=======
Suggestion 6

def main():
    #Write code here
    x, y, z = map(int, input().split())
    print(z, x, y)

=======
Suggestion 7

def main():
    # Read a line from stdin
    line = input()
    # Split the line into a list of strings
    line = line.split()
    # Convert the list of strings to a list of integers
    line = [int(i) for i in line]
    # Store the three integers in variables
    a, b, c = line
    # Swap the contents of the boxes A and B
    a, b = b, a
    # Swap the contents of the boxes A and C
    a, c = c, a
    # Print the integers contained in the boxes A, B, and C
    print(a, b, c)

=======
Suggestion 8

def main():
    # Enter your code here
    x,y,z=map(int,input().split())
    print(z,x,y)

main()
