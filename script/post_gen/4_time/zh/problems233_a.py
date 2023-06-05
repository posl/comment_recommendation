Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve():
    x, y = [int(i) for i in input().split()]
    print((y - x) // 10)

=======
Suggestion 2

def main():
    x,y = map(int,input().split())
    if x >= y:
        print(0)
    else:
        print((y-x)//10)

main()

=======
Suggestion 3

def main():
    x, y = map(int, input().split())
    if x >= y:
        print(0)
    else:
        print((y - x) // 10)

=======
Suggestion 4

def main():
    pass

=======
Suggestion 5

def main():
    x, y = map(int, input().split())
    n = 0
    while x * n < y:
        n += 1
    print(n * x - y)
    return

=======
Suggestion 6

def get_input():
    input_line = input()
    input_line = input_line.split()
    input_line = [int(x) for x in input_line]
    return input_line

=======
Suggestion 7

def solution():
    x,y = list(map(int,input().split()))
    print((y-x)//10)

=======
Suggestion 8

def solve():
    x, y = map(int, input().split())
    print(0 if x >= y else (y - x) // 10)
