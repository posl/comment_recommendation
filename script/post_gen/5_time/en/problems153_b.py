Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    H, N = map(int, input().split())
    A = list(map(int, input().split()))
    if H <= sum(A):
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    H, N = map(int, input().split())
    A = list(map(int, input().split()))
    if H <= sum(A):
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    h, n = map(int, input().split())
    a = list(map(int, input().split()))
    if h <= sum(a):
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    h, n = map(int, input().split())
    a = list(map(int, input().split()))
    if h <= sum(a):
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def solve():
    h, n = map(int, input().split())
    a = list(map(int, input().split()))
    print('Yes' if sum(a) >= h else 'No')

=======
Suggestion 6

def solve(H, N, A):
    if sum(A) >= H:
        return "Yes"
    else:
        return "No"
