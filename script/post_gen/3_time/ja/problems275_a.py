Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    h = list(map(int, input().split()))
    print(h.index(max(h))+1)

=======
Suggestion 2

def main():
    n = int(input())
    h = list(map(int, input().split()))
    max_h = max(h)
    for i in range(n):
        if h[i] == max_h:
            print(i+1)
            break

=======
Suggestion 3

def problems275_a():
    n = int(input())
    h = list(map(int, input().split()))
    max = 0
    for i in range(n):
        if h[i] > max:
            max = h[i]
            max_index = i
    print(max_index+1)

=======
Suggestion 4

def main():
    n = int(input())
    h = list(map(int, input().split()))
    max_h = max(h)
    print(h.index(max_h) + 1)

=======
Suggestion 5

def solve():
    n = int(input())
    h = list(map(int,input().split()))
    max = 0
    for i in range(n):
        if h[i] > max:
            max = h[i]
            index = i + 1
    print(index)

=======
Suggestion 6

def main():
    N = int(input())
    H = list(map(int, input().split()))
    Hmax = max(H)
    print(H.index(Hmax)+1)
