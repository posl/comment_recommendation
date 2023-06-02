Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(n-1):
        if a[i] == a[i+1]:
            print("NO")
            return
    print("YES")
    return

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(n-1):
        if a[i] == a[i+1]:
            print('NO')
            return
    print('YES')

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    #print(a)
    #print(len(a))
    #print(len(set(a)))
    if len(a) == len(set(a)):
        print("YES")
    else:
        print("NO")

=======
Suggestion 4

def main():
    # N = int(input())
    # A = list(map(int, input().split()))
    N = 5
    A = [2, 6, 1, 4, 5]
    # N = 6
    # A = [4, 1, 3, 1, 6, 2]
    # N = 2
    # A = [10000000, 10000000]
    print('Yes' if len(set(A)) == N else 'No')

=======
Suggestion 5

def main():
    n = int(input())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(n-1):
        if A[i] == A[i+1]:
            print("NO")
            return
    print("YES")

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(n-1):
        if a[i] == a[i+1]:
            print("NO")
            exit()
    print("YES")

=======
Suggestion 7

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    for i in range(1, n):
        if a[i - 1] == a[i]:
            print("NO")
            break
    else:
        print("YES")

=======
Suggestion 8

def main():
    n=int(input())
    a=[int(i) for i in input().split()]
    if len(set(a))==n:
        print('Yes')
    else:
        print('No')
