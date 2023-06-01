Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x,y = map(int,input().split())
    if x > y :
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    x, y = map(int, input().split())
    if x > y:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    x, y = map(int, input().split())
    print("Yes" if x < y else "No")

=======
Suggestion 4

def main():
    #input
    x, y = input().split()
    x = int(x)
    y = int(y)
    #process
    if x < y:
        print("Yes")
    else:
        print("No")
    #output

=======
Suggestion 5

def main():
    x, y = map(int, input().split())
    if x < y:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    X, Y = map(int, input().split())
    if X < Y:
        X, Y = Y, X
    if X - Y < 3:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    x, y = map(int, input().split())

    if x < y:
        print("Yes")
    else:
        print("No")
