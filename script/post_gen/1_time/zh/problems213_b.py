Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    print(a[1])

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = sorted(a)
    print(a.index(b[1])+1)

=======
Suggestion 3

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    print(a[1])

solve()

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    min1 = min2 = 10**9
    for i in range(N):
        if A[i] < min1:
            min2 = min1
            min1 = A[i]
            min_index = i
        elif A[i] < min2:
            min2 = A[i]
    print(min_index + 1)

=======
Suggestion 5

def find_second_lowest_score(scores):
    scores = sorted(scores)
    second_lowest_score = scores[1]
    for i in range(2, len(scores)):
        if scores[i] > second_lowest_score:
            return scores[i]

=======
Suggestion 6

def get_second_min(list):
    if len(list) < 2:
        return None
    min = list[0]
    second_min = None
    for i in range(1, len(list)):
        if list[i] < min:
            second_min = min
            min = list[i]
        elif list[i] != min and (second_min == None or list[i] < second_min):
            second_min = list[i]
    return second_min

=======
Suggestion 7

def main():
    n = int(input())
    scores = list(map(int, input().split()))
    scores.sort()
    print(scores[1])

=======
Suggestion 8

def solve(n, a):
    min1 = a[0]
    min2 = a[1]
    if min1 > min2:
        min1, min2 = min2, min1
    for i in range(2,n):
        if a[i] < min1:
            min2 = min1
            min1 = a[i]
        elif a[i] < min2:
            min2 = a[i]
    for i in range(n):
        if a[i] == min2:
            return i + 1
