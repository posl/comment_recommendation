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
    l.sort(reverse=True)
    if l[0] < sum(l[1:]):
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    if L[-1] < sum(L[:-1]):
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def can_draw_polygon(sides):
    sides.sort()
    longest_side = sides.pop()
    if longest_side < sum(sides):
        return "Yes"
    else:
        return "No"

=======
Suggestion 6

def get_input():
    n = int(input())
    l = list(map(int, input().split()))
    return n, l
