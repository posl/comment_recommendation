Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A_even = [a for a in A if a % 2 == 0]
    if len(A_even) == 0:
        print(-1)
    else:
        print(max(A_even))

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    if A[0] % 2 == 0:
        print(A[0] + A[1])
    else:
        print(-1)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = -1
    for i in range(N):
        if A[i] % 2 == 0:
            ans = max(ans, A[i])
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if A[-1] % 2 == 0:
        print(A[-1])
    else:
        for i in range(N-1):
            if A[i] % 2 == 0:
                print(A[i])
                break
        else:
            print(-1)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if A[-1] % 2 == 0:
        print(A[-1])
    elif A[-2] % 2 == 0:
        print(A[-2])
    else:
        print(-1)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()

    if A[-1] % 2 == 0:
        print(A[-1])
    elif A[-1] % 2 == 1:
        if A[-2] % 2 == 0:
            print(A[-2])
        else:
            print(-1)

main()

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    #print(N)
    #print(A)
    if A[0] % 2 == 0:
        print(A[0])
    else:
        for i in range(1, N):
            if A[i] % 2 == 0:
                print(A[i])
                break
        else:
            print(-1)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    #print(A)
    ans = -1
    for i in range(N-1):
        if A[i] % 2 == 0:
            ans = max(ans, A[i]+A[i])
    print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    # a.sort(reverse=True)
    ans = -1
    for i in range(n):
        for j in range(i+1,n):
            if (a[i]+a[j])%2 == 0:
                ans = max(ans,a[i]+a[j])
    print(ans)
