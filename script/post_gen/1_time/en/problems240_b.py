Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(len(set(a)))

=======
Suggestion 2

def main():
    N = int(input())
    a = list(map(int, input().split()))
    print(len(set(a)))

=======
Suggestion 3

def main():
    # input
    N = int(input())
    a = list(map(int, input().split()))

    # compute
    a_set = set(a)

    # output
    print(len(a_set))

=======
Suggestion 4

def main():
    n = int(input())
    a = input().split()
    a = [int(x) for x in a]
    a = set(a)
    print(len(a))
