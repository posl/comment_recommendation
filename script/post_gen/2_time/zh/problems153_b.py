Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def main():
    H,N = map(int,input().split())
    A = list(map(int,input().split()))
    if H > sum(A):
        print("No")
    else:
        print("Yes")

=======
Suggestion 3

def main():
    H, N = map(int, input().split())
    A = list(map(int, input().split()))
    if H <= sum(A):
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def judge(h,n,a):
    if h<=0:
        return True
    if n==0:
        return False
    if judge(h-a[0],n-1,a[1:]):
        return True
    if judge(h,n-1,a[1:]):
        return True
    return False

=======
Suggestion 5

def judge(H, N, A):
    #print(H, N, A)
    if H == 0:
        return True
    if H < 0:
        return False
    if N == 0:
        return False
    if judge(H-A[0], N-1, A[1:]) or judge(H, N-1, A[1:]):
        return True
    else:
        return False

=======
Suggestion 6

def main():
    h,n = map(int,input().split())
    a = list(map(int,input().split()))
    if h <= sum(a):
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    H, N = map(int, input().split())
    A = list(map(int, input().split()))
    if H <= sum(A):
        print('Yes')
    else:
        print('No')

=======
Suggestion 8

def main():
    H, N = map(int, input().split())
    A = list(map(int, input().split()))
    if sum(A) >= H:
        print("Yes")
    else:
        print("No")
