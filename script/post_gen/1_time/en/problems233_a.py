Synthesizing 9/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x, y = map(int, input().split())
    print((y - x + 9) // 10)

=======
Suggestion 2

def main():
    X, Y = map(int, input().split())
    print((Y + 9) // 10 - X // 10)

=======
Suggestion 3

def main():
    x, y = map(int, input().split())
    print((y - x + 10 - 1) // 10)

=======
Suggestion 4

def main():
    X, Y = map(int, input().split())
    print((Y - X + 9) // 10)
main()

=======
Suggestion 5

def main():
    x,y = input().split()
    x = int(x)
    y = int(y)
    if x%10 == 0:
        x = x + 10
    else:
        x = x + (10 - x%10)
    count = 0
    while x < y:
        x = x + 10
        count = count + 1
    print(count)

=======
Suggestion 6

def main():
    # Read in input
    X, Y = map(int, input().split())
    # Calculate the minimum number of 10-yen stamps to add
    stamps = (Y - (X % Y)) % Y
    # Print the answer
    print(stamps)

=======
Suggestion 7

def main():
    #Get Input
    x, y = map(int, input().split())

    #Calculate the number of 10yen stamps needed
    stamps = y - x

    #Check to see if the stamps are already there
    if stamps <= 0:
        stamps = 0

    #Print the answer
    print(stamps)
