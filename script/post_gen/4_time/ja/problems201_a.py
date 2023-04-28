Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a = list(map(int, input().split()))
    a.sort()
    if a[2] - a[1] == a[1] - a[0]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    a = list(map(int, input().split()))
    a.sort()
    if a[2] - a[1] == a[1] - a[0]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    A = sorted(list(map(int, input().split())))
    if A[2] - A[1] == A[1] - A[0]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    a = input().split()
    a.sort()
    if int(a[1]) - int(a[0]) == int(a[2]) - int(a[1]):
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    A = list(map(int, input().split()))
    A.sort()
    print("Yes" if A[1] - A[0] == A[2] - A[1] else "No")

=======
Suggestion 6

def main():
    # 整数の入力
    a1, a2, a3 = map(int, input().split())
    if a3 - a2 == a2 - a1:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    # a,b,c = map(int, input().split())
    a,b,c = map(int, input().split())
    if a-b == b-c or b-a == c-b or c-b == b-a or b-c == a-b:
        print('Yes')
    else:
        print('No')
