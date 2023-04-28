Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    if l[-1] < sum(l[:-1]):
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    if l[-1] < sum(l[:-1]):
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    N = int(input())
    L = sorted(list(map(int, input().split())))
    if L[-1] < sum(L[:-1]):
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    print('Yes' if l[-1] < sum(l[:-1]) else 'No')

=======
Suggestion 5

def main():
    n = int(input())
    l = [int(x) for x in input().split()]
    l.sort()
    print("Yes" if l[-1] < sum(l[:-1]) else "No")

=======
Suggestion 6

def main():
    N = int(input())
    L = list(map(int,input().split()))

    maxL = max(L)
    sumL = sum(L)-maxL

    if maxL < sumL:
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def is_polygon_possible(n, l):
    l.sort()
    if l[-1] < sum(l[:-1]):
        return 'Yes'
    return 'No'
