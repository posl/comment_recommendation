Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    h = list(map(int, input().split()))
    print(h.index(max(h)) + 1)

=======
Suggestion 2

def main():
    n = int(input())
    h = [int(x) for x in input().split()]
    print(h.index(max(h))+1)

=======
Suggestion 3

def main():
    n = int(input())
    h = [int(i) for i in input().split()]
    print(h.index(max(h))+1)

=======
Suggestion 4

def solve():
    n = int(input())
    h = list(map(int, input().split()))
    print(h.index(max(h)) + 1)

=======
Suggestion 5

def main():
    #input
    n = int(input())
    h = list(map(int, input().split()))

    #process
    max = 0
    for i in range(n):
        if h[i] > max:
            max = h[i]

    #output
    print(h.index(max) + 1)

=======
Suggestion 6

def highest_bridge(bridge_heights):
    return bridge_heights.index(max(bridge_heights)) + 1
