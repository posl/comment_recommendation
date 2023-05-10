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

=======
Suggestion 2

def main():
    n = int(input())
    h = list(map(int, input().split()))
    for i in range(n-1):
        if h[i] > h[i+1]:
            if h[i] - h[i+1] == 1:
                h[i] -= 1
            else:
                print('No')
                return
    print('Yes')

=======
Suggestion 3

def main():
    n = int(input())
    h = list(map(int, input().split()))
    for i in range(n):
        if i == 0:
            continue
        if h[i] - h[i-1] >= 2:
            print("No")
            return
    print("Yes")
    return

=======
Suggestion 4

def solve():
    N = int(input())
    H = list(map(int, input().split()))
    for i in range(1, N):
        if H[i-1] > H[i]:
            H[i] += 1
    for i in range(1, N):
        if H[i-1] > H[i]:
            print('No')
            break
    else:
        print('Yes')

=======
Suggestion 5

def solve():
    N = int(input())
    H = list(map(int, input().split()))
    for i in range(1, N):
        if H[i-1] > H[i]:
            H[i] += 1
        if H[i-1] > H[i]:
            print('No')
            return
    print('Yes')
solve()

=======
Suggestion 6

def main():
    N = int(input())
    H = list(map(int, input().split()))
    for i in range(1, N):
        if H[i - 1] > H[i]:
            H[i] += 1
    for i in range(1, N):
        if H[i - 1] > H[i]:
            print('No')
            return
    print('Yes')

=======
Suggestion 7

def solve():
    N = int(input())
    H = list(map(int, input().split()))
    for i in reversed(range(1, N)):
        if H[i-1] > H[i]:
            H[i-1] -= 1
    for i in range(N-1):
        if H[i] > H[i+1]:
            print('No')
            return
    print('Yes')

=======
Suggestion 8

def main():
    n = int(input())
    h = list(map(int, input().split()))
    for i in range(n-1):
        if h[i] < h[i+1]:
            h[i+1] -= 1
        elif h[i] > h[i+1]:
            print('No')
            return
    print('Yes')

=======
Suggestion 9

def main():
    # n = int(input())
    # h = list(map(int, input().split()))
    n = 5
    h = [1, 2, 3, 4, 5]
    # n = 1
    # h = [1000000000]
    # n = 5
    # h = [1, 2, 1, 1, 3]
    # n = 4
    # h = [1, 3, 2, 1]
    # n = 5
    # h = [1, 2, 3, 4, 5]
    # n = 5
    # h = [1, 2, 3, 4, 4]
    # n = 5
    # h = [1, 2, 3, 4, 6]
    # n = 5
    # h = [1, 2, 3, 4, 4]
    # n = 5
    # h = [1, 2, 3, 4, 4]
    # n = 5
    # h = [1, 2, 3, 4, 4]
    # n = 5
    # h = [1, 2, 3, 4, 4]
    # n = 5
    # h = [1, 2, 3, 4, 4]
    # n = 5
    # h = [1, 2, 3, 4, 4]
    # n = 5
    # h = [1, 2, 3, 4, 4]
    # n = 5
    # h = [1, 2, 3, 4, 4]
    # n = 5
    # h = [1, 2, 3, 4, 4]

    # n = 6
    # h = [1, 2, 3, 4, 4, 4]

    # n = 7
    # h = [1, 2, 3, 4, 4, 4, 4]

    # n = 8
    # h = [1, 2

=======
Suggestion 10

def main():
    N = int(input())
    H = list(map(int, input().split()))
    for i in range(N-1):
        if H[i] < H[i+1]:
            H[i+1] -= 1
        elif H[i] > H[i+1]:
            print("No")
            return
    print("Yes")
