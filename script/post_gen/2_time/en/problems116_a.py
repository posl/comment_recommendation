Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, b, c = map(int, input().split())
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    print(int(area))

=======
Suggestion 2

def area(a,b,c):
    s = (a+b+c)/2
    return (s*(s-a)*(s-b)*(s-c))**0.5

a,b,c = map(int,input().split())
print(int(area(a,b,c)))

=======
Suggestion 3

def area(a,b,c):
    s = (a+b+c)/2
    return (s*(s-a)*(s-b)*(s-c))**0.5

=======
Suggestion 4

def main():
    AB, BC, CA = map(int, input().split())
    print((AB * BC) // 2)

=======
Suggestion 5

def main():
    AB, BC, CA = map(int, input().split())
    print(int(AB * BC / 2))

=======
Suggestion 6

def main():
    # read the input
    AB, BC, CA = map(int, input().split())

    # calculate the area
    area = int((AB * BC) / 2)

    # print the area
    print(area)

=======
Suggestion 7

def main():
    #input
    AB, BC, CA = map(int, input().split())
    #processing
    area = (AB*BC)//2
    #output
    print(area)

=======
Suggestion 8

def main():
    # Read input
    a, b, c = map(int, input().split())
    # Calculate area
    area = (a * b) // 2
    # Print area
    print(area)

=======
Suggestion 9

def  main():
    AB, BC, CA =  map ( int , input().split())
    print( int ((AB * BC) / 2 ))

=======
Suggestion 10

def main():
    A,B,C = map(int,input().split())
    print(int((A*B)/2))
