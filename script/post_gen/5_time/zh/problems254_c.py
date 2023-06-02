Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, K)
    #print(A)
    for i in range(N-K):
        if A[i] > A[i+K]:
            print("Yes")
            return
    print("No")

=======
Suggestion 2

def is_sorted(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

=======
Suggestion 3

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(N-K):
        if A[i] > A[i+K]:
            print("Yes")
            return
    print("No")

=======
Suggestion 4

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    for i in range(n-k):
        if a[i] < a[i+k]:
            continue
        else:
            print("No")
            exit()
    print("Yes")

=======
Suggestion 5

def is_sorted(a):
    for i in range(1, len(a)):
        if a[i] < a[i-1]:
            return False
    return True

=======
Suggestion 6

def solve():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    if K == 1:
        for i in range(N-1):
            if a[i] > a[i+1]:
                print('No')
                return
        print('Yes')
        return
    for i in range(N-K):
        if a[i] > a[i+K]:
            print('No')
            return
    print('Yes')
    return

=======
Suggestion 7

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    if K == 1:
        if A == sorted(A):
            print('Yes')
        else:
            print('No')
        return
    if K == 2:
        if A == sorted(A):
            print('Yes')
        else:
            print('No')
        return
    if K > 2:
        if A == sorted(A):
            print('Yes')
        else:
            print('No')
        return


solve()

=======
Suggestion 8

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    for i in range(n-k):
        if a[i] > a[i+k]:
            print("Yes")
            exit()
    print("No")

=======
Suggestion 9

def solve(n, k, a):
    ans = "Yes"
    for i in range(n-k):
        if a[i] > a[i+k]:
            ans = "No"
    return ans

=======
Suggestion 10

def solve(n,k,a):
    if k==1:
        return "Yes"
    for i in range(0,k):
        if a[i]>a[i+k]:
            return "No"
    return "Yes"

n,k=map(int,input().split())
a=list(map(int,input().split()))
print(solve(n,k,a))
