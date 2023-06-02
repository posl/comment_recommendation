Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    h = list(map(int, input().split()))
    for i in reversed(range(n-1)):
        if h[i] > h[i+1]:
            h[i] -= 1
    for i in range(n-1):
        if h[i] > h[i+1]:
            print("No")
            return
    print("Yes")

=======
Suggestion 2

def main():
    n = int(input())
    h = list(map(int, input().split()))
    for i in range(n-1):
        if h[i] > h[i+1]:
            h[i] -= 1
    for i in range(n-1):
        if h[i] > h[i+1]:
            print('No')
            exit()
    print('Yes')

=======
Suggestion 3

def main():
    n = int(input())
    h = list(map(int, input().split()))
    for i in range(n-1):
        if h[i] > h[i+1]:
            h[i] -= 1
        if h[i] > h[i+1]:
            print('No')
            return
    print('Yes')

=======
Suggestion 4

def main():
    N = int(input())
    H = list(map(int,input().split()))
    for i in range(N-1):
        if H[i] < H[i+1]:
            H[i+1] -= 1
        if H[i] > H[i+1]:
            print('No')
            return
    print('Yes')
    return

=======
Suggestion 5

def solve():
    N = int(input())
    H = [int(i) for i in input().split()]
    for i in range(N-1):
        if H[i] > H[i+1]:
            H[i] -= 1
        if H[i] > H[i+1]:
            print("No")
            return
    print("Yes")
solve()

=======
Suggestion 6

def main():
    N = int(input())
    H = list(map(int, input().split()))
    for i in range(N-1):
        if H[i+1] - H[i] == 1:
            H[i+1] -= 1
        elif H[i+1] - H[i] > 1:
            print("No")
            return
    print("Yes")
    return

=======
Suggestion 7

def main():
    n = int(input())
    hs = list(map(int, input().split()))
    for i in range(n - 1):
        if hs[i + 1] - hs[i] > 1:
            print('No')
            return
        elif hs[i + 1] - hs[i] == 1:
            hs[i + 1] -= 1
    print('Yes')

=======
Suggestion 8

def main():
    N = int(input())
    H = list(map(int, input().split()))
    for i in range(N-1, 0, -1):
        if H[i] < H[i-1]:
            H[i-1] -= 1
        if H[i] < H[i-1]:
            print("No")
            return
    print("Yes")

=======
Suggestion 9

def main():
    N = int(input())
    H = list(map(int, input().split()))
    for i in range(N-1):
        if H[i] > H[i+1]:
            H[i] -= 1
    for i in range(N-1):
        if H[i] > H[i+1]:
            print('No')
            return
    print('Yes')
    return

=======
Suggestion 10

def main():
    n = int(input())
    h = list(map(int, input().split()))

    h.reverse()
    for i in range(1, n):
        if h[i-1] - h[i] >= 2:
            print("No")
            exit(0)
        elif h[i-1] - h[i] == 1:
            h[i-1] -= 1
    print("Yes")
