Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    H = list(map(int, input().split()))
    max = 0
    for i in range(N):
        if H[i] >= max:
            max = H[i]
    print(max)

=======
Suggestion 2

def main():
    N = int(input())
    H = list(map(int, input().split()))
    max = H[0]
    for i in range(1, N):
        if H[i] >= max:
            max = H[i]
    print(max)

=======
Suggestion 3

def main():
    N = int(input())
    H = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if ans < H[i]:
            ans = H[i]
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    H = list(map(int, input().split()))
    max_h = 0
    for i in range(N):
        if H[i] >= max_h:
            max_h = H[i]
    print(max_h)

=======
Suggestion 5

def main():
    n = int(input())
    h = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if ans < h[i]:
            ans = h[i]
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    H = list(map(int, input().split()))
    maxH = 0
    for i in range(N):
        if H[i] > maxH:
            maxH = H[i]
    print(maxH)

=======
Suggestion 7

def main():
    n = int(input())
    h = list(map(int, input().split()))
    max_h = 0
    for i in range(1, n):
        if h[i] >= max_h:
            max_h = h[i]
    print(max_h)

=======
Suggestion 8

def main():
    N = int(input())
    H = list(map(int, input().split()))
    maxH = 0
    for i in range(N):
        if (H[i] >= maxH):
            maxH = H[i]
    print(maxH)

=======
Suggestion 9

def main():
    N = int(input())
    H = list(map(int, input().split()))
    #print(N)
    #print(H)
    maxH = 0
    for i in range(N):
        if H[i] >= maxH:
            maxH = H[i]
    print(maxH)

=======
Suggestion 10

def main():
    N = int(input())
    H = list(map(int, input().split()))
    #print(N)
    #print(H)
    max_height = 0
    for i in range(N):
        if H[i] >= max_height:
            max_height = H[i]
    print(max_height)
