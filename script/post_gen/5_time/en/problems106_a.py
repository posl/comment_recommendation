Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    print((a-1) * (b-1))

=======
Suggestion 2

def area(a, b):
    return a*b - (a+b-1)

a, b = map(int, input().split())
print(area(a, b))

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    print(a*b-1)

=======
Suggestion 4

def main():
    a,b = map(int, input().split())
    print(a*b - (a+b) +1)

=======
Suggestion 5

def area(a,b):
    return a*b
a,b = map(int, input().split())
print(area(a,b)-a-b+1)

=======
Suggestion 6

def area():
    A,B = input().split()
    A = int(A)
    B = int(B)
    print(A*B-1)

area()

=======
Suggestion 7

def get_area(a, b):
    return a * b - (a + b - 1)

=======
Suggestion 8

def main():
    # Take input
    input_line = input()
    input_line = input_line.split()
    #print(input_line)
    #print(type(input_line))
    #print(len(input_line))
    #print(input_line[0])
    #print(input_line[1])
    #print(type(input_line[0]))
    #print(type(input_line[1]))
    #print(int(input_line[0]))
    #print(int(input_line[1]))
    #print(type(int(input_line[0])))
    #print(type(int(input_line[1])))
    #print(int(input_line[0]) * int(input_line[1]))
    #print(type(int(input_line[0]) * int(input_line[1])))
    #print(int(input_line[0]) * int(input_line[1]) - (int(input_line[0]) + int(input_line[1]) - 1))
    #print(type(int(input_line[0]) * int(input_line[1]) - (int(input_line[0]) + int(input_line[1]) - 1)))
    # Print output
    print(int(input_line[0]) * int(input_line[1]) - (int(input_line[0]) + int(input_line[1]) - 1))

=======
Suggestion 9

def area(a,b):
    return a*b

=======
Suggestion 10

def area(A,B):
    return A*B-1
