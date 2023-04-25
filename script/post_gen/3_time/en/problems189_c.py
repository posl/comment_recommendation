Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for l in range(N):
        x = A[l]
        for r in range(l, N):
            x = min(x, A[r])
            ans = max(ans, x * (r - l + 1))
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        x = A[i]
        for j in range(i, N):
            x = min(x, A[j])
            ans = max(ans, x * (j - i + 1))
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for x in range(1, 100001):
        l = 0
        r = 0
        for i in range(N):
            while r < N and A[r] >= x:
                r += 1
            ans = max(ans, x * (r - l))
            if A[i] >= x:
                l += 1
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for x in range(1, 10**5+1):
        l = 0
        r = 0
        while r < N:
            while r < N and A[r] >= x:
                r += 1
            ans = max(ans, (r-l)*x)
            while r < N and A[r] < x:
                r += 1
            l = r
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for x in range(1, 10 ** 5 + 1):
        l = 0
        r = 0
        while l < N:
            while r < N and A[r] >= x:
                r += 1
            ans = max(ans, (r - l) * x)
            while l < N and A[l] < x:
                l += 1
            l += 1
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int,input().split()))
    ans = 0
    for x in range(1,10**5+1):
        tmp = 0
        for a in A:
            if a >= x:
                tmp += x
            else:
                ans = max(ans,tmp)
                tmp = 0
        ans = max(ans,tmp)
    print(ans)

=======
Suggestion 7

def main():
    # Read input
    N = int(input())
    A = list(map(int, input().split()))
    
    # Initialize variables
    ans = 0
    
    # Solve
    for i in range(N):
        x = A[i]
        for j in range(i, N):
            x = min(x, A[j])
            ans = max(ans, x * (j - i + 1))
    
    # Output
    print(ans)
