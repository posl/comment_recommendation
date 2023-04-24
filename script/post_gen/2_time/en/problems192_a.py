Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x = int(input())
    if x % 100 == 0:
        print(0)
    else:
        print(100 - x % 100)

=======
Suggestion 2

def main():
    X = int(input())
    if X % 100 == 0:
        print(0)
    else:
        print(100 - X % 100)

=======
Suggestion 3

def main():
    x = int(input())
    print(100 - x % 100 if x % 100 != 0 else 0)

=======
Suggestion 4

def main():
    x = int(input())
    if x%100 == 0:
        print(0)
    else:
        print(100 - (x%100))

=======
Suggestion 5

def main():
    X = int(input())
    if X % 100 == 0:
        print("100")
    else:
        print(100 - X % 100)

=======
Suggestion 6

def main():
    x = int(input())
    print(100 - (x % 100))

=======
Suggestion 7

def main():
    x = int(input())
    print(100 - x % 100)

=======
Suggestion 8

def main():
    # Read the input
    X = int(input())
    # Find the number of coins needed to get the next prize
    coins_needed = 100 - (X % 100)
    # Print the result
    print(coins_needed)
