Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
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
Suggestion 2

def main():
    n = int(input())
    h = list(map(int, input().split()))
    for i in range(n-1):
        if h[i] > h[i+1]:
            h[i] -= 1
    for i in range(n-1):
        if h[i] > h[i+1]:
            print("No")
            exit()
    print("Yes")

=======
Suggestion 3

def main():
    N = int(input())
    H = list(map(int, input().split()))
    for i in range(N-1):
        if H[i] < H[i+1]:
            H[i+1] -= 1
        elif H[i] > H[i+1]:
            print('No')
            exit()
    print('Yes')

=======
Suggestion 4

def main():
    N = int(input())
    H = list(map(int, input().split()))
    for i in range(N - 1):
        if H[i] < H[i + 1]:
            H[i + 1] -= 1
        elif H[i] > H[i + 1]:
            print('No')
            return
    print('Yes')
    return

=======
Suggestion 5

def main():
    N = int(input())
    H = list(map(int,input().split()))
    for i in range(N-1):
        if H[i] > H[i+1]:
            H[i] -= 1
    for i in range(N-1):
        if H[i] > H[i+1]:
            print("No")
            exit()
    print("Yes")

=======
Suggestion 6

def solve():
    n = int(input())
    h = list(map(int, input().split()))
    for i in range(n - 1):
        if h[i] > h[i + 1]:
            h[i] -= 1
    for i in range(n - 1):
        if h[i] > h[i + 1]:
            print('No')
            return
    print('Yes')

=======
Suggestion 7

def main():
    n = int(input())
    h = list(map(int, input().split()))
    for i in range(1, n):
        if h[i] < h[i-1]:
            h[i] -= 1
        if h[i] < h[i-1]:
            print("No")
            return
    print("Yes")

=======
Suggestion 8

def main():
    N = int(input())
    H = list(map(int, input().split()))
    for i in range(N-1):
        if H[i] - H[i+1] > 1:
            print("No")
            return
        elif H[i] - H[i+1] == 1:
            H[i] -= 1
    print("Yes")

=======
Suggestion 9

def main():
    n = int(input())
    h = list(map(int, input().split()))
    if n == 1:
        print("Yes")
        return
    for i in range(n-1):
        if h[i] > h[i+1]:
            h[i] -= 1
        if h[i] > h[i+1]:
            print("No")
            return
    print("Yes")
