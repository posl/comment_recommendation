Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    a.sort()
    b.sort()
    b.reverse()
    
    if a[0] > b[0]:
        print("No")
        return
    
    for i in range(n):
        if a[i] + b[i] > k:
            print("No")
            return
    
    print("Yes")
    return

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    a_max = max(a)
    a_min = min(a)
    b_max = max(b)
    b_min = min(b)
    
    if a_max - a_min > k or b_max - b_min > k:
        print("No")
    else:
        print("Yes")

=======
Suggestion 3

def solve():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    d = 0
    for i in range(N):
        d += abs(A[i]-B[i])
    if d <= K and (K-d)%2 == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def solve():
    pass

=======
Suggestion 5

def input_list():
    return list(map(int,input().split()))

=======
Suggestion 6

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    for i in range(n):
        if abs(a[i]-b[i]) > k:
            print("No")
            exit()
    print("Yes")

=======
Suggestion 7

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    l = 0
    r = k
    while l < r:
        m = (l + r) // 2
        if check(m, n, k, a, b):
            r = m
        else:
            l = m + 1
    print('Yes' if check(l, n, k, a, b) else 'No')

=======
Suggestion 8

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    for i in range(1, n):
        if abs(a[i] - a[i-1]) > k and abs(b[i] - b[i-1]) > k:
            print('No')
            return
    print('Yes')
    return

=======
Suggestion 9

def main():
    N, K = (int(x) for x in input().split())
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    if N == 1:
        if abs(A[0] - B[0]) <= K:
            print("Yes")
        else:
            print("No")
        return
    for i in range(N):
        if abs(A[i] - B[i]) > K:
            print("No")
            return
    print("Yes")
