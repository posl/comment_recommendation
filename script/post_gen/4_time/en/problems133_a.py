Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, a, b = map(int, input().split())
    print(min(n*a, b))

=======
Suggestion 2

def main():
    N, A, B = map(int, input().split())
    print(min(A * N, B))

=======
Suggestion 3

def solve():
    n, a, b = map(int, input().split())
    if n*a < b:
        print(n*a)
    else:
        print(b)

=======
Suggestion 4

def main():
    input_line = input()
    input_list = input_line.split()
    n, a, b = int(input_list[0]), int(input_list[1]), int(input_list[2])
    print(min(n * a, b))

=======
Suggestion 5

def main():
    a,b,c = map(int,input().split())
    print(min(a*b,c))
