Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    if (a * b) % 2 == 0:
        print("No")
    else:
        print("Yes")

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    if (a * b * 1) % 2 == 1:
        print("Yes")
    elif (a * b * 2) % 2 == 1:
        print("Yes")
    elif (a * b * 3) % 2 == 1:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    if (a*b)%2 == 0:
        print('No')
    else:
        print('Yes')

=======
Suggestion 4

def main():
    a, b = map(int, input().split())
    if (a * b * 3) % 2 == 1:
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    a,b = map(int, input().split())
    if a*b%2 == 0:
        print('No')
    else:
        print('Yes')

=======
Suggestion 6

def solve():
    a,b = map(int, input().split())
    if a*b % 2 == 1:
        print('Yes')
    else:
        print('No')
solve()
