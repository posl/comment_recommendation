Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    h = list(map(int, input().split()))
    for i in range(n-1):
        if h[i] > h[i+1]:
            h[i] -= 1
    print("Yes" if sorted(h) == h else "No")

=======
Suggestion 2

def main():
    N = int(input())
    H = [int(x) for x in input().split()]
    for i in range(N - 1):
        if H[i] > H[i + 1]:
            H[i] -= 1
    for i in range(N - 1):
        if H[i] > H[i + 1]:
            print("No")
            exit()
    print("Yes")

=======
Suggestion 3

def main():
    n = int(input())
    h = [int(x) for x in input().split()]
    for i in range(1, n):
        if h[i] > h[i-1]:
            h[i] -= 1
    for i in range(1, n):
        if h[i] < h[i-1]:
            print('No')
            return
    print('Yes')
    return

main()

=======
Suggestion 4

def main():
    n = int(input())
    h = [int(x) for x in input().split()]
    for i in range(n - 1):
        if h[i] > h[i + 1]:
            h[i] -= 1
        elif h[i] == h[i + 1]:
            pass
        else:
            print("No")
            return
    print("Yes")

=======
Suggestion 5

def main():
    N = int(input())
    H = list(map(int, input().split()))
    for i in range(N-1):
        if H[i] < H[i+1]:
            H[i+1] -= 1
        if H[i] > H[i+1]:
            print('No')
            return
    print('Yes')
    return

=======
Suggestion 6

def main():
    n = int(input())
    h = list(map(int, input().split()))
    for i in range(1, n):
        if h[i] > h[i-1]:
            h[i] -= 1
    for i in range(1, n):
        if h[i] < h[i-1]:
            print("No")
            return
    print("Yes")

=======
Suggestion 7

def main():
    n = int(input())
    h = list(map(int, input().split()))
    for i in range(n - 1):
        if h[i + 1] - h[i] >= 2:
            print("No")
            exit()
    print("Yes")

=======
Suggestion 8

def main():
    #n = int(input())
    #h = list(map(int, input().split()))
    n = 5
    h = [1, 2, 1, 1, 3]
    #n = 4
    #h = [1, 3, 2, 1]
    #n = 5
    #h = [1, 2, 3, 4, 5]
    #n = 1
    #h = [1000000000]
    #n = 10
    #h = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    #n = 10
    #h = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    #n = 10
    #h = [2, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    #n = 10
    #h = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11]
    #n = 10
    #h = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    #n = 10
    #h = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    #n = 10
    #h = [2, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    #n = 10
    #h = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11]
    #n = 10
    #h = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    #n = 10
    #h = [10, 9, 8,

=======
Suggestion 9

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
solve()

=======
Suggestion 10

def main():
    n = int(input())
    array = [int(x) for x in input().split()]
    max = array[0]
    for i in range(n):
        if array[i] > max:
            max = array[i]
        if array[i] < max - 1:
            print("No")
            return
    print("Yes")
