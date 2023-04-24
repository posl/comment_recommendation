Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b, c = map(int, input().split())
    for i in range(a, b+1):
        if i % c == 0:
            print(i)
            break
    else:
        print(-1)

main()

I am trying to make a program that will take a string input and output the number of vowels and consonants in the string. I have made the program work, but I am getting an error when I input a string with a space in it. I have tried using .strip() and .replace() but neither of those work.

=======
Suggestion 2

def main():
    A, B, C = map(int, input().split())
    for i in range(A, B + 1):
        if i % C == 0:
            print(i)
            return
    print(-1)

=======
Suggestion 3

def main():
    a, b, c = map(int, input().split())
    for i in range(a, b+1):
        if i % c == 0:
            print(i)
            return
    print(-1)

=======
Suggestion 4

def main():
    a,b,c = map(int, input().split())
    for i in range(a,b+1):
        if i % c == 0:
            print(i)
            break
    else:
        print(-1)

=======
Suggestion 5

def main():
    A,B,C = map(int,input().split())
    for i in range(A,B+1):
        if i%C == 0:
            print(i)
            break
    else:
        print(-1)

=======
Suggestion 6

def main():
    # Get the input
    A, B, C = [int(x) for x in input().split()]
    # Find the first multiple of C
    # between A and B
    for i in range(A, B + 1):
        if i % C == 0:
            print(i)
            return
    # If there is no multiple of C
    # between A and B
    print(-1)
