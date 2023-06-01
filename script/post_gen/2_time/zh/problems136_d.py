Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    H = list(map(int, input().split()))
    for i in range(N-1):
        if H[i] > H[i+1]:
            H[i] -= 1
    for i in range(N-1):
        if H[i] > H[i+1]:
            print("No")
            break
    else:
        print("Yes")

=======
Suggestion 2

def check(heights):
    heights.sort()
    for i in range(len(heights)-1):
        if heights[i+1] - heights[i] > 1:
            return False
    return True

=======
Suggestion 3

def main():
    #n = 5
    #h = [1, 2, 1, 1, 3]
    #n = 4
    #h = [1, 3, 2, 1]
    #n = 5
    #h = [1, 2, 3, 4, 5]
    #n = 1
    #h = [1000000000]
    n = int(input())
    h = list(map(int, input().split()))
    h.reverse()
    for i in range(n - 1):
        if h[i] < h[i + 1]:
            h[i + 1] = h[i + 1] - 1
        if h[i] < h[i + 1]:
            print("No")
            return
    print("Yes")

=======
Suggestion 4

def main():
    n = int(input())
    h = list(map(int, input().split()))
    for i in range(n-1):
        if h[i] > h[i+1]:
            h[i] -= 1
    for i in range(n-1):
        if h[i] > h[i+1]:
            print("No")
            return
    print("Yes")
main()

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n-1):
        if a[i] < a[i+1]:
            a[i+1] -= 1
        elif a[i] > a[i+1]:
            print('No')
            return
    print('Yes')

=======
Suggestion 6

def main():
    n = int(input())
    heights = [int(i) for i in input().split()]
    for i in range(n-1):
        if heights[i] > heights[i+1]:
            heights[i] -= 1
    for i in range(n-1):
        if heights[i] > heights[i+1]:
            print("No")
            return
    print("Yes")
    return

=======
Suggestion 7

def solve(n, h):
    for i in range(n-1):
        if h[i+1] > h[i]:
            h[i+1] -= 1
        elif h[i+1] < h[i]:
            return False
    return True

n = int(input())
h = list(map(int, input().split()))
print('Yes' if solve(n, h) else 'No')

=======
Suggestion 8

def main():
    n = int(input())
    heights = input().split()
    heights = [int(height) for height in heights]
    for i in range(1,n):
        if heights[i] - heights[i-1] > 1:
            print("No")
            exit()
        elif heights[i] - heights[i-1] == 1:
            heights[i] -= 1
    print("Yes")

=======
Suggestion 9

def main():
    n = int(input())
    h = list(map(int, input().split()))
    for i in range(1, n):
        if h[i] - h[i - 1] >= 2:
            print("No")
            return
    print("Yes")

=======
Suggestion 10

def main():
    n = int(input())
    h = list(map(int, input().split()))

    for i in range(n - 1):
        if h[i] > h[i + 1]:
            h[i] -= 1
        elif h[i] == h[i + 1]:
            pass
        else:
            print('No')
            break
    else:
        print('Yes')
