Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B, C = map(int, input().split())
    print(A + B + C - min(A, B, C))

=======
Suggestion 2

def main():
    A, B, C = map(int, input().split())
    print(max(A + B, B + C, C + A))

=======
Suggestion 3

def main():
    a, b, c = map(int, input().split())
    print(max(a+b, b+c, c+a))

=======
Suggestion 4

def main():
    A, B, C = map(int, input().split())
    print(max(A + B, B + C, A + C))

=======
Suggestion 5

def main():
    a,b,c = map(int,input().split())
    print(max(a+b,a+c,b+c))

main()

=======
Suggestion 6

def main():
    A,B,C = map(int,input().split())
    print(max(A+B,A+C,B+C))

=======
Suggestion 7

def main():
    numbers = input().split()
    numbers = [int(i) for i in numbers]
    numbers.sort()
    print(numbers[1] + numbers[2])

=======
Suggestion 8

def main():
    #input
    A,B,C = map(int,input().split())
    #output
    print(max(A+B,A+C,B+C))

=======
Suggestion 9

def main():
    # read input
    a, b, c = input().split()
    # convert to int
    a = int(a)
    b = int(b)
    c = int(c)
    # find the max of the three
    if (a > b) and (a > c):
        max = a
    elif (b > a) and (b > c):
        max = b
    elif (c > a) and (c > b):
        max = c
    # find the min of the three
    if (a < b) and (a < c):
        min = a
    elif (b < a) and (b < c):
        min = b
    elif (c < a) and (c < b):
        min = c
    # print the sum of the other two
    print(a+b+c-max-min)

main()
