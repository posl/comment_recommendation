Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    if b - a == 1:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    if b - a == 1 or b - a == 2:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    if b - a == 1:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    a, b = map(int, input().split())
    if abs(a-b) == 1:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    a, b = map(int, input().split())
    if a in [1, 3, 5, 7, 8, 10]:
        if b in [4, 6, 9]:
            print("Yes")
        else:
            print("No")
    else:
        print("No")

=======
Suggestion 6

def main():
    a, b = map(int, input().split())
    if 1 <= a < b <= 10:
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def main():
    a, b = map(int, input().split())

    if a + 1 == b:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    a,b = map(int,input().split())
    if (a == 1 and b == 3) or (a == 1 and b == 4) or (a == 3 and b == 4) or (a == 2 and b == 3) or (a == 2 and b == 4) or (a == 2 and b == 5):
        print('Yes')
    else:
        print('No')

=======
Suggestion 9

def main():
    a, b = map(int, input().split())
    if (b-a) == 1 or (a+b)%2 == 0:
        print("Yes")
    else:
        print("No")
