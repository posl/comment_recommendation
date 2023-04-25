Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    AB, BC, CA = map(int, input().split())
    print(AB * BC // 2)

=======
Suggestion 2

def area_of_triangle(a,b,c):
    s = (a + b + c)/2
    return (s*(s-a)*(s-b)*(s-c)) ** 0.5

a, b, c = [int(x) for x in input().split()]
print(int(area_of_triangle(a,b,c)))

=======
Suggestion 3

def main():
    AB, BC, CA = map(int, input().split())
    area = int((AB*BC)/2)
    print(area)

=======
Suggestion 4

def main():
    sides = list(map(int, input().split()))
    print(sides[0] * sides[1] // 2)

=======
Suggestion 5

def main():
    # Read input
    ab, bc, ca = map(int, input().split())

    # Calculate area
    area = (ab * bc) // 2

    # Print area
    print(area)

=======
Suggestion 6

def main():
    # Read the three sides of the triangle
    AB, BC, CA = map(int, input().split())
    # Calculate the area of the triangle
    area = (AB*BC)//2
    # Print the area of the triangle
    print(area)

=======
Suggestion 7

def main():
    # Get input
    ab, bc, ca = map(int, input().split())
    # Calculate area of triangle
    area = (ab * bc) // 2
    # Print area of triangle
    print(area)

=======
Suggestion 8

def main():
    # get the input
    ab, bc, ca = map(int, input().split())
    # get the area of the triangle
    area = (ab * bc) // 2
    # print the area
    print(area)

=======
Suggestion 9

def main():
    # Read the three sides of the triangle
    a, b, c = map(int, input().split())
    # Calculate the area of the triangle
    area = int(a * b * c / 2)
    # Output the result
    print(area)

=======
Suggestion 10

def main():
    #read input
    AB, BC, CA = map(int, input().split())
    #calculation
    S = (AB * BC) // 2
    #output
    print(S)
