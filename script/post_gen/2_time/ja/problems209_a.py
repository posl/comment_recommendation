Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a,b = map(int,input().split())
    if a > b:
        print(0)
    else:
        print(b-a+1)

=======
Suggestion 2

def main():
    a,b = map(int, input().split())
    if a <= b:
        print(b - a + 1)
    else:
        print(0)

=======
Suggestion 3

def main():
    A, B = map(int, input().split())
    print(B - A + 1 if A <= B else 0)

=======
Suggestion 4

def main():
    A,B = map(int,input().split())
    if A>B:
        print(0)
    else:
        print(B-A+1)

=======
Suggestion 5

def main():
    A, B = map(int, input().split())
    print(B-A+1 if B-A+1 > 0 else 0)

=======
Suggestion 6

def main():
    a, b = map(int, input().split())
    print(b - a + 1 if b > a else 0)

main()

=======
Suggestion 7

def main():
    A,B = map(int, input().split())
    if A > B:
        print(0)
    elif A <= B:
        print(B-A+1)

=======
Suggestion 8

def main():
    a,b = map(int, input().split())
    print(b-a+1 if b>=a else 0)

=======
Suggestion 9

def count_integers(a,b):
    count=0
    for i in range(a,b+1):
        count+=1
    return count
