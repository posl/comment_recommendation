Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    S = sum(A)
    for i in range(M):
        if A[i] < S / (4 * M):
            print("否")
            return
    print("是")

=======
Suggestion 2

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    sum = 0
    for i in range(m):
        sum += a[i]
    for i in range(m,n):
        if a[i] < sum/(4*m):
            print("否")
            return
    print("是")
    return

=======
Suggestion 3

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    total = sum(a)
    a.sort(reverse=True)
    if a[m-1]*4*m >= total:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    total = sum(A)
    if total / (4 * m) <= A[m-1]:
        print("是")
    else:
        print("否")

=======
Suggestion 5

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    total = sum(a)
    a.sort(reverse=True)
    if a[m-1] >= total/(4*m):
        print("是")
    else:
        print("否")

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    total = sum(a)
    if a[m-1] >= total/(4*m):
        print("是")
    else:
        print("否")

=======
Suggestion 7

def main():
	n,m = map(int,input().split())
	A = list(map(int,input().split()))
	A.sort(reverse=True)
	total = sum(A)
	if A[m-1] >= total/(4*m):
		print("是")
	else:
		print("否")

=======
Suggestion 8

def printYesOrNo():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    total = sum(a)
    a.sort(reverse=True)
    if a[m-1] >= total/(4*m):
        print("是")
    else:
        print("否")

printYesOrNo()

=======
Suggestion 9

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    total = sum(a)
    threshold = total / (4 * m)
    if a[m - 1] >= threshold:
        print("是")
    else:
        print("否")

=======
Suggestion 10

def main():
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    total_vote = sum(A)
    if A[m-1] >= total_vote/(4*m):
        print("Yes")
    else:
        print("No")
