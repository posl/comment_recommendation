Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x = int(input())
    if x % 100 == 0:
        print(0)
    else:
        print(100 - (x % 100))

=======
Suggestion 2

def main():
    x = int(input())
    if x % 100 == 0:
        print(0)
    else:
        print(100 - x % 100)

=======
Suggestion 3

def main():
    x = int(input())
    if x % 100 == 0:
        print(100)
    else:
        print(100 - (x % 100))

=======
Suggestion 4

def main():
    x = int(input())
    print(100 - (x % 100))

=======
Suggestion 5

def main():
    X = int(input())
    print(100 - (X % 100))

=======
Suggestion 6

def main():
    x = int(input())
    print(100 - x%100)

=======
Suggestion 7

def main():
    X = int(input())
    print(100 - (X % 100))

main()

I used the modulo operator to find the remainder of X divided by 100, and then subtracted that from 100 to find the number of coins needed.
