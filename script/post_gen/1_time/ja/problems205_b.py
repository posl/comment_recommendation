Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if A == list(range(1, N+1)):
        print("Yes")
    else:
        print("No")

main()

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = sorted(A)
    if A == B:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(range(1, N+1))
    if A == B:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(N):
        if A[i] != i+1:
            print("No")
            return
    print("Yes")
    return

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    if A == sorted(A):
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a == [i for i in range(1, n+1)]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    B = [i for i in range(1, N+1)]
    if A == B:
        print('Yes')
    else:
        print('No')

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a == [i for i in range(1, n+1)]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))

    A.sort()
    B = list(range(1, N+1))

    if A == B:
        print("Yes")
    else:
        print("No")

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)

    A.sort()
    #print(A)

    for i in range(N):
        if A[i] != i+1:
            print("No")
            break
    else:
        print("Yes")
