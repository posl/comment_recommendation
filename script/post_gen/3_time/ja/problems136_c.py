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
            exit()
    print("Yes")
main()

=======
Suggestion 2

def main():
    N = int(input())
    H = list(map(int, input().split()))
    for i in range(N-1):
        if H[i] > H[i+1]:
            H[i] -= 1
    for i in range(N-1):
        if H[i] > H[i+1]:
            print('No')
            exit()
    print('Yes')

=======
Suggestion 3

def solve():
    N = int(input())
    H = list(map(int, input().split()))
    for i in range(N - 1):
        if H[i] > H[i + 1]:
            H[i] -= 1
    for i in range(N - 1):
        if H[i] > H[i + 1]:
            print('No')
            return
    print('Yes')

=======
Suggestion 4

def main():
    n = int(input())
    h = list(map(int, input().split()))
    for i in range(n-1):
        if h[i] > h[i+1]:
            h[i+1] += 1
    for i in range(n-1):
        if h[i] > h[i+1]:
            print('No')
            return
    print('Yes')

=======
Suggestion 5

def main():
    N = int(input())
    H = list(map(int, input().split()))

    for i in range(N-1):
        if H[i] > H[i+1]:
            H[i] -= 1
        if H[i] > H[i+1]:
            print("No")
            return
    print("Yes")

=======
Suggestion 6

def main():
    n = int(input())
    h = [int(x) for x in input().split()]
    for i in range(n-1):
        if h[i] > h[i+1]:
            h[i] -= 1
    for i in range(n-1):
        if h[i] > h[i+1]:
            print("No")
            exit()
    print("Yes")

=======
Suggestion 7

def main():
    N = int(input())
    H = list(map(int, input().split()))
    for i in range(1, N):
        if H[i] < H[i-1]:
            H[i] += 1
    for i in range(1, N):
        if H[i] < H[i-1]:
            print("No")
            return
    print("Yes")

=======
Suggestion 8

def main():
    N = int(input())
    H = list(map(int, input().split()))
    for i in range(1, N):
        if H[i] < H[i - 1]:
            H[i] -= 1
        if H[i] < H[i - 1]:
            print("No")
            return
    print("Yes")

=======
Suggestion 9

def main():
    n = int(input())
    h = list(map(int, input().split()))
    ans = 'Yes'
    for i in range(n - 1):
        if h[i] > h[i + 1]:
            h[i] -= 1
        if h[i] > h[i + 1]:
            ans = 'No'
            break
    print(ans)

=======
Suggestion 10

def main():
    n = int(input())
    h = list(map(int, input().split()))
    if n == 1:
        print('Yes')
        return
    for i in range(n-1):
        if h[i] > h[i+1]:
            h[i] -= 1
    for i in range(n-1):
        if h[i] > h[i+1]:
            print('No')
            return
    print('Yes')
    return
