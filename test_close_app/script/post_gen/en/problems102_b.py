Synthesizing 10/10 solutions (Duplicates hidden)

=======

def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(max(A) - min(A))

=======

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    print(A[-1] - A[0])

=======

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    maxA = max(A)
    minA = min(A)
    print(maxA - minA)

=======

def main():
    N = int(input())
    A = list(map(int,input().split()))
    max_diff = 0
    for i in range(N):
        for j in range(i+1,N):
            max_diff = max(max_diff,abs(A[i]-A[j]))
    print(max_diff)

=======

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    A.sort()
    print(A[-1] - A[0])

=======

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            ans = max(ans,abs(A[i]-A[j]))
    
    print(ans)
