Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a1, a2, a3, a4 = map(int, input().split())
    print(min(a1, a2, a3, a4))

=======
Suggestion 2

def main():
    a = list(map(int, input().split()))
    print(min(a[0], a[1], a[2], a[3]))

=======
Suggestion 3

def main():
    # Get input here
    A1, A2, A3, A4 = map(int, input().strip().split())
    # Calculate result here
    result = 0
    if A1 <= 100 and A2 <= 100 and A3 <= 100 and A4 <= 100:
        result = 1
    # Print output here
    print(result)

=======
Suggestion 4

def main():
    A = list(map(int, input().split()))
    print(min(A))

=======
Suggestion 5

def main():
    a = list(map(int, input().split()))
    print(min(a))

=======
Suggestion 6

def main():
    a = list(map(int, input().split()))
    a.sort()
    print(a[2]+a[3])

=======
Suggestion 7

def main():
    a = input().split()
    a = [int(i) for i in a]
    print(min(a))

=======
Suggestion 8

def main():
    a = input()
    a = a.split()
    a = list(map(int, a))
    print(min(a))

=======
Suggestion 9

def main():
    a = input().split()
    print(min(a))
