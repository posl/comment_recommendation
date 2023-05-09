Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    if L[-1] < sum(L[:-1]):
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
    l = list(map(int, input().split()))
    l.sort()
    if l[n-1] < sum(l[:n-1]):
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    n = int(input())
    l = sorted(list(map(int, input().split())))
    if l[-1] < sum(l[:-1]):
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    n = int(input())
    l = [int(x) for x in input().split()]
    l.sort(reverse=True)
    if l[0] < sum(l[1:]):
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    print("Yes" if L[-1] < sum(L[:-1]) else "No")

=======
Suggestion 8

def main():
    n = int(input())
    L = list(map(int, input().split()))
    if max(L) < sum(L)-max(L):
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def check_polygon(n, l):
    l.sort()
    if l[-1] < sum(l[:-1]):
        return "Yes"
    else:
        return "No"
