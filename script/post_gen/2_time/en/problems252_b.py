Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if max(A) in [A[i] for i in B]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    N, K = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]

    A.sort()
    B.sort()

    for i in range(K):
        if A[-1] == B[i]:
            A.pop()
        else:
            break

    if len(A) > 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort(reverse=True)
    B.sort()
    i = 0
    for j in range(K):
        while A[i] == B[j]:
            i += 1
            j += 1
        if A[i] > B[j]:
            print('Yes')
            return
    print('No')

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    B = set(B)
    A.sort(reverse=True)
    for i in range(K):
        if A[i] in B:
            print("Yes")
            return
    print("No")

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    B = [b-1 for b in B]
    A.sort(reverse=True)
    for i in range(K):
        if A[i] in B:
            print("Yes")
            return
    print("No")

main()

=======
Suggestion 6

def main():
    # input
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # compute
    A.sort(reverse=True)
    for i in range(K):
        if A[i] in B:
            print('Yes')
            return
    print('No')

=======
Suggestion 7

def main():
    #input
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    #compute
    A.sort(reverse=True)
    B.sort()

    #output
    for i in range(K):
        if A[i] == A[i+1]:
            continue
        if i+1 == B[i]:
            print('Yes')
            return
    print('No')

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    B = set(B)
    
    for i in range(N):
        if (N - i) in B:
            continue
        else:
            print(A[N - i - 1])
            break

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # Sort A in descending order
    A.sort(reverse=True)

    # Check if the greatest tastiness food is disliked
    if B.count(A.index(B[0])+1) > 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 10

def main():
    N,K = map(int,input().split())
    A = map(int,input().split())
    B = map(int,input().split())
    A = list(A)
    B = list(B)
    A.sort(reverse=True)
    B.sort(reverse=True)
    i = 0
    for j in range(K):
        while i<N:
            if A[i] == A[i+1]:
                i += 1
            else:
                if A[i] == A[i+1] and B[j] == i+1:
                    print("Yes")
                    return
                elif A[i] != A[i+1] and B[j] == i+1:
                    print("Yes")
                    return
                else:
                    i += 1
    print("No")
