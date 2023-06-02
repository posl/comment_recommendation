Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(1, n+1):
        if a[i-1] != i:
            print("No")
            return
    print("Yes")
main()

=======
Suggestion 2

def main():
    n = int(input())
    arr = input().split()
    arr = [int(x) for x in arr]
    arr.sort()
    for i in range(n):
        if arr[i] != i+1:
            print("No")
            return
    print("Yes")

=======
Suggestion 3

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    for i in range(n):
        if a[i] != i+1:
            print('No')
            break
    else:
        print('Yes')

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    if a == list(range(1,n+1)):
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    for i in range(n):
        if i + 1 != a[i]:
            print("No")
            exit()
    print("Yes")

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if A == list(range(1, N+1)):
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a == list(range(1, n+1)):
        print('Yes')
    else:
        print('No')

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(n):
        if a[i] != i + 1:
            print("No")
            exit()
    print("Yes")
