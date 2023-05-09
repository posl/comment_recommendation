Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    mountains = []
    for i in range(n):
        mountains.append(input().split())
    mountains = sorted(mountains, key=lambda x: int(x[1]), reverse=True)
    print(mountains[1][0])

=======
Suggestion 2

def main():
    n = int(input())
    mountains = []
    for _ in range(n):
        mountains.append(input().split())
    mountains.sort(key=lambda x: int(x[1]), reverse=True)
    print(mountains[1][0])

=======
Suggestion 3

def main():
    N = int(input())
    mountains = []
    for i in range(N):
        S, T = input().split()
        T = int(T)
        mountains.append((S, T))
    mountains.sort(key=lambda x: x[1], reverse=True)
    print(mountains[1][0])

=======
Suggestion 4

def main():
    n = int(input())
    mountains = []
    for i in range(n):
        mountains.append(input().split(" "))
    mountains.sort(key=lambda x: int(x[1]), reverse=True)
    print(mountains[1][0])

=======
Suggestion 5

def main():
    N = int(input())
    mountains = []
    for i in range(N):
        mountain = input().split()
        mountains.append(mountain)
    mountains.sort(key=lambda x: int(x[1]), reverse=True)
    print(mountains[1][0])

=======
Suggestion 6

def main():
    n = int(input())
    mountains = {}
    for i in range(n):
        s, t = input().split()
        mountains[s] = int(t)
    mountains = sorted(mountains.items(), key=lambda x:x[1], reverse=True)
    print(mountains[1][0])

=======
Suggestion 7

def main():
    N = int(input())
    mountains = []
    for i in range(N):
        mountains.append(input().split())

    mountains.sort(key=lambda x: int(x[1]), reverse=True)

    print(mountains[1][0])

=======
Suggestion 8

def problem201_b():
    n = int(input())
    mountains = []
    for i in range(n):
        name, height = input().split()
        mountains.append((name, int(height)))
    mountains.sort(key=lambda x: x[1], reverse=True)
    print(mountains[1][0])

=======
Suggestion 9

def main():
    N = int(input())
    mountains = []
    for i in range(N):
        mountains.append(input().split())

    mountains = sorted(mountains, key=lambda mountain: mountain[1], reverse=True)

    print(mountains[1][0])

=======
Suggestion 10

def main():
    # Read from stdin
    n = int(input())
    # Initialize variables
    mountains = {}
    for i in range(n):
        # Read from stdin
        name, height = input().split()
        # Add to dictionary
        mountains[name] = int(height)
    # Find the second highest mountain
    second_highest = sorted(mountains.items(), key=lambda x: x[1], reverse=True)[1][0]
    # Print to stdout
    print(second_highest)
