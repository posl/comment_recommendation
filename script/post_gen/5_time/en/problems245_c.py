Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    diff = 0
    for i in range(N):
        diff += abs(A[i] - B[i])
    if diff > K:
        print("No")
    else:
        if (diff - K) % 2 == 0:
            print("Yes")
        else:
            print("No")

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    diff = 0
    for i in range(n):
        diff += abs(a[i]-b[i])
    if k >= diff and (k-diff)%2 == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    diff = 0
    for i in range(N):
        diff += abs(A[i] - B[i])
    
    if diff > K:
        print("No")
    elif (diff - K) % 2 == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    B.sort()

    for i in range(N):
        if abs(A[i] - B[i]) > K:
            print("No")
            exit()

    print("Yes")

main()

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    min_A = min(A)
    max_A = max(A)
    min_B = min(B)
    max_B = max(B)

    if (min_A > max_B) or (min_B > max_A):
        print('No')
        exit()

    if K == 0:
        print('Yes')
        exit()

    for i in range(N):
        if abs(A[i] - B[i]) > K:
            print('No')
            exit()

    print('Yes')

=======
Suggestion 6

def main():
    N,K=map(int,input().split())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    A.sort()
    B.sort()
    for i in range(N):
        if abs(A[i]-B[i])>K:
            print("No")
            exit()
    print("Yes")

=======
Suggestion 7

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    for i in range(N):
        if abs(A[i]-B[i])>K:
            return "No"
    return "Yes"
print(solve())

=======
Suggestion 8

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    min_a = min(A)
    max_a = max(A)
    min_b = min(B)
    max_b = max(B)

    if abs(max_a - min_b) <= K:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    N, K = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    for i in range(N):
        if abs(A[i]-B[i]) > K:
            print("No")
            return
    print("Yes")

=======
Suggestion 10

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    if k == 0:
        print('Yes')
    else:
        for i in range(n):
            if abs(a[i]-b[i]) > k:
                print('No')
                break
        else:
            print('Yes')
