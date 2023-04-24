Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    A, B = map(int, input().split())
    if A + B < 10 ** 19:
        print("Easy")
    else:
        print("Hard")

=======
Suggestion 2

def main():
    A, B = map(int, input().split())
    if A + B >= 10 ** 18:
        print("Hard")
    else:
        print("Easy")

=======
Suggestion 3

def main():
    A,B = map(int,input().split())
    if A+B >= 10:
        print("Hard")
    else:
        print("Easy")

=======
Suggestion 4

def main():
    a,b = map(int,input().split())
    if a+b >= 10:
        print("Hard")
    else:
        print("Easy")

=======
Suggestion 5

def main():
    a, b = map(int, input().split())
    if a+b > 10**18:
        print('Hard')
    else:
        print('Easy')

=======
Suggestion 6

def main():
    a, b = map(int, input().split())
    if (a + b) // 10 == 0:
        print("Easy")
    else:
        print("Hard")

=======
Suggestion 7

def main():
    a,b = map(int,input().split())
    if a+b >= 10**18:
        print("Hard")
    else:
        print("Easy")

=======
Suggestion 8

def main():
    a,b = map(int,input().split())
    if a+b < 10**(len(str(a))):
        print("Easy")
    else:
        print("Hard")

=======
Suggestion 9

def main():
    A,B = map(int,input().split())
    if A+B <= 9999999999:
        print("Easy")
    else:
        print("Hard")

=======
Suggestion 10

def main():
    import sys
    input = sys.stdin.readline
    A,B = map(int,input().split())
    print('Hard' if len(str(A+B))>len(str(A)) else 'Easy')
