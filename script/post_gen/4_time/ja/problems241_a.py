Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a = list(map(int, input().split()))
    k = 0
    for i in range(3):
        k = a[k]
    print(k)

=======
Suggestion 2

def main():
    a = list(map(int, input().split()))
    ans = 0
    for i in range(3):
        ans = a[ans]
    print(ans)

=======
Suggestion 3

def main():
    # input
    a = list(map(int, input().split()))

    # compute
    k = 0
    for i in range(3):
        k = a[k]

    # output
    print(k)

=======
Suggestion 4

def main():
    a = list(map(int, input().split()))
    k = 0
    for i in range(0, 3):
        k = a[k]
    print(k)

=======
Suggestion 5

def main():
    a = list(map(int, input().split()))
    print(a[a[a[0]]])

=======
Suggestion 6

def main():
    a = list(map(int,input().split()))
    print(a[a[a[a[0]]]])

=======
Suggestion 7

def get_input():
    return list(map(int, input().split()))
