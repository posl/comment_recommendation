Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B = map(int, input().split())
    if A + B >= 10**18:
        print("Hard")
    else:
        print("Easy")

=======
Suggestion 2

def main():
    A,B = map(int,input().split())
    if A+B < 10:
        print("Easy")
    else:
        print("Hard")

=======
Suggestion 3

def main():
    A,B = map(int,input().split())
    if A+B < 10:
        print('Easy')
    else:
        print('Hard')

=======
Suggestion 4

def main():
    A, B = map(int, input().split())
    if (A+B) >= 10:
        print("Hard")
    else:
        print("Easy")

=======
Suggestion 5

def main():
    a,b = map(int,input().split())
    if a+b >= 10**19:
        print("Hard")
    else:
        print("Easy")

=======
Suggestion 6

def main():
    a, b = map(int, input().split())
    print("Easy" if a + b < 10 ** 19 else "Hard")

=======
Suggestion 7

def main():
    a,b = map(int,input().split())
    if a+b < 10:
        print('Easy')
    else:
        print('Hard')
main()

=======
Suggestion 8

def main():
    A,B = map(int,input().split())
    print("Hard" if (A+B) >= 10**19 else "Easy")
