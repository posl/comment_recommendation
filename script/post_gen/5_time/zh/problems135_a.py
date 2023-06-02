Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a,b=map(int,input().split())
    if (a+b)%2==0:
        print((a+b)//2)
    else:
        print("IMPOSSIBLE")

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    if (a + b) % 2 == 0:
        print(int((a + b) / 2))
    else:
        print("IMPOSSIBLE")

=======
Suggestion 3

def solve(a, b):
    if (a + b) % 2 == 0:
        return (a + b) // 2
    else:
        return "IMPOSSIBLE"

=======
Suggestion 4

def main():
    a, b = map(int, input().split())
    if a > b:
        print(a + (a - b) // 2)
    elif a < b:
        print(b - (b - a) // 2)
    else:
        print(a)

=======
Suggestion 5

def main():
    a,b = map(int,input().split())
    if (a+b)%2 == 0:
        print((a+b)//2)
    else:
        print('IMPOSSIBLE')

=======
Suggestion 6

def main():
    a,b = map(int,input().split())
    if (a+b)%2 == 0:
        print((a+b)//2)
    else:
        print("IMPOSIBLE")

=======
Suggestion 7

def main():
    a,b = map(int, input().split())
    if (a+b)%2 == 0:
        print(int((a+b)/2))
    else:
        print("IMPOSIBLE")
