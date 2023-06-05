Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def carry(a, b):
    if a == 0 and b == 0:
        return 0
    elif a % 10 + b % 10 >= 10:
        return 1 + carry(a // 10, b // 10)
    else:
        return carry(a // 10, b // 10)

a, b = map(int, input().split())

=======
Suggestion 2

def main():
    A,B = map(int,input().split())
    if A + B >= 10**10:
        print("Hard")
    else:
        print("Easy")

=======
Suggestion 3

def main():
    a,b = map(int, input().split())
    if a+b < 10:
        print('Easy')
    else:
        print('Hard')

=======
Suggestion 4

def main():
    a, b = map(int, input().split())
    if a + b >= 10**10:
        print("Hard")
    else:
        print("Easy")

=======
Suggestion 5

def main():
    a,b = map(int,input().split())
    if a+b < 10:
        print("Easy")
    else:
        print("Hard")

=======
Suggestion 6

def main():
    a,b = map(int,input().split())
    if a+b >= 10:
        print("Hard")
    else:
        print("Easy")

=======
Suggestion 7

def main():
    A,B = map(int,input().split())
    if A+B >= 10**9:
        print("Hard")
    else:
        print("Easy")
