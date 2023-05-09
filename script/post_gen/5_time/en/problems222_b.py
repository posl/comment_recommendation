Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, p = map(int, input().split())
    a = list(map(int, input().split()))
    count = 0
    for i in range(n):
        if a[i] < p:
            count += 1
    print(count)

=======
Suggestion 2

def main():
    n, p = map(int, input().split())
    a = list(map(int, input().split()))
    print(len([x for x in a if x < p]))

=======
Suggestion 3

def main():
    n, p = map(int, input().split())
    a = list(map(int, input().split()))
    print(len([i for i in a if i < p]))

=======
Suggestion 4

def main():
    N, P = map(int, input().split())
    a = list(map(int, input().split()))
    print(len([x for x in a if x < P]))

=======
Suggestion 5

def main():
    # input
    n, p = map(int, input().split())
    a = list(map(int, input().split()))

    # process
    cnt = 0
    for i in range(n):
        if a[i] < p:
            cnt += 1

    # output
    print(cnt)

=======
Suggestion 6

def get_input():
    N, P = map(int, input().split())
    A = list(map(int, input().split()))
    return N, P, A
