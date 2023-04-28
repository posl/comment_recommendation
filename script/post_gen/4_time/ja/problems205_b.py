Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if A == list(range(1, N+1)):
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a == list(range(1,n+1)):
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    if a == list(range(1,n+1)):
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(N):
        if A[i] != i+1:
            print('No')
            return
    print('Yes')
    return

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))

    if len(set(a)) == n:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    for i in range(n):
        if a[i] != i + 1:
            print("No")
            exit()
    print("Yes")

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))

    A.sort()

    for i in range(1, N + 1):
        if i != A[i - 1]:
            print('No')
            return

    print('Yes')
    return

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()
    ans = "Yes"
    for i in range(1,N+1):
        if A[i-1] != i:
            ans = "No"
    print(ans)

=======
Suggestion 9

def main():
    # input
    N = int(input())
    A = list(map(int, input().split()))

    # compute
    A.sort()
    for i in range(N):
        if A[i] != i+1:
            print("No")
            exit()

    # output
    print("Yes")
