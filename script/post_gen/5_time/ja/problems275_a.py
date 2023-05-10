Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    h = list(map(int, input().split()))
    max_h = max(h)
    print(h.index(max_h) + 1)

=======
Suggestion 2

def main():
    n = int(input())
    h = list(map(int, input().split()))
    print(h.index(max(h))+1)

=======
Suggestion 3

def main():
    n = int(input())
    bridges = list(map(int, input().split()))
    max_height = 0
    for height in bridges:
        if height > max_height:
            max_height = height
    for i in range(n):
        if bridges[i] == max_height:
            print(i+1)
            break

=======
Suggestion 4

def main():
    N = int(input())
    H = list(map(int,input().split()))
    print(H.index(max(H))+1)

=======
Suggestion 5

def main():
    n = int(input())
    h = list(map(int, input().split()))
    max = 0
    for i in range(n):
        if h[i] > max:
            max = h[i]
    for i in range(n):
        if h[i] == max:
            print(i+1)
            break

=======
Suggestion 6

def main():
    N = int(input())
    H = list(map(int, input().split()))
    max = H[0]
    for i in range(1, N):
        if max < H[i]:
            max = H[i]
    print(H.index(max) + 1)
