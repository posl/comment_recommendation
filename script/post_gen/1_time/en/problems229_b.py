Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    A, B = map(int, input().split())
    if A + B >= 10:
        print('Hard')
    else:
        print('Easy')

=======
Suggestion 2

def main():
    A, B = map(int, input().split())
    if A + B < 10:
        print("Easy")
    else:
        print("Hard")

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    if a + b >= 10:
        print("Hard")
    else:
        print("Easy")

=======
Suggestion 4

def main():
    A,B = map(int, input().split())
    if len(str(A+B)) == len(str(A)) or len(str(A+B)) == len(str(B)):
        print("Easy")
    else:
        print("Hard")

=======
Suggestion 5

def main():
    A, B = map(int, input().split())
    if len(str(A + B)) == len(str(A)) == len(str(B)):
        print('Easy')
    else:
        print('Hard')

=======
Suggestion 6

def main():
    A, B = map(int, input().split())
    if A + B < 10**18:
        print("Easy")
    else:
        print("Hard")

=======
Suggestion 7

def main():
    A, B = input().split()
    A = int(A)
    B = int(B)
    C = A + B
    if len(str(C)) == len(str(A)) and len(str(C)) == len(str(B)):
        print('Easy')
    else:
        print('Hard')

=======
Suggestion 8

def main():
    A,B = map(int,input().split())
    if A+B > 999999999:
        print("Hard")
    else:
        print("Easy")

main()

=======
Suggestion 9

def main():
    A, B = map(int, input().split())
    print('Easy' if (A+B) < 10 else 'Hard')

=======
Suggestion 10

def solve(A, B):
    if A + B < 10:
        return "Easy"
    else:
        return "Hard"
