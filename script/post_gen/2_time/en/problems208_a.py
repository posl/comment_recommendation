Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    A, B = map(int, input().split())
    if A * 6 < B:
        print("No")
    elif A > B:
        print("No")
    else:
        print("Yes")

main()

=======
Suggestion 2

def main():
    A, B = map(int, input().split())
    if A*1 <= B <= A*6:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    A, B = map(int, input().split())
    if 6*A < B:
        print("No")
    elif B < A:
        print("No")
    else:
        print("Yes")

=======
Suggestion 4

def main():
    A, B = map(int, input().split())
    if A * 6 < B:
        print("No")
    else:
        print("Yes")

=======
Suggestion 5

def main():
    A, B = map(int, input().split())
    if A >= 1 and A <= 100 and B >= 1 and B <= 1000:
        if A * 1 <= B <= A * 6:
            print("Yes")
        else:
            print("No")
    else:
        print("Input Error")

=======
Suggestion 6

def main():
    A, B = map(int, input().split())
    if A <= B <= A * 6:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    A, B = map(int, input().split())
    if B > A * 6:
        print("No")
    else:
        print("Yes")

=======
Suggestion 8

def main():
    a, b = map(int, input().split())
    print("Yes" if a * 6 >= b >= a else "No")

=======
Suggestion 9

def main():
    A, B = map(int, input().split())
    if A*6 < B or A > B:
        print("No")
    else:
        print("Yes")

main()

A, B = map(int, input().split())
print("YNeos"[A*6<B or A>B::2])

A, B = map(int, input().split())
print('YNeos'[A*6<B or A>B::2])

A, B = map(int, input().split())
print("YNeos"[A*6<B or A>B::2])

A, B = map(int, input().split())
print("YNeos"[A*6<B or A>B::2])

A, B = map(int, input().split())
print("YNeos"[A*6<B or A>B::2])

A, B = map(int, input().split())
print("YNeos"[A*6<B or A>B::2])

A, B = map(int, input().split())
print("YNeos"[A*6<B or A>B::2])

A, B = map(int, input().split())
print("YNeos"[A*6<B or A>B::2])

A, B = map(int, input().split())
print("YNeos"[A*6<B or A>B::2])

A, B = map(int, input().split())
print("YNeos"[A*6<B or A>B::2])

A, B = map(int, input().split())
print("YNeos"[A*6<B or A>B::2])

A, B = map(int, input().split())
print("YNeos"[A*6<B or A>B::2])

A, B = map(int, input().split())
print("YNeos"[A*6<B or A>B::2])

A, B = map(int, input().split())
print("YNeos"[A*6<B or A>B::2])

A, B = map(int, input().split())
print("YNeos"[A*6<B or A>B::2])

A, B = map(int, input().split())
print("YNeos"[A*6<B or A>B::2])

A, B = map(int, input().split())
print("YNeos"[A*6<B or A>B::2])

=======
Suggestion 10

def main():
    A,B = map(int,input().split())
    if B < A or B > 6*A:
        print("No")
    else:
        print("Yes")
