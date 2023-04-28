Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    R, C = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(2)]
    print(A[R-1][C-1])

=======
Suggestion 2

def main():
    R, C = map(int, input().split())
    A = []
    for i in range(2):
        A.append(list(map(int, input().split())))
    print(A[R-1][C-1])

=======
Suggestion 3

def main():
    r, c = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(2)]
    print(a[r-1][c-1])

=======
Suggestion 4

def main():
    r, c = map(int, input().split())
    matrix = []
    for i in range(2):
        matrix.append(list(map(int, input().split())))
    print(matrix[r-1][c-1])

=======
Suggestion 5

def main():
    R,C = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(2)]
    print(A[R-1][C-1])

=======
Suggestion 6

def get_input():
    # Get the input
    input = ''
    try:
        while True:
            input += raw_input()
    except EOFError:
        pass

    # Convert the input to integers
    input = input.split()
    input = [int(i) for i in input]

    return input
