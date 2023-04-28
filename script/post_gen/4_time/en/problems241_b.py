Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if N < M:
        print('No')
    else:
        A.sort()
        B.sort()
        i = 0
        j = 0
        while i < N and j < M:
            if A[i] <= B[j]:
                i += 1
                j += 1
            else:
                i += 1
        if j == M:
            print('Yes')
        else:
            print('No')

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if m > n:
        print("No")
    else:
        a.sort()
        b.sort()
        for i in range(m):
            if a[i] < b[i]:
                print("No")
                exit()
        print("Yes")

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if N < M:
        print('No')
        exit()

    A.sort()
    B.sort()

    for i in range(M):
        if A[i] > B[i]:
            print('No')
            exit()

    print('Yes')

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if n < m:
        print("No")
        exit()

    a.sort()
    b.sort()

    for i in range(m):
        if a[i] > b[i]:
            print("No")
            exit()

    print("Yes")

=======
Suggestion 5

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    j = 0
    for i in range(N):
        while j < M and B[j] < A[i]:
            j += 1
        if j == M or B[j] != A[i]:
            print('No')
            return
        j += 1
    print('Yes')

solve()

=======
Suggestion 6

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if M > N:
        print("No")
        return
    A.sort()
    B.sort()
    for i in range(M):
        if A[-M+i] > B[-1-i]:
            print("No")
            return
    print("Yes")

solve()

=======
Suggestion 7

def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A.sort(reverse=True)
    B.sort(reverse=True)
    if N < M:
        print("No")
    else:
        for i in range(M):
            if A[i] < B[i]:
                print("No")
                break
        else:
            print("Yes")

=======
Suggestion 8

def main():
    #n, m = map(int, input().split())
    #a = list(map(int, input().split()))
    #b = list(map(int, input().split()))
    n, m = 1, 1
    a = [1000000000]
    b = [1]
    if m > n:
        print('No')
    else:
        if len(set(b)) != len(b):
            print('No')
        else:
            for i in range(m):
                if b[i] not in a:
                    print('No')
                    break
            else:
                print('Yes')
main()

=======
Suggestion 9

def solve(n, m, a, b):
    if m > n:
        return False
    if m == 1:
        if b[0] in a:
            return True
        else:
            return False
    else:
        for i in range(n):
            for j in range(m):
                if a[i] == b[j]:
                    return True
        return False

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
