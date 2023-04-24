Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    r, c = map(int, input().split())
    if (r % 2 == 0 and c % 2 == 0) or (r % 2 == 1 and c % 2 == 1):
        print("black")
    else:
        print("white")

main()

=======
Suggestion 2

def main():
    R, C = map(int, input().split())
    if R % 2 == 0:
        if C % 2 == 0:
            print("white")
        else:
            print("black")
    else:
        if C % 2 == 0:
            print("black")
        else:
            print("white")

=======
Suggestion 3

def main():
    R, C = map(int, input().split())
    if (R % 2 == 0 and C % 2 == 0) or (R % 2 != 0 and C % 2 != 0):
        print('black')
    else:
        print('white')

=======
Suggestion 4

def main():
    R, C = map(int, input().split())
    if (R + C) % 2 == 0:
        print("black")
    else:
        print("white")

main()

=======
Suggestion 5

def main():
    r, c = map(int, input().split())
    if (r * c) % 2 == 0:
        print('black')
    else:
        print('white')

main()

=======
Suggestion 6

def main():
    r, c = map(int, input().split())
    if r % 2 == c % 2:
        print("black")
    else:
        print("white")

=======
Suggestion 7

def main():
    # input
    R, C = map(int, input().split())

    # compute
    if (R*C)%2 == 0:
        ans = 'black'
    else:
        ans = 'white'

    # output
    print(ans)

=======
Suggestion 8

def main():
    R, C = map(int, input().split())
    if (R*C) % 2 == 0:
        print('white')
    else:
        print('black')

=======
Suggestion 9

def main():
    # Read the input
    r, c = map(int, input().split())

    # Print the output
    if (r + c) % 2 == 0:
        print("black")
    else:
        print("white")

=======
Suggestion 10

def main():
    #write your code below this line
    pass
