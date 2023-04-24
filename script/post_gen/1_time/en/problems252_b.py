Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    for i in range(N):
        if A[i] == max(A) and i+1 not in B:
            print("Yes")
            return
    print("No")

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    for i in range(N):
        if A[i] == max(A) and i+1 not in B:
            print("Yes")
            exit()
    print("No")

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    for i in range(K):
        if A[B[i]-1] == max(A):
            print('Yes')
            return
    print('No')

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if max(A) in [A[i] for i in B]:
        print("Yes")
    else:
        print("No")
    return 0

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    for i in range(K):
        if A[B[i] - 1] == max(A):
            print("Yes")
            return
    print("No")

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort(reverse=True)
    B.sort()
    for i in range(K):
        if A[i] <= A[B[i]-1]:
            print("No")
            return
    print("Yes")

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort(reverse=True)
    B.sort()
    for i in range(K):
        if A[i] == B[i]:
            print("No")
            return
    print("Yes")

main()

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort(reverse=True)
    B.sort()
    i = 0
    for b in B:
        if A[i] > A[b-1]:
            print("Yes")
            return
        i += 1
    print("No")

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort(reverse=True)
    B.sort()
    
    for i in range(K):
        if A[i] == B[i]:
            print('Yes')
            return
    print('No')

=======
Suggestion 10

def main():
    #input
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    #compute
    for i in range(N-K):
        A.remove(max(A))
    for i in range(K):
        B[i] = A[B[i]-1]
    if max(B) == max(A):
        print("Yes")
    else:
        print("No")
    #output
