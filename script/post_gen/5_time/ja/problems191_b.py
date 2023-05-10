Synthesizing 10/10 solutions

=======
Suggestion 1

def problem191_b():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    ans = []
    for a in A:
        if a != X:
            ans.append(a)

    print(*ans)

=======
Suggestion 2

def main():
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    ans = []
    for i in range(n):
        if a[i] == x:
            pass
        else:
            ans.append(a[i])
    print(*ans)

=======
Suggestion 3

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(n):
        if a[i] != x:
            print(a[i], end=' ')

=======
Suggestion 4

def removeElement(nums, val):
    i = 0
    while i < len(nums):
        if nums[i] == val:
            nums.pop(i)
            i -= 1
        i += 1
    return nums

=======
Suggestion 5

def main():
    N,X = map(int,input().split())
    A = list(map(int,input().split()))
    A = [i for i in A if i != X]
    print(*A)

main()

=======
Suggestion 6

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    ans = []
    for i in range(n):
        if a[i] != x:
            ans.append(a[i])

    for i in range(len(ans)):
        print(ans[i], end=" ")
    print()

=======
Suggestion 7

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    result = []
    for i in range(n):
        if a[i] != x:
            result.append(a[i])
    print(*result)

=======
Suggestion 8

def main():
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    for i in range(n):
        if a[i] != x:
            print(a[i],end=" ")

=======
Suggestion 9

def main():
    N,X = map(int,input().split())
    A = list(map(int,input().split()))
    for i in range(N):
        if A[i] != X:
            print(A[i],end=" ")

=======
Suggestion 10

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    ans = []
    for i in range(N):
        if A[i] != X:
            ans.append(A[i])
    print(*ans)
