Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x, y = map(int, input().split())

    if x == 0 and y == 1:
        print(2)
    elif x == 0 and y == 2:
        print(0)
    elif x == 1 and y == 0:
        print(0)
    elif x == 1 and y == 2:
        print(1)
    elif x == 2 and y == 0:
        print(1)
    elif x == 2 and y == 1:
        print(2)
    else:
        print(x)

=======
Suggestion 2

def main():
    x, y = map(int, input().split())
    if (x + y) % 3 == 0:
        print(0)
    elif (x + y) % 3 == 1:
        print(1)
    else:
        print(2)

=======
Suggestion 3

def main():
    x, y = input().split()
    x = int(x)
    y = int(y)
    if x == 0 and y == 1:
        print(2)
    elif x == 0 and y == 2:
        print(0)
    elif x == 1 and y == 0:
        print(0)
    elif x == 1 and y == 2:
        print(1)
    elif x == 2 and y == 0:
        print(1)
    elif x == 2 and y == 1:
        print(2)
    else:
        print(x)

=======
Suggestion 4

def main():
    x, y = map(int, input().split())
    if x == y:
        print(x)
    else:
        print(3 - x - y)

main()

=======
Suggestion 5

def main():
    x, y = map(int, input().split())
    if x == y:
        print(x)
    else:
        print(3 - x - y)

=======
Suggestion 6

def main():
    x, y = map(int, input().split())
    if x == y:
        print(x)
    elif x == 0 and y == 2:
        print(1)
    elif x == 1 and y == 0:
        print(2)
    elif x == 2 and y == 1:
        print(0)
    elif x == 0 and y == 1:
        print(0)
    elif x == 1 and y == 2:
        print(1)
    elif x == 2 and y == 0:
        print(2)

=======
Suggestion 7

def main():
    x,y = map(int, input().split())
    if x == 0 and y == 1:
        print('2')
    elif x == 0 and y == 2:
        print('0')
    elif x == 1 and y == 0:
        print('2')
    elif x == 1 and y == 2:
        print('1')
    elif x == 2 and y == 0:
        print('0')
    elif x == 2 and y == 1:
        print('1')
    else:
        print(x)

=======
Suggestion 8

def main():
    # Read the input
    x, y = map(int, input().split())
    # Calculate the answer
    if x == y:
        answer = x
    elif x != y:
        answer = 3 - x - y
    # Print the answer
    print(answer)

=======
Suggestion 9

def main():
    x, y = map(int, input().split())
    print((x + 1) % 3)

main()

This is a very simple problem, and I think it is better to solve it without using any extra libraries. I have used the map function to map the input to an integer. I have used the modulo operator to find the remainder of the sum of x and 1 divided by 3. The remainder will be the answer.

The problem is solved.

Thank you for reading this post. I hope you liked it. If you have any questions or suggestions, please feel free to comment below.

I hope you have a nice day.

See you in the next post.

Happy Coding! 🙂

Related
