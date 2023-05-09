Synthesizing 10/10 solutions

=======
Suggestion 1

def swap(a, b):
    return b, a

a, b, c = map(int, input().split())
a, b = swap(a, b)
a, c = swap(a, c)
print(a, b, c)

=======
Suggestion 2

def swap(a, b):
    return b, a

a, b, c = input().split()
a, b = swap(a, b)
a, c = swap(a, c)
print(a, b, c)

=======
Suggestion 3

def swap(a,b):
    temp = a
    a = b
    b = temp
    return a,b

=======
Suggestion 4

def main():
    input_str = input()
    input_list = input_str.split(" ")
    x = input_list[0]
    y = input_list[1]
    z = input_list[2]
    print(z + " " + x + " " + y)

=======
Suggestion 5

def main():
    a = input().split()
    print(a[2] + " " + a[0] + " " + a[1])

=======
Suggestion 6

def main():
    # Get input here
    X, Y, Z = map(int, input().split())
    # Calculate result here
    print(Z, X, Y)
    # Print output here

=======
Suggestion 7

def main():
    a,b,c = map(int,input().split())
    print(c,a,b)

=======
Suggestion 8

def main():
    X,Y,Z = map(int, input().split())
    print(Z,X,Y)

=======
Suggestion 9

def main():
    # Take input
    x,y,z = map(int, input().split())
    # Print output
    print(z,x,y)

=======
Suggestion 10

def swap(a,b):
    return b,a
