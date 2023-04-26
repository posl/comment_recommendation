Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if A[0] != 0:
        print(0)
    else:
        for i in range(N-1):
            if A[i+1] - A[i] > 1:
                print(A[i] + 1)
                exit()
        print(A[-1] + 1)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if A[0] != 0:
        print(0)
        return
    for i in range(N-1):
        if A[i+1] - A[i] > 1:
            print(A[i]+1)
            return
    print(A[-1]+1)
    return

main()

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    for i in range(0, 2001):
        if i not in A:
            print(i)
            break

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int,input().split()))
    a = list(set(a))
    a.sort()
    if a[0] != 0:
        print(0)
    else:
        for i in range(len(a)-1):
            if a[i+1] - a[i] != 1:
                print(a[i]+1)
                break
        else:
            print(a[-1]+1)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(2001):
        if i not in A:
            print(i)
            break

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a[0] != 0:
        print(0)
    else:
        for i in range(1,n):
            if a[i] - a[i-1] >= 2:
                print(a[i-1]+1)
                break
            elif i == n-1:
                print(a[n-1]+1)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int,input().split()))
    B = set(A)
    for i in range(N+1):
        if i not in B:
            print(i)
            break

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int,input().split()))
    #print(N)
    #print(A)
    A.sort()
    #print(A)
    if A[0] != 0:
        print(0)
        return
    for i in range(1,N):
        if A[i] - A[i-1] > 1:
            print(A[i-1]+1)
            return
    print(A[N-1]+1)

main()

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int,input().split()))
    A = sorted(A)
    A.append(2001)
    for i in range(2001):
        if A[i] != i:
            print(i)
            break

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(min(set(range(2001)) - set(A)))
