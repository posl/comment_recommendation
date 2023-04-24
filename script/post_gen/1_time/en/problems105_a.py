Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    if n % k == 0:
        print(0)
    else:
        print(1)

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    print(0 if n % k == 0 else 1)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    if N%K == 0:
        print(0)
    else:
        print(1)

=======
Suggestion 4

def problems105_a():
    N, K = map(int, input().split())
    if N%K == 0:
        print(0)
    else:
        print(1)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    print(0 if N%K == 0 else 1)

=======
Suggestion 6

def main():
    # input
    N, K = map(int, input().split())

    # compute

    # output
    print(0 if N%K==0 else 1)

=======
Suggestion 7

def main():
    num_of_crackers, num_of_users = map(int, input().split())
    print(num_of_crackers % num_of_users)

=======
Suggestion 8

def get_input():
    input_line = input()
    input_line = input_line.split()
    return input_line
