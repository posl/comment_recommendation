Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    for i in range(2001):
        if i not in A:
            print(i)
            break

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = set(A)
    for i in range(2001):
        if i not in A:
            print(i)
            break

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if A[0] != 0:
        print(0)
    else:
        for i in range(N-1):
            if A[i+1] - A[i] >= 2:
                print(A[i] + 1)
                break
        else:
            print(A[-1] + 1)

main()

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()
    if A[0] != 0:
        print(0)
    else:
        for i in range(1,N):
            if A[i] - A[i-1] > 1:
                print(A[i-1]+1)
                break
        else:
            print(A[-1]+1)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a[0] != 0:
        print(0)
    else:
        for i in range(n-1):
            if a[i+1] - a[i] > 1:
                print(a[i]+1)
                return
        print(a[-1]+1)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(N):
        if A[i] != i:
            print(i)
            return
    print(N)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(n):
        if a[i] != i:
            print(i)
            return
    print(n)

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = list(set(a))
    a.sort()
    for i in range(n+1):
        if i not in a:
            print(i)
            break

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a = list(set(a))
    for i in range(2001):
        if i not in a:
            print(i)
            break

=======
Suggestion 10

def main():
    #入力
    N = int(input())
    A = list(map(int,input().split()))
    #最小の非負整数を求める
    for i in range(2001):
        if not i in A:
            print(i)
            break
