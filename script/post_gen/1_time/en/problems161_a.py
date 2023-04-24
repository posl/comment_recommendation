Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x, y, z = map(int, input().split())
    print(z, x, y)

=======
Suggestion 2

def main():
    X, Y, Z = map(int, input().split())
    print(Z, X, Y)

=======
Suggestion 3

def main():
    a = input().split()
    for i in range(len(a)):
        a[i] = int(a[i])
    a[0], a[1] = a[1], a[0]
    a[0], a[2] = a[2], a[0]
    for i in a:
        print(i, end=' ')

=======
Suggestion 4

def main():
    x,y,z = map(int, input().split())
    x,y = y,x
    x,z = z,x
    print(x,y,z)

=======
Suggestion 5

def main():
    #Read input
    X, Y, Z = map(int, input().split())
    #Swap the contents of the boxes A and B
    A = Y
    B = X
    #Swap the contents of the boxes A and C
    C = Z
    #Print the integers contained in the boxes A, B, and C, in this order, with space in between.
    print(A, B, C)

=======
Suggestion 6

def main():
    num1, num2, num3 = map(int, input().split())
    print(num3, num1, num2)

=======
Suggestion 7

def main():
    #Get Input
    x,y,z = map(int, input().split())
    #Swap the contents of the boxes A and B
    x,y = y,x
    #Swap the contents of the boxes A and C
    x,z = z,x
    #Print Output
    print(x,y,z)
