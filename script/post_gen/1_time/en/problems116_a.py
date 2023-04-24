Synthesizing 10/10 solutions

=======
Suggestion 1

def area(a,b,c):
    s = (a+b+c)/2
    return (s*(s-a)*(s-b)*(s-c))**0.5

a,b,c = map(int,input().split())
print(int(area(a,b,c)))

=======
Suggestion 2

def main():
    AB, BC, CA = input().split()
    AB = int(AB)
    BC = int(BC)
    CA = int(CA)
    print(int((AB * BC)/2))

=======
Suggestion 3

def main():
    AB, BC, CA = map(int, input().split())
    print((AB * BC) // 2)

=======
Suggestion 4

def main():
    a, b, c = map(int, input().split())
    print((a * b * c) // (4 * (a * b + b * c + c * a)**0.5))

=======
Suggestion 5

def main():
    # Read the input
    ab, bc, ca = map(int, input().split())
    # Calculate the area
    area = int((ab * bc) / 2)
    # Print the result
    print(area)

=======
Suggestion 6

def main():
    #Read the input
    ab, bc, ca = map(int, input().split())
    #Calculate the area
    area = int((ab * bc) / 2)
    #Print the area
    print(area)

=======
Suggestion 7

def main():
    # Get the input
    AB, BC, CA = map(int, input().split())

    # Calculate the area
    area = (AB * BC) // 2

    # Output the result
    print(area)

=======
Suggestion 8

def main():
    # Write your code here
    a, b, c = map(int, input().split())
    print((a*b)//2)

=======
Suggestion 9

def main():
    #input the values of the sides
    a, b, c = map(int, input().split())
    #calculate the area of the triangle
    area = int(a * b * 0.5)
    #print the area of the triangle
    print(area)

main()

=======
Suggestion 10

def main():
    print("Welcome to the right triangle area calculator!")
    print("Please enter the lengths of the three sides of the triangle, one at a time.")
    ab = int(input("Please enter the length of side AB: "))
    bc = int(input("Please enter the length of side BC: "))
    ca = int(input("Please enter the length of side CA: "))
    print("The area of the triangle is: " + str((ab * bc) / 2))
