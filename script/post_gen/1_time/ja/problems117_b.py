Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort(reverse=True)
    if L[0] < sum(L[1:]):
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    N = int(input())
    L = list(map(int, input().split()))

    L.sort(reverse=True)
    if L[0] < sum(L[1:]):
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    if l[-1] < sum(l[:-1]):
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    n = int(input())
    l = list(map(int,input().split()))
    max_l = max(l)
    l.remove(max_l)
    if sum(l) > max_l:
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def readinput():
    n = int(input())
    l = list(map(int,input().split()))
    return n,l
