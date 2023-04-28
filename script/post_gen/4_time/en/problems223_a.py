Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    X = int(input())
    if X % 100 == 0 and X != 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    X = int(input())
    if X % 100 == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    x = int(input())
    if x%100 == 0 and x != 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    x = int(input())
    if x % 100 == 0 and x != 0:
        print('Yes')
    else:
        print('No')
main()

=======
Suggestion 5

def main():
    x = int(input())
    print("Yes" if x % 100 == 0 and x != 0 else "No")

=======
Suggestion 6

def main():
    x = int(input())
    print('Yes' if x % 100 == 0 and x != 0 else 'No')

=======
Suggestion 7

def main():
    x = int(input())
    print("Yes") if x >= 100 and x % 100 == 0 else print("No")

=======
Suggestion 8

def check():
    x = int(input())
    if x%100 == 0 and x>0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    # Take input Here and Call solution function
    x = int(input())
    solution(x)

=======
Suggestion 10

def problem223_a():
    # Store the input
    x = int(input())

    # Check if the value is between 0 and 1000
    if 0 <= x <= 1000:
        # Check if the value is divisible by 100
        if x % 100 == 0:
            print("Yes")
        else:
            print("No")
