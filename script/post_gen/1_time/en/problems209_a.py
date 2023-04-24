Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    if a > b:
        print(0)
    else:
        print(b - a + 1)

=======
Suggestion 2

def count_integers(a, b):
    count = 0
    for i in range(a, b+1):
        count += 1
    return count

a, b = map(int, input().split())
print(count_integers(a, b))

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    print(max(0, b - a + 1))

=======
Suggestion 4

def main():
    A, B = map(int, input().split())
    print(max(0, B - A + 1))

=======
Suggestion 5

def solution():
    a, b = map(int, input().split())
    if a > b:
        print(0)
    else:
        print(b - a + 1)

solution()

=======
Suggestion 6

def main():
    # Get input here
    a, b = map(int, input().strip().split())
    # Calculate result here
    result = 0
    for i in range(a, b+1):
        result += 1
    # Print output here
    print(result)

=======
Suggestion 7

def findIntegers():
    A, B = map(int, input().split())
    if A > B:
        print(0)
    else:
        print(B - A + 1)

findIntegers()
