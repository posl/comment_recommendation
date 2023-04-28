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
    h = list(map(int, input().split()))
    max = 0
    for i in range(n):
        if h[i] > max:
            max = h[i]
            index = i+1
    print(index)

=======
Suggestion 3

def main():
    N = int(input())
    H = list(map(int, input().split()))

    print(H.index(max(H))+1)

=======
Suggestion 4

def get_highest_bridge(bridge_heights):
    return bridge_heights.index(max(bridge_heights)) + 1

=======
Suggestion 5

def get_int():
    return int(input().strip())
