Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    X = int(input())
    if X == 0:
        print('No')
    elif X % 100 == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    x = int(input())
    if x % 100 == 0 and x != 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    x = int(input())
    if x % 100 == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    x = int(input())
    if x % 100 == 0 and x != 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    x = int(input())
    if x % 100 == 0 and x <= 1000:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    # input
    X = int(input())

    # compute

    # output
    if X%100 == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def purse(x):
    if x % 100 == 0 and x <= 1000 and x >= 0:
        return "Yes"
    else:
        return "No"

print purse(500)
print purse(40)
print purse(0)

=======
Suggestion 8

def purse(x):
    if x % 100 == 0:
        return "Yes"
    else:
        return "No"

x = int(input())
print(purse(x))

=======
Suggestion 9

def main():
    #write your code below this line
    x = int(input())
    if x % 100 == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 10

def main():
    # Take input from standard input
    X = int(input())
    # Check if X is divisible by 100
    if X % 100 == 0:
        # If yes, print Yes
        print("Yes")
    else:
        # If no, print No
        print("No")
