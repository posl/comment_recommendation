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
    a, b, c = map(int, input().split())
    print(c, a, b)

=======
Suggestion 4

def main():
    A, B, C = map(int, input().split())
    print(C, A, B)

=======
Suggestion 5

def main():
    input_string = input()
    input_list = input_string.split()
    box_a = int(input_list[0])
    box_b = int(input_list[1])
    box_c = int(input_list[2])
    box_a, box_b = box_b, box_a
    box_a, box_c = box_c, box_a
    print(str(box_a) + " " + str(box_b) + " " + str(box_c))

=======
Suggestion 6

def main():
    #input
    x, y, z = map(int, input().split())
    #output
    print(z, x, y)

=======
Suggestion 7

def main():
    #read in the values
    a,b,c = map(int,input().split())
    #swap the values
    a,b = b,a
    a,c = c,a
    #print the values
    print(a,b,c)
