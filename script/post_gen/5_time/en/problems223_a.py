Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x = int(input())
    if x % 100 == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    x = int(input())
    if x < 100:
        print("No")
    elif x % 100 == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    X = int(input())
    if X % 100 == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    x = int(input())
    if x%100 == 0 and x != 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    x = int(input())

    if x % 100 == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    X = int(input())
    if X % 100 == 0 and X >= 100:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def solve():
    #import sys
    #input = sys.stdin.readline
    x = int(input())
    if x % 100 == 0 and x != 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    X = int(input())
    print('Yes' if X % 100 == 0 and X != 0 else 'No')

=======
Suggestion 9

def main():
    x=int(input())
    if x%100==0 and x!=0:
        print("Yes")
    else:
        print("No")

main()

=======
Suggestion 10

def isPossible(x):
    if x % 100 == 0:
        print("Yes")
    else:
        print("No")
