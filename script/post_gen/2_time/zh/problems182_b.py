Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a,b = map(int, input().split())

    if a >= b:
        print(2*a+100-b)
    else:
        print(2*a+100)

=======
Suggestion 2

def main():
    a,b=map(int,input().split())
    if b<=2*a+100:
        print(2*a+100-b)
    else:
        print(0)

=======
Suggestion 3

def main():
    A,B = map(int,input().split())
    print(2*A+100-B)

=======
Suggestion 4

def main():
    a, b = map(int, input().split())
    print(2 * a + 100 - b)

=======
Suggestion 5

def main():
    # Read from stdin
    a, b = map(int, input().split())
    print(2*a+100-b)

=======
Suggestion 6

def main():
    a,b = map(int, input().split())
    if b > 2*a+100:
        print(0)
    else:
        print(2*a+100-b)

=======
Suggestion 7

def problem182_a(a,b):
    print(2*a+100-b)

=======
Suggestion 8

def main():
    a,b=map(int,input().split())
    print(2*a+100-b)

main()
