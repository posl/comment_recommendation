Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort()
    if n < m:
        print("No")
        return
    for i in range(m):
        if a[i] >= b[i]:
            print("No")
            return
    print("Yes")

=======
Suggestion 2

def solve():
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    a.sort()
    b.sort()
    if a[-1]>b[-1]:
        print("No")
        return
    i=0
    for j in range(m):
        if a[i]==b[j]:
            i+=1
            if i==n:
                print("Yes")
                return
    print("No")
solve()

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    B.sort()

    if M > N:
        print('No')
        return

    for i in range(M):
        if B[i] < A[i]:
            print('No')
            return

    print('Yes')

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # a.sort()
    # b.sort()
    # a.reverse()
    # b.reverse()
    # if b[0] > a[0]:
    #     print('No')
    # else:
    #     print('Yes')

    a.sort()
    b.sort()
    a.reverse()
    b.reverse()
    for i in range(n):
        if a[i] < b[i]:
            print('No')
            return
    print('Yes')
    return

=======
Suggestion 5

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    a.sort()
    b.sort()

    if n < m:
        print('No')
        exit()

    for i in range(m):
        if a[i] >= b[i]:
            print('No')
            exit()

    print('Yes')

=======
Suggestion 6

def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort()

    if n < m:
        print("No")
        return

    for i in range(m):
        if a[i] > b[i]:
            print("No")
            return
    print("Yes")

=======
Suggestion 7

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort()
    b.sort()
    if a[-1] > b[-1]:
        print("No")
    else:
        print("Yes")
main()

=======
Suggestion 8

def main():
    n,m = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    #print(A)
    #print(B)
    if n < m:
        print('No')
    else:
        A.sort(reverse=True)
        B.sort(reverse=True)
        #print(A)
        #print(B)
        for i in range(m):
            if A[i] < B[i]:
                print('No')
                break
        else:
            print('Yes')

=======
Suggestion 9

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort()
    b.sort()
    if n < m:
        print("No")
    else:
        for i in range(m):
            if a[i] < b[i]:
                print("No")
                return
        print("Yes")

=======
Suggestion 10

def solve():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort(reverse=True)
    b.sort(reverse=True)
    if n < m:
        print("No")
        return
    i = 0
    for j in range(m):
        while i < n:
            if b[j] <= a[i]:
                i += 1
                break
            else:
                i += 1
        if i == n:
            print("No")
            return
    print("Yes")
solve()
