Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    h = list(map(int, input().split()))
    for i in range(n-1):
        if h[i] < h[i+1]:
            h[i+1] -= 1
        if h[i] > h[i+1]:
            print("No")
            return
    print("Yes")

=======
Suggestion 2

def main():
    N = int(input())
    H = list(map(int, input().split()))
    for i in range(1, N):
        if H[i - 1] > H[i]:
            H[i] += 1
    for i in range(1, N):
        if H[i - 1] > H[i]:
            print('No')
            exit()
    print('Yes')

=======
Suggestion 3

def main():
    N = int(input())
    H = list(map(int, input().split()))

    for i in range(N-1):
        if H[i] > H[i+1]:
            H[i] -= 1
        if H[i] > H[i+1]:
            print('No')
            return
    print('Yes')

=======
Suggestion 4

def solve():
    n = int(input())
    h = list(map(int, input().split()))
    for i in range(n-1):
        if h[i] > h[i+1]:
            h[i] -= 1
    for i in range(n-1):
        if h[i] > h[i+1]:
            print('No')
            return
    print('Yes')

=======
Suggestion 5

def main():
    n = int(input())
    h = list(map(int,input().split()))
    for i in range(n-1):
        if h[i] < h[i+1]:
            h[i+1] -= 1
        if h[i] > h[i+1]:
            print('No')
            return
    print('Yes')

=======
Suggestion 6

def main():
    n = int(input())
    h = [int(i) for i in input().split()]
    for i in range(n-1):
        if h[i+1] < h[i]:
            h[i+1] += 1
    for i in range(n-1):
        if h[i+1] < h[i]:
            print('No')
            return
    print('Yes')

=======
Suggestion 7

def main():
    n = int(input())
    h = [int(x) for x in input().split()]
    for i in range(n-1,0,-1):
        if h[i] < h[i-1]:
            h[i-1] -= 1
        elif h[i] > h[i-1]:
            print("No")
            return
    print("Yes")

=======
Suggestion 8

def isNonDecreasing(arr):
    if len(arr) == 1:
        return True
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            return False
    return True

=======
Suggestion 9

def check(h):
    for i in range(1,len(h)):
        if h[i-1] > h[i]:
            h[i] += 1
    if sorted(h) == h:
        return True
    else:
        return False

n = int(input())
h = list(map(int, input().split()))

=======
Suggestion 10

def main():
    # Get input
    n = int(input())
    h = list(map(int, input().split()))

    # Initialize
    res = True
    h_max = h[0]

    # Loop
    for i in range(1, n):
        if h[i] >= h_max:
            h_max = h[i]
        elif h[i] == h_max - 1:
            h_max = h[i]
        else:
            res = False
            break

    # Output
    if res:
        print('Yes')
    else:
        print('No')
