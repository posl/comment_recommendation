Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        A_i, B_i = map(int, input().split())
        A.append(A_i)
        B.append(B_i)
    A_min = min(A)
    B_min = min(B)
    if A.index(A_min) == B.index(B_min):
        A.pop(A.index(A_min))
        B.pop(B.index(B_min))
        A_min = min(A)
        B_min = min(B)
        print(min(A_min+B_min, max(A_min

=======
Suggestion 2

def main():
    N = int(input())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    
    min_time = 10**5 * 2 + 1
    
    for i in range(N):
        for j in range(N):
            if i == j:
                time = A[i] + B[j]
            else:
                time = max(A[i], B[j])
            if min_time > time:
                min_time = time
    
    print(min_time)

=======
Suggestion 3

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A.sort()
    B.sort()
    if N % 2 == 0:
        print((B[N//2] - B[N//2 - 1]) + (A[N//2] - A[N//2 - 1]))
    else:
        print(B[N//2] - A[N//2] + 1)

=======
Suggestion 4

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A.sort()
    B.sort()
    if N % 2 == 1:
        print(B[N // 2] - A[N // 2] + 1)
    else:
        print(min(B[N // 2] - A[N // 2], B[N // 2 - 1] - A[N // 2 - 1]) + 1)

=======
Suggestion 5

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    min_time = 10**9
    for i in range(N):
        for j in range(N):
            if i == j:
                time = A[i] + B[j]
            else:
                time = max(A[i], B[j])
            if time < min_time:
                min_time = time
    print(min_time)

=======
Suggestion 6

def main():
    N = int(input())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    ans = float('inf')
    for i in range(N):
        for j in range(N):
            ans = min(ans, max(A[i], B[j]) if i != j else A[i] + B[j])
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    min_time = 10**10
    for i in range(N):
        for j in range(N):
            if i == j:
                min_time = min(min_time, A[i] + B[j])
            else:
                min_time = min(min_time, max(A[i], B[j]))
    print(min_time)

=======
Suggestion 8

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    #print(A)
    #print(B)
    A.sort()
    B.sort()
    #print(A)
    #print(B)
    if A[-1] > B[-1]:
        print(A[-1])
    else:
        print(B[-1])

=======
Suggestion 9

def main():
    #input
    n = int(input())
    a = [0]*n
    b = [0]*n
    for i in range(n):
        a[i],b[i] = map(int,input().split())
    
    #compute
    ans = min(max(a[i],b[j]) for i in range(n) for j in range(n) if i!=j)
    
    #output
    print(ans)
