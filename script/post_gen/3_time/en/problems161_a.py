Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def swap(a, b):
    a, b = b, a
    return a, b

x, y, z = map(int, input().split())
x, y = swap(x, y)
x, z = swap(x, z)
print(x, y, z)

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
    #read input
    A, B, C = map(int, input().split())
    #swap A and B
    A, B = B, A
    #swap A and C
    A, C = C, A
    #print output
    print(A, B, C)

main()

=======
Suggestion 5

def main():
    #input
    X, Y, Z = map(int, input().split())

    #output
    print(Z, X, Y)

=======
Suggestion 6

def main():
    #Get the input from the user
    x, y, z = map(int, input().split())

    #Swap the contents of the boxes A and B
    x, y = y, x

    #Swap the contents of the boxes A and C
    x, z = z, x

    #Print the integers contained in the boxes A, B, and C, in this order, with space in between.
    print(x, y, z)

=======
Suggestion 7

def main():
    # Read the numbers from the standard input
    X, Y, Z = map(int, input().split())
    # Swap the contents of the boxes A and B
    X, Y = Y, X
    # Swap the contents of the boxes A and C
    X, Z = Z, X
    # Print the integers contained in the boxes A, B, and C, in this order, with space in between.
    print(X, Y, Z)
