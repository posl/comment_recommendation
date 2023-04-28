Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    # input
    a, b = map(int, input().split())

    # compute

    # output
    print(int((b-a)*(b-a+1)/2-b))

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    print((b-a)*(b-a+1)//2-b)

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    print(int((b-a)*(b-a+1)/2-b))

=======
Suggestion 4

def problems099_b():
    a, b = map(int, input().split())
    total = 0
    for i in range(1, b - a):
        total += i
    print(total - a)

=======
Suggestion 5

def main():
    a = int(input())
    b = int(input())
    print((b-a)*(b-a+1)//2 - b)

=======
Suggestion 6

def solve():
    a, b = map(int, input().split())
    print(b-a-1)

=======
Suggestion 7

def main():
    a,b = map(int,input().split())
    print(b-a-1)

=======
Suggestion 8

def snow_cover(a,b):
    return (b-a)*(b-a+1)//2 - b
